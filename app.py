import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename
import os
from Vector import load_vector_storage
from QA import answer_question


app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set the secret key from the environment variable
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Define the directory to store uploaded PDF files
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Function to check if a filename has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('upload_success.html')

@app.route('/ask_question', methods=['POST'])
def ask_question():
    if request.method == 'POST':
        question = request.form['question']
        model_name = "all-MiniLM-L6-v2"
        db = load_vector_storage(model_name)
        answer = answer_question(db, question)
        return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
