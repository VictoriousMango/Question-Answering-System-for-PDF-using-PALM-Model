import os
from langchain.chains.question_answering import load_qa_chain
import google.generativeai as palm
from Vector import load_vector_storage, create_vector_storage

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

def answer_question(db, question):
    # Load vector storage
    model_name = "all-MiniLM-L6-v2"
    db = load_vector_storage(model_name)
    
    # Configure Google API
    google_api_key = os.getenv('GOOGLE_API_KEY')
    palm.configure(api_key=google_api_key)

    # Define the query
    query = question
   
    # Integrate retriever
    retriever = db.as_retriever()
    try:
        docs = retriever.invoke(query)
        if docs:
            print("Documents retrieved successfully")
        else:
            print("No documents retrieved for the query.")
    except Exception as e:
        print("Error occurred while retrieving documents:", e)

    # Generate the answer
    completion = palm.generate_text(
        model='models/text-bison-001',
        prompt=query,
        temperature=0.1
    )
    
    return completion.result
