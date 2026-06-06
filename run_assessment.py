
# it reads the policy documents from the raw documents folder selects appropriate parser based on the file type 
#  # cleans the extracted text , generates metadata chunks  stores outputs as json files and creates a processing summary report
# summary report contains document ,page 

import os
import json

# import the custom modules 

from src.ingestion.pdf_parser import parse_pdf
from src.ingestion.docx_parser import parse_docx
from src.ingestion.txt_parser import parse_txt
from src.ingestion.cleaner import clean_text

from src.chunking.chunk_generator import generate_chunks


RAW_FOLDER = "data/raw_docs"
PARSED_FOLDER = "data/parsed_docs"
CHUNKS_FOLDER = "data/chunks"


os.makedirs(PARSED_FOLDER, exist_ok=True)
os.makedirs(CHUNKS_FOLDER, exist_ok=True)

 # these are the statistics folder
total_documents = 0
total_pages = 0
total_chunks = 0

summary_documents = []

# reads every document
# builds full file path
for filename in os.listdir(RAW_FOLDER):

    file_path = os.path.join(
        RAW_FOLDER,
        filename
    )

    print(f"\nProcessing: {filename}")

    # choose the parser

    if filename.endswith(".pdf"):

        parsed_doc = parse_pdf(file_path)

    elif filename.endswith(".docx"):

        parsed_doc = parse_docx(file_path)

    elif filename.endswith(".txt"):

        parsed_doc = parse_txt(file_path)

    else:

        print("Unsupported file format")
        continue

    # Clean every page

    for page in parsed_doc["pages"]:

        page["text"] = clean_text(
            page["text"]
        )

    # It saves the parsed document

    parsed_output_path = os.path.join(
        PARSED_FOLDER,
        filename.replace(".pdf", ".json")
                .replace(".docx", ".json")
                .replace(".txt", ".json")
    )

    with open(
        parsed_output_path,
        "w",
        encoding="utf-8"
    ) as file:
     
    # json.dump() is used to save python data into a json file
    # json.dump() writes directly to a file 
    #json.dumps() returns json as a string
    
        json.dump(
            parsed_doc,
            file,
            indent=4
        )

# It  Generates chunks

    chunks = generate_chunks(parsed_doc)

# save all the previously created chunks

    chunk_output_path = os.path.join(
        CHUNKS_FOLDER,
        filename.replace(".pdf", "_chunks.json")
                .replace(".docx", "_chunks.json")
                .replace(".txt", "_chunks.json")
    )

    with open(
        chunk_output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            chunks,
            file,
            indent=4
        )

    total_documents += 1
    total_pages += len(parsed_doc["pages"])
    total_chunks += len(chunks)

    summary_documents.append(
        {
            "file": filename,
            "pages": len(parsed_doc["pages"]),
            "chunks": len(chunks)
        }
    )

 # it helps to store the document summary and then save the summary
summary = {

    "total_documents":
    total_documents,

    "total_pages":
    total_pages,

    "total_chunks":
    total_chunks,

    "average_chunk_size":
    700,

    "documents":
    summary_documents
}

with open(
    "data/outputs/processing_summary.json",
    "w"
) as file:

    json.dump(
        summary,
        file,
        indent=4
    )

print("\nProcessing Completed Successfully")