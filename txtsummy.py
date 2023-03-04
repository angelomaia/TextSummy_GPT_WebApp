from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    # Run your algorithm on the PDF data here
    return "Processed {} pages".format(num_pages)

if __name__ == '__main__':
    app.run(debug=True)
