import os
import shutil


RAW_DOCS_FOLDER = "data/raw_docs"


def clear_raw_docs():
    """
    Deletes all old documents before uploading new ones.
    """

    os.makedirs(RAW_DOCS_FOLDER, exist_ok=True)

    for file in os.listdir(RAW_DOCS_FOLDER):
        file_path = os.path.join(RAW_DOCS_FOLDER, file)

        if os.path.isfile(file_path):
            os.remove(file_path)


def save_uploaded_files(uploaded_files):
    """
    Saves uploaded Streamlit files into data/raw_docs.
    """

    clear_raw_docs()

    saved_files = []

    for uploaded_file in uploaded_files:

        save_path = os.path.join(
            RAW_DOCS_FOLDER,
            uploaded_file.name
        )

        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        saved_files.append(uploaded_file.name)

    return saved_files