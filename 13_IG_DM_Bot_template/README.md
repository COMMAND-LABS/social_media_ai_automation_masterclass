# TLDR

Info about connecting to ManyChat in order to build an IG DM bot

## Reference tutorial

- https://www.youtube.com/watch?v=6OpwwC19cgE (GOLD)

## Requirements

- Manychat "Pro" plan
  - Needed to provide Credit Card details

## Connect Manychat with Make.com

- Add Manychat "Watch Incoming Data" Hook
- Get an API key from the Manychat "Settings" page
  - Settings > Extensions > API
  - Copy Manychat API key to the Manychat module in Make.com

## Create Manychat custom fields

- Settings
  - Fields
    - New User Field - "Assistant - Prompt"
    - New User Field - "Assistant - Completion"
    - New User Field - "Assistant - Thread ID"


## Set up the Default Reply (AKA an automation in Manychat)

- Settings
  - Instagram
  - Default Reply
