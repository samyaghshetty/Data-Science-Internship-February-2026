import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama


# PAGE TITLE

st.title("🤖 RAG Customer Support Assistant")


# LOAD PDF

loader = PyPDFLoader("data.pdf")
docs = loader.load()


# CHUNKING

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=100
)

chunks = splitter.split_documents(docs)


# EMBEDDINGS

embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)


# VECTOR DATABASE

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="db"
)

retriever = db.as_retriever(search_kwargs={"k": 3})


# LLM

llm = ChatOllama(model="mistral")


# ANSWER FUNCTION

def generate_answer(query):

    docs = retriever.invoke(query)

    context = " ".join([d.page_content for d in docs])

    prompt = f"""
You are a customer support assistant.

Answer ONLY from the context below.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    answer = response.content

    return answer


# USER INPUT

query = st.text_input("Ask your question")


# BUTTON

if st.button("Generate Answer"):

    if query:

        with st.spinner("Generating answer..."):

            answer = generate_answer(query)

            st.success("Answer Generated")

            st.write(answer)
