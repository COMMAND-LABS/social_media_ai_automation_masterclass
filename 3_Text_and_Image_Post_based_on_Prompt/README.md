# TLDR

This folder holds the Make.com automation blueprints for automating the creation and distribution
of Text + Image posts by leveraging Make.com and OpenAI's GPT and DALLE APIs. The content will be distributed to 
an `X.com account` and a `LinkedIn Personal Account`.

## Requirements

- OpenAI Platform Account - https://platform.openai.com/
- gotoHuman Account - https://www.gotohuman.com/
- X.com Account - https://x.com/
- LinkedIn Account - https://www.linkedin.com/
- Make.com Account - https://www.make.com/
- Some tenacity
  - You will need to configure & connect each blueprint after importing it into your Make.com account.
  - Build a compatible form in gotoHuman: https://docs.gotohuman.com/Integrations/make-com

## `Blueprint 1` - Generate "Text & Image" Post for LinkedIn & X

This automation takes a single prompt and generates 3 pieces of information...

1 - a text post for LinkedIn
2 - a text for X.com
3 - an image

After these 3 outputs are generated, they are sent to a platform called gotoHuman where they can be reviewed.
In gotoHuman you can "approve" or "reject" the generated content.
If "approved" then `Blueprint 2` gets trigged and if "rejected" then nothing happens.

Make sure to set up a form in gotoHuman that contains the following fields (check out ref_1.png)

- 1 - id: `images` - "Images" field type
- 2 - id: `x_dot_com_text` - "Text (Long)" field type
- 3 - id: `linkedin_text` - "Text (Long)" field type
- 4 - id: `approval` - "Button Group" field type

Add the gotoHuman API key found at the bottom of the Form builder into Make.com to integrate the
"Create a Review Request" node (check out ref_2.png)

## `Blueprint 2` - Distribute the approved content to LinkedIn & X

Make sure to add the gotoHuman webhook to the "Watch the Review Response" node to connect Blueprint 2 to gotoHuman.

Make sure to "activate" the Blueprint 2 Scenario so it automatically gets triggers after the 
gotoHuman review process.

After the approved content is submitted then it will be posted to LinkedIn & X.com.