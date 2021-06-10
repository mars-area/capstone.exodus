from google.cloud import automl

# TODO(developer): Uncomment and set the following variables
project_id = "flask-vision"
model_id = "ICN4502515508905508864"
file_path = ".\dummy_images\Apple dee04161.png"

prediction_client = automl.PredictionServiceClient()

# Get the full path of the model.
model_full_id = automl.AutoMlClient.model_path(project_id, "us-central1", model_id)

# Read the file.
with open(file_path, "rb") as content_file:
    content = content_file.read()

image = automl.Image(image_bytes=content)
payload = automl.ExamplePayload(image=image)

# params is additional domain-specific parameters.
# score_threshold is used to filter the result
# https://cloud.google.com/automl/docs/reference/rpc/google.cloud.automl.v1#predictrequest
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