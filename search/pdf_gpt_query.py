import os
import sys

from langchain import FAISS, OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings


def check_openai_api_key():
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        sys.exit("Error: OPENAI_API_KEY environment variable not found. Please set the OPENAI_API_KEY env variable to "
                 "the API key and try again.")


def load_pdfs(directory):
    pdf_files = []

    # Get all files and directories within the given directory
    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.lower().endswith('.pdf'):
            pdf_files.append(entry.path)
        elif entry.is_dir():
            pdf_files.extend(load_pdfs(entry.path))  # Recursively explore subdirectories

    return pdf_files


def process_files(directory):
    embeddings = OpenAIEmbeddings()
    pages = []
    for file in load_pdfs(directory):
        print(f"[Processing]: {file}")
        loader = PyPDFLoader(file)
        p = loader.load_and_split()
        pages.append(p)

    vector_db = FAISS.from_documents(pages[0], embeddings)
    for page in pages[1:]:
        if len(page) == 0:
            continue
        d = FAISS.from_documents(page, embeddings)
        vector_db.merge_from(d)

    return vector_db


def search(directory):
    check_openai_api_key()
    vector_db = process_files(directory)
    qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0), vector_db.as_retriever())
    history = []
    while True:
        question = input("input (type 'q' to exit): ")
        if question.lower() == "q":
            break

        result = qa({"question": question, "chat_history": history})
        answer = result['answer']
        history.append((question, answer))
        print(result['answer'])
