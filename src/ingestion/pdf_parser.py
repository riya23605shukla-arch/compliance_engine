# the purpose of this file is to extract text from pdf documents by mentioning the page nos
# first open the pdf file then read each page and  then extract the text and store the page no and the text
# fitz is the PuMuPdf library which is use to read pdf files
# os helps us to work with file nme and paths

import fitz
import os


def parse_pdf(file_path):

    # parse a pdf document and preserve page information 
    # file_path=path to pdf file
    # dict=parsed document structure
   

    doc = fitz.open(file_path)
   
   # creates an empyty list which will store page information here
    pages = []
    for page_num in range(len(doc)): # loops through very page

        page = doc[page_num]

        text = page.get_text()  # extracts all readable text from the page

     # stores page number and text
        pages.append(
            {
                "page_number": page_num + 1,  
                "text": text
            }
        )
    
    # returns the final parsed document
    return {
        "file_name": os.path.basename(file_path),
        "pages": pages
    }