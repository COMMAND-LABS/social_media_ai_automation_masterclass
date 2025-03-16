import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.heygen.com/v1/webhook/endpoint.add"
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": os.getenv('HEYGEN_API_KEY')
}
data = {
    "url": "https://hook.us2.make.com/k23gukiv5b5b9x2zfpdq1qww16pb3hn0", # copied from the webhook from Make.com
    "events": ["avatar_video.success"]
}

response = requests.post(url, json=data, headers=headers)

print(response.status_code)
print(response.json()) 