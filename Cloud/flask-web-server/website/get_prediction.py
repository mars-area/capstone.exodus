import os      # For File Manipulations like get paths, rename
from flask import Blueprint, Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

get_prediction = Blueprint('get_prediction', __name__)
app=Flask(__name__)

app.secret_key = "secret key" # for encrypting the session
#It will allow below 16MB contents only, you can change it
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 
path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path,'website', 'static', 'uploads')

if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@get_prediction.route('/get_prediction', methods=['GET', 'POST'])
def upload_file():
    filename = 'default.png'
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part', category='error')
            # return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading', category='error')
            # return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded', category='success')
            # return redirect('/')
        else:
            flash('Allowed file types are png, jpg, and jpeg', category='error')
        print('file:', file)
        print('filename:', filename)
    return render_template('predict.html', value='uploads' + '/' + filename)