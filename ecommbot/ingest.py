from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def ingestdata(status):
    if status is None:
        loader = CSVLoader(file_path="C:\\Users\\Chandana\\Desktop\\E-Commerce-Chatbot1\\data\\mightymerge.io__th52bne0.csv", encoding="utf-8", csv_args={"delimiter": ","})
        documents = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        vstore = FAISS.from_documents(docs, embedding)
        vstore.save_local("faiss_index")
        return vstore
    else:
        vstore = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)

        return vstore

if __name__ == '__main__':
    vstore = ingestdata(None)
    print("✅ Ingestion complete and FAISS vector store created.")