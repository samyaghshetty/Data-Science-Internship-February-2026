# RAG-Based Customer Support Assistant
(LangGraph + ChromaDB + Ollama + HITL)

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) based customer support assistant that:

- Processes a PDF knowledge base
- Retrieves relevant information using vector embeddings
- Generates contextual answers using an LLM
- Uses LangGraph for workflow orchestration
- Supports Human-in-the-Loop (HITL) escalation

This is not just a chatbot, but a decision-based AI system.

---

## Features

- PDF-based knowledge retrieval  
- Semantic search using embeddings  
- Context-aware response generation  
- Graph-based workflow (LangGraph)  
- Conditional routing  
- Human-in-the-Loop escalation  

---

## Architecture

User Input  
↓  
LangGraph Workflow  
↓  
Processing Node  
- Retrieval (ChromaDB)  
- LLM Generation  
↓  
Router  
↓        ↓  
Output     HITL  
↓        ↓  
Answer   Human Agent  

---

## Tech Stack

- Python  
- LangChain  
- LangGraph  
- ChromaDB  
- Ollama (Local LLM)  
- PyPDF  

---

## Project Structure

RAG_Project/
│
├── main.py
├── data.pdf
├── db/ (auto-generated)
├── requirements.txt
└── README.md

---

## How It Works

1. Load PDF document  
2. Split into chunks  
3. Convert chunks into embeddings  
4. Store embeddings in ChromaDB  
5. User asks a query  
6. Retrieve relevant chunks  
7. Generate answer using LLM  
8. Route:
   - Answer → Output  
   - Uncertain → HITL  

---

## Installation

pip install langchain langgraph chromadb pypdf langchain-community langchain-ollama

---

## Run the Project

Step 1: Start Ollama  
ollama run mistral  

Step 2: Pull embedding model  
ollama pull nomic-embed-text  

Step 3: Run application  
python main.py  

---

## Example Queries

- What is refund policy?  
- How to contact support?  
- Who is CEO? (triggers HITL)  

---

## Human-in-the-Loop (HITL)

If the system cannot find relevant context or generates an uncertain answer, it escalates to a human agent.

---

## Challenges Faced

- Model limitations with low RAM  
- Embedding compatibility issues  
- Vector database dimension mismatch  

---

## Future Improvements

- Web interface (Streamlit or React)  
- Multi-document support  
- Feedback learning loop  
- Cloud deployment  

---

## Acknowledgment

I sincerely thank Innomatics Research Labs for providing me this opportunity to work on this project and gain hands-on experience in building real-world AI systems.

---

## Author

Shetty Samyagh Vijay  
Intern – Agentic AI  

---

## Star the Project

If you like this project, consider giving it a star on GitHub.
