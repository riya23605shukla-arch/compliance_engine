# this converts large policy documents into smaller chunks 
# this function contains parsed document chunks 
#  maximum 700 words per chunk , last 100 chunks from previous chunk will be repeated in the next chunk
# embedding model works better on smaller sections that is why creating chunks in needed

def generate_chunks(
        parsed_document,
        chunk_size=700,
        overlap=100):

    chunks = [] # created an empty chunk

    for page in parsed_document["pages"]:

        words = page["text"].split() # convert text into list of words

        start = 0

        chunk_number = 1

        while start < len(words):  # keep generating chunks untill all words are processed

            end = start + chunk_size
       

         # converts the word list back into readable text 
            chunk_text = " ".join(
                words[start:end]
            )

            # creates metadata that is the structured format

            chunk = {

                "chunk_id":
                f"{parsed_document['file_name']}_p{page['page_number']}_c{chunk_number}",

                "file_name":
                parsed_document["file_name"],

                "page_number":
                page["page_number"],

                "text":
                chunk_text,         # stores actual content

                "token_count":
                len(chunk_text.split())
            }
          
          # stores the chunk into chunk list
            chunks.append(chunk)
          
          # move window forward that means seperating the size as nchunk size - overlapped part
            start += (
                chunk_size - overlap
            )

            chunk_number += 1

    return chunks