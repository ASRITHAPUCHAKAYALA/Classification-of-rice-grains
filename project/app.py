from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Ensure static folder exists
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Details Page
@app.route('/details')
def details():
    return render_template('details.html')

# Predict Page (handles both GET & POST)
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part in request"
        file = request.files['file']
        if file.filename == '':
            return "No file selected"
        
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Dummy prediction logic (replace with your model)
        predicted_class = "Basmati"  # Example output

        return render_template('result.html', prediction=predicted_class, image_path=file_path)
    
    # For GET request, show the upload form
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
