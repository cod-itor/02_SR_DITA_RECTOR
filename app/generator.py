import ollama
from app import config

def generate_answer(question: str, context_chunks: list[str]) -> str:
    context_text = "\n\n---\n\n".join(context_chunks)
    user_prompt = f"Here is the context to use:\n\n{context_text}\n\nQuestion: {question}"
    
    messages = [
        {"role": "system", "content": config.SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]
    
    response = ollama.chat(
        model=config.GEN_MODEL,
        messages=messages
    )
    
    return response['message']['content']
