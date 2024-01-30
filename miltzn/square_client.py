from square import client
from .secrets import square_api_token

square_client = client.Client(
    access_token=square_api_token,
    environment='sandbox'  # Change to 'production' in a live environment
)

if __name__ == "__main__":
    result = square_client.locations.list_locations()

    if result.is_success():
        for location in result.body['locations']:
            print(f"{location['id']}: ", end="")
            print(f"{location['name']}, ", end="")
            print(f"{location['address']['address_line_1']}, ", end="")
            print(f"{location['address']['locality']}")

    elif result.is_error():
        for error in result.errors:
            print(error['category'])
            print(error['code'])
            print(error['detail'])