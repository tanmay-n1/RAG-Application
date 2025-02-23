MODEL = "mistral:latest"
CHROMA_PATH = "chroma"
DATA_PATH = "mydocs"

from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

model = Ollama(model= MODEL)

template = """
Answer the question based on the context below. If you can't 
answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(template)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("source", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    
    return formatted_response

def chatbot():
    print("Hello! I'm your chatbot. Ask me anything.")
    
    while True:
        # Ask for user input
        user_input = input("Your question: ")
        
        # If the user wants to quit, break the loop
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye! Have a great day!")
            break
        
        # Get the answer from the query_rag function
        answer = query_rag(user_input)
        
        # Print the answer
        print(answer)
        
        # Optionally, ask the user if they want to ask another question
        print("\nFeel free to ask another question or type 'exit' to quit.\n")

if __name__ == "__main__":
    chatbot()