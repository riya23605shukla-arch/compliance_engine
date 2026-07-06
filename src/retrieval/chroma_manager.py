import os
import chromadb

# ==========================================
# Project Root
# ==========================================

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        ".."
    )
)

# ==========================================
# Absolute ChromaDB Path
# ==========================================

DB_PATH = os.path.join(
    BASE_DIR,
    "data",
    "chroma_db"
)

COLLECTION_NAME = "policy_chunks"

# ==========================================
# Connect to ChromaDB
# ==========================================

def get_collection():

    client = chromadb.PersistentClient(
        path=DB_PATH
    )

    collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)

    return collection