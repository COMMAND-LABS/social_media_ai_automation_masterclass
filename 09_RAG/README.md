# TLDR

This is a blueprint for performing retrieval augmented generation for producing content that is more aligned to your tone, voice, and history of posting.

## Prerequisites

- Pinecone - https://www.pinecone.io/
- Google Sheets - https://workspace.google.com/products/sheets/
  - Create a spreadsheet with 2 sheets (`Knowledge` & `Query`)
- OpenAI - https://platform.openai.com/docs/overview

## References

- https://www.youtube.com/watch?v=DNDI4c3z-6A&t=456s
- https://www.youtube.com/watch?v=epz94WIvIYk
- https://docs.google.com/spreadsheets/d/1rvdUA5lUKbCCN2IWM0nrEj90J6jRSR4AdoUzPkzwFPA/edit?gid=0#gid=0

## PART 1: Steps for creating knowledge base aka `blueprint_9a.json`

- Create a Google Sheet (called `Knowledge`) with the following headers:
  - Post
  - Platform
  - Link to post

- Add "Google Sheets - Get Range Values" node
  - And specify range

- Add "OpenAI - Make an API Call" node
  - https://platform.openai.com/docs/api-reference/embeddings/create
  - URL: `/v1/embeddings`
  - Method: `POST`
  - Body: `{"input": "The food was delicious and the waiter...","model": "text-embedding-ada-002","encoding_format": "float"}`
  - Make the "input" key's value dynamic based on ONE of the rows in the spreadsheet

- Add "Tool - Set variable" node
  - Here's the code to make the "input" key's dynamic value JSON Safe - `{{replace(replace(replace(replace(replace(replace(replace(4.fullRecord; "/\n/g"; space); "/\r/g"; space); "/\t/g"; space); "/\f/g"; space); "/\//g"; "/"); "/\\/g"; "\\"); "/""/g"; "\""")}}`

- Add another "Tool - Set variable" node
  - Add it right after the "Google Sheets - Get Range Values" node
  - This is for compiling the data from each row into a single record followed by escaping it and then
  followed by sending it to the /v1/embeddings API from OpenAI for conversion into a Vector

- Set up Pinecone
  - https://www.pinecone.io/
  - Create an index that uses the `text-embedding-3-small` model
    - which has 1,536 dimensions
    - call the index whatever you like for example `text-embedding-3-small` 😊
    - Create an API in the Pinecone dashboard
    - Copy the index "host" from the Pinecone dashboard into the Index Name field of the Make.com node
      - https://text-embedding-3-small-2s9gzmx.svc.aped-4627-b74a.pinecone.io
      - Strip the `https://` and `.pinecone.io` and you're left with `text-embedding-3-small-2s9gzmx.svc.aped-4627-b74a`
  
- Add "Pinecone - Get a Vector" node
  - Vector ID - `1. Link to post (C)`
  
- Add "Pinecone - Upsert a Vector" node
  - Vector ID - `1. Link to post (C)`
  - Values - `2. Body.data[` `]: embedding`
  - Metadata
    - content (String) - `4. fullRecord`
    - platform (String) - `1. Platform (B)`
    - unique_hash (String) - `{{sha256(4.fullRecord)}}`

- Set up a filter between the "Get a Vector" & "Upsert a Vector" nodes
  - `6. Vector ID` Does not exist OR `6. Metadata: unique_hash` Not equal to `{{sha256(4.fullRecord)}}`

SIDENOTE: Peep ref_1.png

## PART 2: Steps for running RAG `blueprint_9b.json`

- Create a Google Sheet (called `RAG`) in the same spreadsheet used for `PART 1` with the following headers:
  - Prompt
  - RAG

- Add "Google Sheets - Get Range Values" node
  - And specify range (ie: A2:B2)

- Add an "OpenAI - Create a Completion (Prompt)" node
  - This step was just to test that completion calls are working

- Add another "OpenAI - Create a Completion (Prompt)" node
  - add it right after the "Google Sheets - Get Range Values" node
  - Configure the node with 2 messages
    - System: `You are a helpful assistant. I have a Pinecone knowledge base holding some of my past high-performing posts across various social media platforms. I'd like you generate a search term that I can use to retrieve the most similar past posts based on my objective so I can thereafter generate new marketing copy in the style of my posts. Respond in JSON like so: { "search_term": string }`
    - Toggle on Show advanced settings
      - Response Format: `JSON Object`
      - Parse JSON Response: `Yes`
    - User: `1. Prompt (A)`

- Add "OpenAI - Make an API Call" node
  - https://platform.openai.com/docs/api-reference/embeddings/create
  - URL: `/v1/embeddings`
  - Method: `POST`
  - Body: `{"input": "{{3.result.search_term}}","model": "text-embedding-ada-002","encoding_format": "float"}`
  - Make the "input" key's value dynamic based on ONE of the rows in the spreadsheet

- Add "Pinecone - Query Vectors" node after the "OpenAI - Make an API Call" node
  - Toggle on Vector Map feature
  - Vector: {{5.body.data[].embedding}}
  - Include Metadata: Yes
  - Limit: 3 (aka how many search results you want back)

- Add "Array aggregator" node
  - Source Module: Pinecone - Query Vectors [6]
  - Aggregated fields: VectorID, Metadata

- Add "JSON - Transform to JSON" node
  - Object: {{7.array}}

- Update the "OpenAI - Create a Completion (Prompt)" node from the 3rd step of Part 2
  - Configure the node with 1 message
    - User: (awkward but breaking to a new line)

```md - User prompt for reference
# PROMPT
{{1.`0`}}

## Requirements

The relevant knowledge holds a list of the most related past posts of Tad Duval so you can generate new marketing material in an authentic and original style. Only include the provided information as the source of tone, voice, and style for generated content

## RELEVANT KNOWLEDGE

{{8.json}}
```

- Add a "Google Sheets - Update a Cell" node
  - Use the same spreadsheet id as used in previous steps
  - Sheet Name: `RAG`
  - Cell: B + (the number of the same row being processed)
  - Value: {{2.result}} (aka the output of the RAG response)

## Closing Remarks

And that should do it!