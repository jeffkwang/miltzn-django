from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseRedirect

def get_cart_data(request):
    cart_cookie = request.COOKIES.get('cart', '[]')
    return json.loads(cart_cookie)

from products.models import Product

def get_product_by_slug(slug):
    try:
        return Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        return None

def format_square_order_line_item(id, name, price, color, qty):
    return {
        "uid": str(id),
        "name": str(name),
        "quantity": str(qty),
        "variation_name": str(color),
        "base_price_money": {
            "amount": int(price * 100),  # Convert to cents
            "currency": "USD"
        }
    }

from miltzn.square_client import square_client
import uuid
import os
from miltzn.secrets import location_id

def create_square_payment(request, line_items):
    order_data = {
        "checkout_options": {
            "accepted_payment_methods": {
                "apple_pay": True,
                "google_pay": True,
            },
            "allow_tipping": False,
            "ask_for_shipping_address": True,
            "merchant_support_email": "jeff@miltzn.com"
        },
        "idempotency_key": str(uuid.uuid4()),
        "order": {
            "location_id": location_id,
            "line_items": line_items,
            "taxes": [
                {
                "name": "CA Tax",
                "type": "ADDITIVE",
                "percentage": "7.25"
                }
            ],
            "service_charges": [
                {
                "name": "Square Processing Fee",
                "percentage": "2.9",
                "calculation_phase": "SUBTOTAL_PHASE",
                "taxable": False,
                "scope": "ORDER"
                }
            ],
            "state": "OPEN",
            "pricing_options": {
                "auto_apply_taxes": False
            }
        }
    }
    # Create the order using Square API
    response = square_client.checkout.create_payment_link(body=order_data)
    return response

# from .models import create_order_in_db
import time
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def checkout_view(request):
    if request.method == 'POST':
        cart_data = json.loads(request.body.decode('utf-8'))
        line_items = []

        for item in cart_data:
            product = get_product_by_slug(item['slug'])
            if product:
                line_item = format_square_order_line_item(product.id, product.name, product.price, item['color'], item['qty'])
                line_items.append(line_item)
        
        square_response = create_square_payment(request, line_items)
        if square_response.is_success():
            checkout_url = square_response.body['payment_link']['url']  # Extract checkout URL
            # create_order_in_db(square_response.body)
            return JsonResponse({'checkout_url': checkout_url})
        else:
            # Handle errors
            return JsonResponse({'error': 'Error creating order'}, status=400)
        