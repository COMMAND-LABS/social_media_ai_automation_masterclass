#!/bin/bash

curl --location "https://api.heygen.com/v2/templates" \
     --header "accept: application/json" \
     --header "x-api-key: ${HEYGEN_API_KEY}" \