import os
from langchain.chains.question_answering import load_qa_chain
import google.generativeai as palm

from Vector import load_vector_storage, create_vector_storage

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":
    pdf_path = "/content/AI.pdf"  # Provide the path to your PDF file
    model_name = "all-MiniLM-L6-v2"
    
    # Uncomment the following line if you haven't created the vector storage yet
    # create_vector_storage(pdf_path, model_name)
    
    db = load_vector_storage(model_name)
    
     
    google_api_key=os.getenv('GOOGLE_API_KEY')
    palm.configure(api_key=google_api_key)

    query = "Give a short note on Artificial Intelligence vs Traditional Robotics in 50 words"
   
    completion = palm.generate_text(
    model='models/text-bison-001',
    prompt=query,
    temperature=0.1
)
print(completion.result)