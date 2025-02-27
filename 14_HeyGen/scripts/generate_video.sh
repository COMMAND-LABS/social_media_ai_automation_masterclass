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
        "avatar_id": "148aa78267f84bdb8c88035378334c6d",
        "avatar_style": "normal"
      },
      "voice": {
        "type": "text",
        "input_text": "Hello to everyone who is attending tonight's A.I. Social Media Masterclass at THE HUB presented in partnership with Supercharged Magazine! For those who couldn't make it we are sending many blessings. For those who are on their way be sure to connect with everyone who is present before heading home and know that what we will be exploring tonight is literally the tip of the iceberg. Be ready to get your hands dirty and know in advance that you will run into many technical issues but we have a great team here to support and guide you. Arrive early and bring your A plus game.",
        "voice_id": "e7e6ad7c235748fe9147884f26c3af94",
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