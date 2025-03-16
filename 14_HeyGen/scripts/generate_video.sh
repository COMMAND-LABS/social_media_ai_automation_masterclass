#!/bin/bash

curl -X POST https://api.heygen.com/v2/video/generate \
-H "X-Api-Key: ${HEYGEN_API_KEY}" \
-H "Content-Type: application/json" \
-d @- <<EOF
{
  "video_inputs": [
    {
      "character": {
        "type": "avatar",
        "avatar_id": "7cda91fe529746008869e50c8eb913e9",
        "avatar_style": "normal"
      },
      "voice": {
        "type": "text",
        "input_text": "Only 12 days away!",
        "voice_id": "cce692bffb474236ab42868496723b52",
        "speed": 1.0
      }
    }
  ],
  "dimension": {
    "width": 1280,
    "height": 720
  }
}
EOF