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
        "input_text": "Hello GPTuesdays community,\n\nI've included a mini-project below for how to leverage the HeyGen API. HeyGen has 2 websites that you can use in combination with each other to generate 'Avatar' videos like this one: app dot heygen dot com and docs dot heygen dot com. You can create your personalized avatar on app.heygen.com and then retrieve an API key from docs.heygen.com. In the mini-project, I've included a README with some additional tips too for those interested to try this out. One practical business application for this technology is for sales outreach. My feedback from several A.I. Avatar Sales experts is that when done on an ICP with great script writing and well-timed sequences, avatars like the ones offered by HeyGen can convert to booked appointments at a rate of about 3%. The last tip I'll share is to make sure to speak with a bit of energy and emotion when providing the video for generating your avatar. I generated mine while half asleep at 4 in the morning which is why this avatar sounds a bit flat. The other A.I. avatar video platform I'm hearing great things about is Synthesia if you're looking for alternatives. Enjoy!",
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