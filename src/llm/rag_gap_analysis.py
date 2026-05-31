from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import ollama

print("Loading embedding model...")

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

print("Loading ChromaDB...")

vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

# Load policy

with open("policies/sample_policy.txt", "r", encoding="utf-8") as file:

    policy = file.read()

print("\n================ POLICY ================\n")

print(policy)

# Retrieve relevant NIST context

query = policy

print("\nRetrieving relevant NIST controls...\n")

results = vector_db.similarity_search(query, k=1)

nist_context = ""

for result in results:

    nist_context += result.page_content + "\n\n"

print("\n================ RETRIEVED NIST CONTEXT ================\n")

print(nist_context[:1000])

# AI Prompt

prompt = f"""
You are a cybersecurity auditor.

Analyze the policy using the NIST context.

Identify:
- missing controls
- compliance gaps
- weak areas

Provide:
- recommendations
- short implementation roadmap

POLICY:
{policy}

NIST:
{nist_context[:1000]}
"""

print("\nGenerating AI Gap Analysis...\n")

response = ollama.chat(
    model="tinyllama",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n================ AI GAP ANALYSIS ================\n")

print(response['message']['content'])