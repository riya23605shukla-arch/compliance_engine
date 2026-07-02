from src.services.retrieval_service import retrieve_control_evidence

chunks = retrieve_control_evidence(
    "PR.AA-01"
)

print()

print("Retrieved Chunks:", len(chunks))

print()

for chunk in chunks:

    print(chunk["chunk_id"])

    print(chunk["text"][:200])

    print()