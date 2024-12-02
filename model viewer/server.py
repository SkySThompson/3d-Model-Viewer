from flask import Flask, render_template, request, redirect, url_for  
import os  
  
app = Flask(__name__)  
  
# Directory for saving uploaded models  
UPLOAD_FOLDER = 'static/models'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  
  
# Allowed file extensions  
ALLOWED_EXTENSIONS = {'gltf', 'glb'}  
  
def allowed_file(filename):  
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS  
  
# List to store uploaded files  
uploaded_files = []  
  
@app.route('/', methods=['GET', 'POST'])  
def index():  
   model_filename = None  
  
   if request.method == 'POST':  
      # Check if the post request has the file part  
      if 'file' not in request.files:  
        return redirect(request.url)  
      file = request.files['file']  
  
      if file and allowed_file(file.filename):  
        # Save the file to the 'static/models' folder  
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)  
        file.save(filename)  
        model_filename = file.filename  
        uploaded_files.append(model_filename)  # Add file to the list  
  
   return render_template('index.html', model_filename=model_filename, uploaded_files=uploaded_files)  
  
@app.route('/upload_history')  
def upload_history():  
   return render_template('upload_history.html', uploaded_files=uploaded_files)  
  
if __name__ == "__main__":  
   app.run(debug=True)