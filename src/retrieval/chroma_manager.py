# Handles all ChromaDB operations

import chromadb

# location of persistent vector database
DB_PATH = "data/chroma_db"

#collection containing policy document chunks
COLLECTION_NAME = "policy_chunks"


def get_collection():
   
   # cretae or connect to chromaDB
    client = chromadb.PersistentClient(
        path=DB_PATH
    )
    # load collection if it exists
    # otherwise create a new one
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection