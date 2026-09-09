import os
import glob

def load_documents(data_dir: str = "data") -> list[str]:
    documents = []
    file_paths = glob.glob(os.path.join(data_dir, "*.txt"))
    
    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as f:
            documents.append(f.read())
            
    return documents
