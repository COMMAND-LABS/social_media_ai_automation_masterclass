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

## Steps for creating knowledge base aka `blueprint_1.json`

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

## Steps for running RAG `blueprint_2.json`

- Create a Google Sheet (called `RAG`) with the following headers:
  - Post
  - Platform
  - Link to post