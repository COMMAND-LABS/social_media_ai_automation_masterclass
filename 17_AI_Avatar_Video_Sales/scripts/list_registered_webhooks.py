import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('HEYGEN_API_KEY')

url = "https://api.heygen.com/v1/webhook/endpoint.list"

headers = {
    "Accept": "application/json",
    "X-Api-Key": api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")