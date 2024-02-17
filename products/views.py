# Square Catalog Views and Helpers

def find_category_by_id(categories, category_id):
    for category in categories:
        if category['id'] == category_id:
            return category['name'], category['href']
    return None, None

def splitDescription(description):
    sections = description.split("\n\n")
    description = ""
    highlights = []
    details = ""

    for section in sections:
        if "Highlights" in section:
            highlights = section.replace("Highlights", "").strip()
            highlights = section.replace("Highlights", "").strip().split("\n")
        elif "Details" in section:
            details = section.replace("Details", "").strip()
        else:
            # Assume the section is part of the description
            description += section.strip()

    return [description, highlights, details]

def getImageUrls(imageID):
    result = square_client.catalog.retrieve_catalog_object(
          object_id = imageID
    )

    if result.is_success():
        return result.body['object']['image_data']['url']
    elif result.is_error():
        print(result.errors)

def format_items_response(response):
    '''
    Filters the response text as a dictionary with the following fields:
    - id : item ID gathered from Square catalog
    - name : name of the product
    - description : description of the product
    - highlights : highlights of the product
    - details : details of the product
    - href : product url path
    - src : the first image provided by the item
    - alt : the item's name (for ease of programming)
    - price : the range of the price of the item, based off all of its variants
    - category_name : the category that the product belongs to
    - category_href : the path of the category
    - variants : list of variations (name, price, inStock, image_urls) as Dict objects
    '''

    formatted_items = []
    categoryDict = getCategoriesFromSquare()

    firstItem = next(iter(response.keys()))
    itemType = str(response[firstItem][0]["type"]).lower()
    item_data = itemType + "_data"

    if itemType == "item":
        for item in response[firstItem]:
            item_id = item.get('id', '')
            item_name = item[item_data].get('name', '')
            item_image_uris = item[item_data].get('ecom_image_uris', [])
            item_image_src = item_image_uris[0] if item_image_uris else ''  
            item_image_alt = item[item_data].get('name', '')
            item_href = item[item_data]['ecom_seo_data'].get('permalink', '') 

            item_description = item[item_data].get('description', '')
            description, highlights, details = splitDescription(item_description)

            variation_prices = [variation['item_variation_data']['price_money']['amount'] / 100 for variation in item[item_data]['variations']]
            price_range = f"${min(variation_prices):.2f} - ${max(variation_prices):.2f}"
            variation_data = item[item_data]['variations']
            
            variations = [{ "name": variant["item_variation_data"]["name"][0], 
                           "price": variant["item_variation_data"]["price_money"], 
                           "inStock": variant["item_variation_data"]["sellable"],
                           "image_urls": [getImageUrls(imageID) for imageID in variant["item_variation_data"]["image_ids"]] } for variant in variation_data]

            category_id = item[item_data]['reporting_category']['id']
            category_name, category_href = find_category_by_id(categoryDict, category_id)

            formatted_items.append({
                'id': item_id,
                'name': item_name,
                'description': description,
                'highlights': highlights,
                'details': details,
                'href': item_href,
                'src': item_image_src,
                'alt': item_image_alt,
                'price': price_range,
                'category_name': category_name,
                'category_href': category_href,
                'variants': variations,
            })

    return formatted_items

from miltzn.square_client import square_client 
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def getCatalogItemsFromSquare(request):

    items_response = cache.get("items_response")
    if items_response is not None:
        return JsonResponse({'items': items_response})
    
    result = square_client.catalog.search_catalog_items(
        body = {}
    )
    
    if result.is_success():
        
        formatted_response = format_items_response(result.body)
        cache.set("items_response", formatted_response, timeout=604800)
        return JsonResponse({'items': formatted_response})
    elif result.is_error():
        return JsonResponse({'error': result.errors}, status=400)

def getCategoriesFromSquare():
    # check if cache table contains categories key
    #   if not, query Square to retrieve the category data
    #   save the category data to the cache table
    #   return the category data
    # if cache table contains categories key
    #   return the category data

    categories_data = cache.get("categories_data")
    if categories_data is not None:
        return categories_data
    
    result = square_client.catalog.search_catalog_objects(
    body = {
        "object_types": [
        "CATEGORY"
        ]
    }
    )

    if result.is_success():
        raw_categories = result.body['objects']
        categories_data = [{
            'id': category['id'],
            'name': category['category_data']['name'],
            'href': category['category_data']['ecom_seo_data'].get('permalink'),
        } for category in raw_categories]

        cache.set("categories_data", categories_data, timeout=3600)
        return categories_data
    elif result.is_error():
        return []

def getItemDetails(request, name):

    items_response = cache.get(name)
    if items_response is not None:
        return JsonResponse({'items': items_response})

    result = square_client.catalog.search_catalog_items(
        body = {
            "text_filter": name
        }
    )
    

    if result.is_success():
        cache.set(name, format_items_response(result.body), timeout=604800)

        return JsonResponse({'items': format_items_response(result.body)})
    elif result.is_error():
        return JsonResponse({'error': result.errors}, status=400)