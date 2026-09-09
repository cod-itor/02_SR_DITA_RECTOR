from app.pipeline import run_rag_pipeline

def chat_loop():
    print("==================================================")
    print("Welcome to your RAG 'Chat with Documents' App!")
    print("==================================================\n")
    while True:
        question = input("==> : ")
        
        if question.strip().lower() == 'exit':
            break
            
        if not question.strip():
            continue
            
        try:
            answer = run_rag_pipeline(question)
            print(f"\nAnswer:\n{answer}\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_loop()
