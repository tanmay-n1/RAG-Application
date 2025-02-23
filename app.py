from flask import Flask, render_template, request, jsonify
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

app = Flask(__name__)

MODEL = "mistral:latest"
CHROMA_PATH = "chroma"

template = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""

def query_rag(query_text: str):
    """Handles the query to the RAG model and retrieves an answer."""
    embedding_function = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_score(query_text, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    prompt_template = ChatPromptTemplate.from_template(template)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model=MODEL)
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("source", "Unknown") for doc, _score in results]
    
    return {"response": response_text, "sources": sources}

@app.route("/")
def home():
    """Renders the chatbot UI."""
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    """Handles chatbot queries."""
    data = request.json
    user_query = data.get("question", "")

    if not user_query:
        return jsonify({"error": "Empty question"}), 400

    response_data = query_rag(user_query)
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
