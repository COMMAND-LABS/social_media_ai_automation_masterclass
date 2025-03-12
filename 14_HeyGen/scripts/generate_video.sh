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
        "input_text": "Good morning Noelle and Elena! ACTION ITEM 1 FOR NOELLE: Let's connect (or perhaps just connect me with your team member?) for marketing the MASTERCLASS on March 27th, 2025 throughout the Office Logic network. BONUS ACTION ITEM FOR NOELLE: Send out an email asking for sponsors for the March 27th, 2025 MASTERCLASS - We need a Venue Sponsor at 500 dollars and an A.I. Sponsor at 700 dollars. ACTION ITEM 1 FOR ELENA: Collect testimonials from the past attendees of the A.I. Social Media MASTERCLASS. BONUS ACTION ITEM FOR ELENA: Send out a survey for fielding interest in a corporate level event. Some ideas to suggest to your audience are: A) n8n, B) Google Cloud, C) Azure AI Foundry, D) Pinecone, E) Databricks, F) Ask your audience for a suggestion. My survey has shown Google Cloud has the most interest so far but only 2 people voted.",
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