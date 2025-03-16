from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

# Initialize the OpenAI client
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(profile):  
  response = openai.responses.create(
      model="gpt-4o-mini",
      instructions="You are an outbound sales specialist.",
      input=f""""
      # TASK

      Craft a 2-4 sentence personalized message to {profile.get("firstName")} {profile.get("lastName")} in regards to the MASTERCLASS taking place on 3/27/2025 in Miami, FL.
      The script will be read by a sales representative to record a personalized video message for the
      prospective guest. The final video message will be sent via LinkedIn.

      ## CONTEXT

      - The masterclass is about A.I. Video Automation and its impact on business.
      - There is still the $500 sponsorship opportunity available to cover the venue costs
      - There is still the $700 sponsorship opportunity to cover the A.I. costs
      - The goal is also to get the prospect to suggest businesses and business owners in their network to fill the remaining 2 sponsorship slots.
      
      ## PROSPECT PROFILE

      ```json
      {json.dumps(profile)}
      ```

      ## EVENT DETAILS

      - Name: A.I. Social Media Masterclass
      - Location: Office Logic, Edgewater, Miami, FL
      - Date: 3/27/2025 6pm-10pm EST
      - CTA Link: https://lu.ma/supercharged

      ## REQUIREMENTS
      - Make the output natural and impossible to detect as being A.I. generated
      - Use spacing and new lines to make the marketing copy easy to read
      - Use minimal emojis
      - The goal is to convert readers to sign up the event
      - Do NOT include the CTA Link in the style as it does not fit the style
      - Do NOT bold any text when generating the copy for LinkedIn
      - Avoid using the **TEXT** characters for emphasizing LinkedIn copy as it does NOT align to my style
      """
  )

  print('GENERATED SCRIPT...')
  print(response.output_text)
  print()

  return response.output_text

# Path to the JSON file
# json_file_path = 'data/dataset_linkedin-profile-scraper_2025-03-15.json'
json_file_path = 'data/staged_profiles.json'

# Read the JSON file
with open(json_file_path, 'r') as file:
  prospects = json.load(file)

# Loop through the contents of the JSON file

invitation_scripts = []
for prospect in prospects:
  print(f"Generating script for {prospect.get('firstName')} {prospect.get('lastName')}")
  script = generate_script(prospect)

  invitation_scripts.append({
    'prospect_name': f"{prospect.get('firstName')} {prospect.get('lastName')}",
    'script': script
  })

# Save the generated scripts to a new JSON file
output_file_path = 'data/generated_scripts_2025-03-15.json'
with open(output_file_path, 'w') as output_file:
  json.dump(invitation_scripts, output_file, indent=4)
  