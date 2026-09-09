from app.embeddings import get_embedding
from app.vector_store import get_collection

def test_search(question: str):
    question_vector = get_embedding(question)
    collection = get_collection()
    
    results = collection.query(
        query_embeddings=[question_vector],
        n_results=3
    )
    
    documents = results['documents'][0]
    
    print(f"Question: {question}\n")
    print("Top 3 Matching Chunks:")
    for i, doc in enumerate(documents):
        print(f"\nResult {i+1}:")
        print(doc)

if __name__ == "__main__":
    test_search("How do I configure my email on an Android device?")
