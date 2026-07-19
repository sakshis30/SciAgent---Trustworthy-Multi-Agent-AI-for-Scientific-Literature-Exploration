# 🤖 SciAgent

> Trustworthy Multi-Agent AI for Scientific Literature Exploration

SciAgent is a Retrieval-Augmented Generation (RAG) based scientific literature assistant that enables researchers to ask natural language questions over research papers while providing grounded answers, verification reports, and citations.

The system uses a Multi-Agent architecture with FAISS vector search and Ollama-powered Large Language Models to ensure trustworthy scientific question answering.


# Features

- Multi-Agent Architecture
- Retrieval-Augmented Generation (RAG)
- FAISS Vector Database
- Scientific PDF Parsing
- Intelligent Document Chunking
- SentenceTransformer Embeddings
- Ollama (Qwen 3)
- Answer Verification
- Evidence-based Citations
- Multiple Paper Support
- Streamlit Web Interface

# Architecture

```
                User Question
                      │
                      ▼
               Retrieval Agent
                      │
          Similar Chunks (FAISS)
                      │
                      ▼
              Reasoning Agent
                      │
                Draft Answer
                      │
                      ▼
            Verification Agent
                      │
             Confidence Report
                      │
                      ▼
             Citation Generator
                      │
                      ▼
               Streamlit UI
```

# Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Framework | Streamlit |
| Vector DB | FAISS |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| LLM | Ollama (Qwen3:8B) |
| PDF Parsing | PyMuPDF |
| Chunking | LangChain |
| Multi-Agent Design | Custom Agent Architecture |

# Folder Structure

```
SciAgent
│
├── app/
│   └── app.py
│
├── data/
│   ├── papers/
│   └── vector_store/
│
├── src/
│   ├── agents/
│   ├── core/
│   ├── parser.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store.py
│   ├── llm.py
│   ├── run_agent.py
│   ├── config.py
│   └── prompt_builder.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

# Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/SciAgent.git

cd SciAgent
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Ollama

```bash
ollama run qwen3:8b
```

Start Streamlit

```bash
streamlit run app/app.py
```


# Example Workflow

1. Upload scientific papers
2. Generate embeddings
3. Store embeddings in FAISS
4. Ask a research question
5. Retrieve relevant evidence
6. Generate an answer
7. Verify the answer
8. Display citations


# Future Improvements

- Hybrid BM25 + FAISS Retrieval
- LangGraph Workflow Orchestration
- Docker Deployment
- Kubernetes Deployment
- Evaluation Pipeline
- Web Paper Upload
- Research Gap Visualization
- Knowledge Graph Integration


# Author

**Sakshi Singh**

MSc. Computer Science Student


# License

This project is intended for educational and research purposes.
