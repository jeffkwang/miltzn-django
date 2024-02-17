from django.db import models
from miltzn.square_client import square_client
from django.http import JsonResponse
from django.core.exceptions import ValidationError

class CustomerManager(models.Manager):
    def create(self, **kwargs):
        """
        Custom create method to create a new customer instance.
        """ 
        idempotency_key = kwargs.get('idempotency_key')
        email_address = kwargs.get('email')
        if not (idempotency_key and email_address):
            return JsonResponse({'error': 'Missing required parameters'}, status=400)

        # Call Square API to create customer
        result = square_client.customers.create_customer(
            body={
                "idempotency_key": idempotency_key,
                "email_address": email_address
            }
        )

        if result.is_success():
            # Optionally, do something with the response body
            print(result.body)
            customer_id = result.body['customer']['id']
            kwargs['customer_id'] = customer_id
        elif result.is_error():
            # Log or handle the error
            print(result.errors)
            return JsonResponse({'error': 'Bad request'}, status=400)
        
        try:
            # Attempt to create the customer object
            new_customer = super().create(email=kwargs.get('email'), 
                auth_id=kwargs.get('auth_id'), customer_id=kwargs.get('customer_id'))
            return new_customer
        except ValidationError as e:
            # Log the error message if validation fails
            print(f"Validation error occurred during customer creation: {e}")
            return JsonResponse({'error': 'Validation error'}, status=400)
        except Exception as e:
            # Log any other unexpected errors
            print(f"An unexpected error occurred during customer creation: {e}")
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)
        
    def customerExists(self, email):
        result = square_client.customers.search_customers(
        body = {
            "query": {
            "filter": {
                "email_address": {
                "exact": email
                }
            }
            }
        }
        )

        if result.is_success():
            if not result.body: 
                response_data = {'exists': 'false'}
            else:
                response_data = {'exists': 'true'}
            return response_data
        elif result.is_error():
            print(result.errors)
            JsonResponse({'error':'Bad request'}, status=400)

from django.core.exceptions import FieldDoesNotExist

class Customer(models.Model):
    email = models.EmailField(max_length=255, verbose_name="Email address", unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=100, unique=True, primary_key=True)
    auth_id = models.CharField(max_length=100, unique=True)
    birthday = models.CharField(max_length=20, blank=True, verbose_name="Birthday")
    company_name = models.CharField(max_length=255, blank=True, verbose_name="Company name")
    family_name = models.CharField(max_length=255, blank=True, verbose_name="Family name")
    given_name = models.CharField(max_length=255, blank=True, verbose_name="Given name")
    nickname = models.CharField(max_length=255, blank=True, verbose_name="Nickname")
    note = models.TextField(blank=True, verbose_name="Note")
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Phone number")
    reference_id = models.CharField(max_length=255, blank=True, verbose_name="Reference ID")

    objects = CustomerManager()
    
    def update(self, **kwargs):
        """
        Custom update method to update fields of the customer instance.
        """
        for field, value in kwargs.items():
            try:
                self._meta.get_field(field)
            except FieldDoesNotExist:
                raise ValueError(f"Invalid field '{field}' specified in kwargs")
            
            setattr(self, field, value)
        self.save()

        result = square_client.customers.update_customer(
            customer_id = self.customer_id,
            body = kwargs
        )

        if result.is_success():
            print(result.body)
            return JsonResponse({'message': 'Customer updated successfully'}, status=200)
        elif result.is_error():
            print(result.errors)
            return JsonResponse({'error': 'Bad request'}, status=400)

    def __str__(self):
        return f"{self.given_name} {self.family_name} - {self.email_address}"