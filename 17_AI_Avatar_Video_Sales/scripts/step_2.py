import json

import os
from dotenv import load_dotenv
import json
import requests

load_dotenv()

# Path to the JSON file
json_file_path = 'data/generated_scripts_2025-03-15.json'

# Load the JSON data
with open(json_file_path, 'r') as file:
  scripts_data = json.load(file)

# Loop through each script and print its contents
for script in scripts_data:
  
  api_key = os.getenv('HEYGEN_API_KEY')
  url = "https://api.heygen.com/v2/video/generate"
  headers = {
    "X-Api-Key": api_key,
    "Content-Type": "application/json"
  }
  data = {
    "video_inputs": [
        {
            "character": {
                "type": "avatar",
                "avatar_id": "7cda91fe529746008869e50c8eb913e9",
                "avatar_style": "normal"
            },
            "voice": {
                "type": "text",
                "input_text": script.get("script"),
                "voice_id": "cce692bffb474236ab42868496723b52",
                "speed": 1.0
            }
        }
    ],
    "dimension": {
        "width": 1280,
        "height": 720
    },
    "callback_id": script.get("prospect_name")
  }
  response = requests.post(url, headers=headers, data=json.dumps(data))
  if response.status_code == 200:
    print("Response:", response.json())
  else:
    print(f"Error {response.status_code}: {response.text}")