from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

from langchain_text_splitters import RecursiveCharacterTextSplitter

print("Loading NIST text...")

# Load extracted text

with open("nist_text.txt", "r", encoding="utf-8") as file:

    text = file.read()

print("Splitting text into chunks...")

# Create chunks

splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=200
)

chunks = splitter.split_text(text)

print(f"Total chunks: {len(chunks)}")

print("Loading embedding model...")

# Load embedding model

embedding_model = HuggingFaceEmbeddings(

    model_name="all-MiniLM-L6-v2"
)

print("Creating ChromaDB vector database...")

# Create vector database

vector_db = Chroma.from_texts(

    texts=chunks,

    embedding=embedding_model,

    persist_directory="chroma_db"
)

print("Saving vector database...")

vector_db.persist()

print("Vector Database Created Successfully")