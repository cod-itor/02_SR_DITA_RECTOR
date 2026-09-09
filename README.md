# Baseline "Chat with Documents" RAG App

This is a local Retrieval-Augmented Generation (RAG) prototype that answers questions grounded in my own IT support documents.

## How to Run the App

1. Ensure you have Python installed and the Poetry package manager.
2. Ensure you have Ollama installed and running with the required models:
   - `ollama pull llama3.2`
   - `ollama pull nomic-embed-text`
3. Install dependencies by running:
   ```bash
   poetry install
   ```
4. Build the vector database (this will read the documents in the `data/` folder and create chunks):
   ```bash
   poetry run python -m app.vector_store
   ```
5. Start chatting!
   ```bash
   poetry run python main.py
   ```

## Technical Details

- **Embedding Model:** `nomic-embed-text` (via Ollama)
- **Generation Model:** `llama3.2` (via Ollama)
- **Vector Database:** ChromaDB (Persistent local storage in the `chroma_db/` folder)

## Chunking Strategy

I used a **fixed-size character chunking strategy with overlap**. 
- **Chunk Size:** 800 characters
- **Overlap:** 120 characters

**Why?** This is a simple but effective strategy for a baseline Naive RAG system. By splitting the text into 800-character blocks, we ensure the LLM receives highly relevant context without exceeding its context window. The 120-character overlap is crucial because it prevents sentences or thoughts from being abruptly cut in half across two chunks, ensuring we don't lose the meaning at the boundary edges.
