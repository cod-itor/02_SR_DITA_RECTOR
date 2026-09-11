# Homework Reflection

The process of building the offline pipeline (ingestion, chunking, and embedding) went very smoothly. Before starting the code, I made sure to do my research by carefully reviewing the slides and the video that the teacher provided. By breaking the project down into steps, it was much easier to understand how everything flowed together. Setting up ChromaDB to store the vectors and using the `nomic-embed-text` model to retrieve the correct IT support chunks worked perfectly, and the database searches were extremely fast.

The most difficult part of this assignment by far was the fact that Python is a completely new programming language for me. Writing the code for the retriever and the generator wasn't just about understanding RAG; it was about learning how to write Python. I encountered several syntax rules and programming concepts that required me to stop and do extra research just to understand what the code was doing before I could move forward.

Right now, the app uses a naive fixed-size character chunking strategy. While this works, it might accidentally split important paragraphs. To improve this app later, I could implement a "Semantic Chunking" strategy using LangChain, or use a "Re-ranking" model. A re-ranker would take the top chunks retrieved by ChromaDB and score them again for relevance before sending them to the LLM, making the final answers much more accurate.

Overall, this project was a huge learning experience. Seeing the AI successfully answer my questions based strictly on the documents I provided was incredibly rewarding. This is just the first step, and while it is definitely not easy, I am really enjoying learning about the deeper process of how AI actually works under the hood.
