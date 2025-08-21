import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Embedding model
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# Vector DB location
db_location = "./chroma_unicef_db"
add_documents = not os.path.exists(db_location)

documents = []
ids = []

if add_documents:
    pdf_folder = "./data/pdf"
    if os.path.exists(pdf_folder):
        for file in os.listdir(pdf_folder):
            if file.endswith(".pdf"):
                file_path = os.path.join(pdf_folder, file)
                loader = PyPDFLoader(file_path)
                pdf_docs = loader.load()

                # Split PDFs into chunks
                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000, chunk_overlap=200
                )
                split_docs = splitter.split_documents(pdf_docs)

                for j, doc in enumerate(split_docs):
                    doc.metadata["source"] = file
                    documents.append(doc)
                    ids.append(f"{file}-{j}")

# Create Chroma vector store
vector_store = Chroma(
    collection_name="unicef_eof_docs",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add documents if needed
if add_documents and documents:
    vector_store.add_documents(documents=documents, ids=ids)

# Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 5})

print(f"Vector store ready with documents." if add_documents else "Vector store loaded from disk.")
