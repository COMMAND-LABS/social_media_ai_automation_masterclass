#!/bin/bash

response=$(curl --request GET \
  --url https://api.heygen.com/v2/avatars \
  --header 'Accept: application/json' \
  --header "X-Api-Key: ${HEYGEN_API_KEY}")

if [[ -z "$response" ]]; then
  echo "Empty response received. Possible API error."
fi

# echo $response > avatar_response.json # For debugging

# Use the following to find YOUR avatar in HeyGen's list of supported avatars
echo "$response" | jq -r '.data.avatars[] | select(.avatar_name == "Tad Duval") | .avatar_id'