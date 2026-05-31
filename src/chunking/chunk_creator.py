from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load extracted NIST text

with open("nist_text.txt", "r", encoding="utf-8") as file:

    text = file.read()

# Create splitter

splitter = RecursiveCharacterTextSplitter(

    chunk_size=1000,

    chunk_overlap=200
)

# Split text

chunks = splitter.split_text(text)

# Print chunk count

print(f"Total Chunks Created: {len(chunks)}")

# Save chunks

with open("chunks.txt", "w", encoding="utf-8") as file:

    for chunk in chunks:

        file.write(chunk)

        file.write("\n\n====================\n\n")