import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('HEYGEN_API_KEY')
endpoint_id = "737e50776df74183a4a7e608da1d671e" # Retrievable from the list_registered_webhooks.py script
url = f"https://api.heygen.com/v1/webhook/endpoint.delete?endpoint_id={endpoint_id}"
headers = {
    "Accept": "application/json",
    "X-Api-Key": api_key
}

response = requests.delete(url, headers=headers)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")