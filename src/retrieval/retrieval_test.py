from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

print("Loading embedding model...")

embedding_model = HuggingFaceEmbeddings(

    model_name="all-MiniLM-L6-v2"
)

print("Loading ChromaDB...")

vector_db = Chroma(

    persist_directory="chroma_db",

    embedding_function=embedding_model
)

# Query

query = "patch management requirements"

print(f"\nSearching for: {query}")

# Retrieve results

results = vector_db.similarity_search(query, k=3)

print("\n===== RETRIEVED NIST RESULTS =====\n")

for i, result in enumerate(results):

    print(f"\nRESULT {i+1}\n")

    print(result.page_content[:1000])

    print("\n----------------------------------")