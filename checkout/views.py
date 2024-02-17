from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404

def get_cart_data(request):
    cart_cookie = request.COOKIES.get('cart', '[]')
    return json.loads(cart_cookie)

from django.core.cache import cache
from miltzn.square_client import square_client
from products.views import format_items_response
def get_product(name):
    # product should be cached, but in case ...
    
    product = cache.get(name)
    if product is not None:
        return product
    
    result = square_client.catalog.search_catalog_items(
        body = {"text_filter": name}
    )

    if result.is_success():
        formatted_response = format_items_response(result.body)
        cache.set("items_response", formatted_response, timeout=604800)
        return formatted_response
    elif result.is_error():
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

def create_square_payment(line_items):
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
            "location_id": os.getenv('LOCATION_ID'),
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
            "state": "DRAFT",
            "pricing_options": {
                "auto_apply_taxes": False
            }
        }
    }
    # Create the order using Square API
    response = square_client.checkout.create_payment_link(body=order_data)
    return response

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def find_variant(product_variants, variation_name):
    for variant in product_variants:
        if variant["name"] == variation_name:
            return variant
    return None

@csrf_exempt
def checkout_view(request):
    if request.method == 'POST':
        cart_data = json.loads(request.body.decode('utf-8'))
        line_items = []

        for item in cart_data:
            product = get_product(item['name'])[0]
            variation = find_variant(product['variants'], item['variation'])
            if product:
                line_item = format_square_order_line_item(product['id']+variation['name'], product['name'], variation['price']['amount']/100, variation['name'], item['qty'])
                line_items.append(line_item)
        print('creating square payment')
        square_response = create_square_payment(line_items)
        if square_response.is_success():
            
            checkout_url = square_response.body['payment_link']['url']

            return JsonResponse({'checkout_url': checkout_url})
        else:
            # Handle errors
            return JsonResponse({'error': 'Error creating order'}, status=400)
        