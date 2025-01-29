# TLDR

Tips for authenticating Make.com with X.com

## FYI

According to my understanding, the X.com (formerly Twitter) API has multiple APIs that can require slightly different authentication approaches to set up depending on what you would like to do.

## Reference links

- https://www.make.com/en/help/app/twitter#create-a-custom-application-in-x--formerly-twitter- 
- https://developer.x.com/en/portal/projects/1867631503221325824/apps/29761167/keys
- https://www.youtube.com/watch?v=cFfJATte6-M


## OAuth 2.0 Connection

On the X.com Developer Portal, copy the...

- OAuth 2.0 Client ID - ZVlXZ3pSWlBqbEdJb1VkeThFZjE6MTpjaQ
- Client Secret - 🤫

## Uploading media to X.com (photos & videos) requires a v5 Make.com connection

For the v5 Make.com integration with X.com you'll need to authenticate using the `Consumer Keys` found in the
`Keys and tokens` tab of your App in the X.com Developer Portal

## FYI regarding the `X (formerly Twitter) - Upload a Media` node

Supports uploading images AND videos

## Creating a post to X.com require a v6 Make.com connection

For the v6 Make.com integration with X.com you'll need to authenticate using the `OAuth 2.0 Client ID and Client Secret`
keys found in the `Keys and tokens` tab of your App in the X.com Developer Portal