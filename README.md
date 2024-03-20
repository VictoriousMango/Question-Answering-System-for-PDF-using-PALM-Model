**PDF Bot**

PDF Bot is a web application designed to extract information and answer questions from PDF documents using natural language processing techniques.

**Features:**

- Upload PDF files to the system for analysis.
- Ask questions related to the content of the uploaded PDF files.
- Retrieve answers to the questions using advanced question answering techniques.
- Supports various language models for text analysis.
- Simple and intuitive web interface.

**Installation:**

To run PDF Bot on your local machine, follow these steps:

- Clone the repository to your local machine:
  git clone <repository_url>

- Navigate to the project directory:
   

- Install the required dependencies:
  pip install -r requirements.txt

- Set up the environment variables:

- Create a .env file in the root directory of the project and add the following variables:
  FLASK_SECRET_KEY=your_secret_key
  GOOGLE_API_KEY=your_google_api_key

- Replace your_secret_key and your_google_api_key with your preferred values.

- Run the application:
  python app.py

- Access the application in your web browser at http://127.0.0.1:5000

**Usage:**

Upload PDF files:

- Click on the "Choose File" button and select a PDF file to upload.
- Once the file is uploaded successfully, you will see a confirmation message.

Ask questions:

- Type your question in the input field provided.
- Click on the "Post" button to submit your question.

View answers:

After submitting the question, you will receive the answer displayed on the same page.

**Technologies Used:**

- Flask: Python web framework for building the backend.
- HTML/CSS: For designing the user interface.
- Sentence Transformers: For generating text embeddings.
- LangChain: For text processing and analysis.
- PyMuPDF: For loading and parsing PDF documents.
- text-bison-001: For text generation and question answering.
