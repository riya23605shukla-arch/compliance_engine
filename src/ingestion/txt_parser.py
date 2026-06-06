
# the parse_text function accepts a text file path and converts the document into structured format 
import os


def parse_txt(file_path):
   
   # using with open python handles closing the file automatically

    with open(  
        file_path,
        "r",
        encoding="utf-8"          # provides proper encoding of english text, symbols and special characters
    ) as file:

        text = file.read()   # entire content of the text is  extracted and stored in variable for processing.


# return the structured  format document
# input data/raw_docs/policy.txt =output policy.txt
# original document name to understand source document
# parsers are kept consistent

    return {
        "file_name": os.path.basename(file_path),
        "pages": [
            {
                "page_number": 1,
                "text": text
            }
        ]
    }