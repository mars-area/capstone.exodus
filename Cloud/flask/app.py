import os
from flask import Flask, render_template
from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
from google.cloud import automl

# files directory
UPLOAD_FOLDER = './dummy_images'
# extension that allowed
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# defining function
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route
# Homepage
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
# homepage when user upload
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            project_id = "flask-vision"
            model_id = "ICN598914978765864960"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            prediction_client = automl.PredictionServiceClient()
            # Get the full path of the model.
            model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

            # Read the file.
            with open(file_path, "rb") as content_file:
                content = content_file.read()

            image = automl.Image(image_bytes=content)
            payload = automl.ExamplePayload(image=image)
            params = {"score_threshold": "0.8"}

            request = automl.PredictRequest(name=model_full_id, payload=payload, params=params)

            response = prediction_client.predict(request=request)
            print("Prediction results:")
            for result in response.payload:
                print("Predicted class name: {}".format(result.display_name))
                print("Predicted class score: {}".format(result.image_object_detection.score))
                bounding_box = result.image_object_detection.bounding_box
                print("Normalized Vertices:")
                for vertex in bounding_box.normalized_vertices:
                    print("\tX: {}, Y: {}".format(vertex.x, vertex.y))
    return render_template('result.html')

@app.route('/model.json', methods=['GET'])
def modeljson():
    modelname = 'model.json'
    return send_from_directory('tf_js', modelname)

@app.route('/dict.txt', methods=['GET'])
def dict():
    dicttxt = 'dict.txt'
    return send_from_directory('tf_js', dicttxt)

@app.route('/group1-shard1of1.bin', methods=['GET'])
def group():
    groupbin = 'group1-shard1of1.bin'
    return send_from_directory('tf_js', groupbin).read()

# accessing uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)