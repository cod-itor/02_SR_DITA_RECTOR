from app.retriever import retrieve_chunks
from app.generator import generate_answer

def run_rag_pipeline(question: str) -> str:
    chunks = retrieve_chunks(question)
    
    print("\n[Retrieved Context]")
    for i, chunk in enumerate(chunks):
        preview = chunk[:80].replace('\n', ' ')
        print(f"  {i+1}: {preview}...")
        
    answer = generate_answer(question, chunks)
    return answer
