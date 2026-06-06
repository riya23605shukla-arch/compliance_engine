
#imports the python document library
# open docs files and read paragraphs and extracts the text

from docx import Document
import os

# parse_docx function accepts the docx file path
# python can access paragraph , headings and text content

def parse_docx(file_path):

    doc = Document(file_path)

# the paragraphs are combined in the list but kept seperated 
    text = "\n".join(
        para.text
        for para in doc.paragraphs
    )

    return {
        "file_name": os.path.basename(file_path),
        "pages": [
            {
                "page_number": 1,
                "text": text
            }
        ]
    }