from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv

load_dotenv()

# Pinecone API key and environment
API_KEY = os.getenv("PINECONE_API_KEY")
ENVIRONMENT = "us-east-1"
INDEX_NAME = "text-embedding-3-small"

pc = Pinecone(
    api_key=os.environ.get("PINECONE_API_KEY")
)

# Connect to index
index = pc.Index(INDEX_NAME)

def delete_records(ids=None, delete_all=False):
    """
    Deletes records from the Pinecone index.
    
    :param ids: List of record IDs to delete.
    :param delete_all: If True, deletes all records from the index.
    """
    if delete_all:
        index.delete(delete_all=True)
        print(f"Deleted all records from index: {INDEX_NAME}")
    elif ids:
        index.delete(ids=ids)
        print(f"Deleted records with IDs: {ids}")
    else:
        print("No IDs provided and delete_all is False. No action taken.")

# Example usage:
# Delete specific records
# delete_records(ids=["id1", "id2", "id3"])

# Delete all records
delete_records(delete_all=True)
