# TLDR

Documenting steps of setting up a Google Sheets "Spreadsheet" tool to give to a "Lead Gen" Agent

##

- Create a GCP Service Account
- Add a JSON key to the Service Account (SA)
- Extract the "client_email" from the Service Account (SA) .json file
- Create a spreadsheet in Google Sheet and grant the "client_email" Editor access
- Go to Replit and add another "App Secret" to the "Lead Gen Bot" Repl
  - call it `GOOGLE_CREDENTIALS` and paste in the SA json
  - add a file called `add_lead_to_google_sheet.py`
  - add a file called `add_lead_to_google_sheet_tool_definition.py`
  - in the Replit console add `gspread` -> `poetry add gspread`
  - in the Replit console add `oauth2client` -> `poetry add oauth2client`
  - add the Google Sheet ID to the Replit tool function code: `1frcV3MUEsPHePcaxjEwfbtMOv6TRTFzej9y2Mx-ia64`
  - 

