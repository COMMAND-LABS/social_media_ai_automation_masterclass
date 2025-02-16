#!/bin/bash

if [ -z "${HEYGEN_API_KEY}" ]; then
     echo "Error: HEYGEN_API_KEY is not set."
     exit 1
fi

VIDEO_ID="bf314209bfc64306b60e97db90d3402a" # Replace with your actual video ID

curl --request GET \
     --url https://api.heygen.com/v1/video_status.get?video_id=$VIDEO_ID \
     --header 'Accept: application/json' \
     --header "X-Api-Key: ${HEYGEN_API_KEY}"