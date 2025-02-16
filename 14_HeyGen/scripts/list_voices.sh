#!/bin/bash

response=$(curl --request GET \
     --url https://api.heygen.com/v1/voice.list \
     --header 'Accept: application/json' \
     --header "X-Api-Key: ${HEYGEN_API_KEY}")

# echo $response > voices_response.json # For debugging

# Use the following to find YOUR voice in HeyGen's list of supported voices
echo "$response" | tr -d '\000-\031' | jq -r '.data.list[] | select(.name == "Tad Duval") | .voice_id'