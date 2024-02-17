import boto3
from botocore.exceptions import ClientError


def get_secret(secret_name, region_name="us-west-2"):
    import json

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    return json.loads(get_secret_value_response['SecretString'])

secrets = get_secret('SQUARE_API')
square_api_token = secrets['SQUARE_ACCESS_TOKEN']
location_id = secrets['LOCATION_ID']

secrets = get_secret('DJANGO')
key = secrets['DJANGO_SECRET_KEY']