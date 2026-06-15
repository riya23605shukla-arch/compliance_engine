# Import required libraries
import json
import os
import chromadb

# import the embeddding model
from sentence_transformers import SentenceTransformer

# Load MiniLM embedding model used to generate vector embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
from src.retrieval.chroma_manager import get_collection

# connect to existing chromadb connection
collection = get_collection()

# Folder containing chunk files
CHUNKS_FOLDER = "data/chunks"

# iterate through every chunk file
for file_name in os.listdir(CHUNKS_FOLDER):

    # skip non json files
    if not file_name.endswith(".json"):
        continue
    
    #build complete file path
    file_path = os.path.join(
        CHUNKS_FOLDER,
        file_name
    )

    print(f"Processing {file_name}")

    # Load chunk JSON
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        chunks = json.load(file)

    # Store each chunk
    for chunk in chunks:

        chunk_text = chunk["text"]

        # Generate embedding
        embedding = model.encode(
            chunk_text
        ).tolist()

        # Store in ChromaDB
        collection.add(
            ids=[
                chunk["chunk_id"]
            ],

            embeddings=[
                embedding
            ],

            documents=[
                chunk_text
            ],
 # metadta used for traceability:
            metadatas=[
    {
        "chunk_id":
            chunk["chunk_id"],

        "file_name":
            chunk["file_name"],

        "page_number":
            chunk["page_number"],

        "document_type":
            "policy_document"
    }
]
        )

print("Embeddings stored successfully.")