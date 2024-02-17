from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json 
import uuid
from .models import Customer
import logging

logging.basicConfig(filename='logs/customer_signups.log', level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()
logger.filter('REQUEST')

@csrf_exempt
def customerExists(request):
    data = json.loads(request.body.decode('utf-8'))
    email = data.get('email')

    exists = Customer.objects.customerExists(email)

    return JsonResponse(exists)

@csrf_exempt
def customers_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        email = data.get('email')
        uid = data.get('uid')

        try:
            new_customer = Customer.objects.create(
                email=email, 
                auth_id=uid, 
                idempotency_key=str(uuid.uuid4())
            )
            logging.info(f"New customer signed up: {email}", extra={'tag': 'REQUEST'})

            return JsonResponse({'message': 'Customer signup success!'})
        except Exception as e:
            logging.error(f"Error occurred during customer signup: {str(e)}", extra={'tag': 'REQUEST'})
            return JsonResponse({'error': 'An error occurred during customer signup'}, status=500)
    else:
        logging.warning(f"Method not allowed: {request.method}")
        return JsonResponse({'error': 'Method not allowed'}, extra={'tag': 'REQUEST'}, status=405)

@csrf_exempt
def update_customer_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        customer_id = data.get('customer_id')
        try:
            customer = Customer.objects.get(customer_id=customer_id)
        except Customer.DoesNotExist:
            return JsonResponse({'error': f'Customer with ID {customer_id} does not exist'}, status=404)
        
        try:
            response = customer.update(**data)
            return response
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)


