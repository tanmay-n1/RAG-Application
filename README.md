# AI-Powered PDF Chatbot with Local LLMs, LangChain, and ChromaDB

## Overview
This project is an AI-powered chatbot designed to enable users to interact with their PDFs intelligently. Instead of merely searching for keywords, the chatbot understands document content, allowing users to ask complex questions and receive precise, context-aware responses. The entire process runs locally without requiring an internet connection, ensuring privacy and efficiency.

## How It Works
1. **PDF Processing & Storage**: Before interacting with the chatbot, PDFs must first be processed and stored in the vector database. This step involves breaking the document into smaller chunks and embedding them in ChromaDB.
2. **Vector Storage in ChromaDB**: The document chunks are embedded and stored in ChromaDB, enabling fast retrieval of relevant content.
3. **Retrieval & Query Handling**: When a user asks a question, the system retrieves the top 4 most relevant chunks and forwards them to a local LLM (Ollama).
4. **Response Generation with RAG**: Using retrieval-augmented generation (RAG), the model generates an accurate and context-aware response based on the retrieved data.
5. **Private & Offline Execution**: The chatbot operates entirely on-device, ensuring secure and fast document intelligence without external API calls or cloud dependencies.

## Features
- **Intelligent Document Search**: Retrieves meaningful answers rather than just matching keywords.
- **Fast & Efficient**: Uses ChromaDB for quick vector-based searches.
- **Local Execution**: No internet required; runs fully on-device.
- **Command-Line Interaction**: Chatbot interacts with the stored vector database via CLI.

## Tech Stack
### Backend:
- Python
- LangChain
- Ollama (LLM)
- ChromaDB (Vector Database)

### Frontend:
- HTML
- CSS
- JavaScript

## Why Use Local LLMs?
- **Privacy**: No data leaves your machine.
- **Speed**: No API latency.
- **Cost-Efficient**: No subscription or API costs.
- **Full Control**: Customize models and responses as needed.

## Contributing
Feel free to contribute! Fork the repo, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License.

