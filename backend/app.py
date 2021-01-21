from flask import Flask, send_file, request
from flask_cors import CORS, cross_origin
from pathvalidate import sanitize_filename
from flask import Blueprint, jsonify
from src.utils import allowed_file, get_extension, check_length, last_modified, get_duration
from src.config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from src.predict import predict
from src.api_spec.swagger import swagger_ui_blueprint, SWAGGER_URL
from src.api_spec.spec import spec
import os
import sys

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Blueprint('v1', __name__, url_prefix='/api/v1')


@api.route('/upload', methods=['POST'])
@cross_origin()
def post_audio():
    """
    ---
    post:
      description: Uploading a selected file
      requestBody:
        content:
          multipart/form-data:
           schema:
            type: object
            properties:
              file:
                type: string
                format: binary
      responses:
        '201':
          description: File is uploaded
          content:
            application/json:
              schema: DescSchema
        '400':
          description: File not found in request [OR] Not allowed file extension detects [OR] File not meet minimum length
          content:
            application/json:
              schema: DescSchema

      tags:
          - Upload
    """
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify(description="File not found in request"), 400
    file = request.files['file']
    filename = old_filename = sanitize_filename(file.filename)
    file_ext = get_extension(filename)
    if not allowed_file(filename):
        return jsonify(description="Allowed " + str(ALLOWED_EXTENSIONS) + " received " + file_ext), 400
    # TODO
    duplicate_counts = 0
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER']) + filename):
        filename = old_filename.replace('.' + file_ext, '') + " (" + str(duplicate_counts) + ")." + file_ext
        duplicate_counts = duplicate_counts + 1
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    if not check_length(filename):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(description="The audio file should be at least 0.3 seconds"), 400
    return jsonify(description='Uploaded ' + filename), 201


@api.route('/files', methods=['POST'])
@cross_origin()
def get_files_with_offset():
    # TODO MAYBE CHANGES
    """
    ---
    post:
      description: Get files information with offset and limit on the server
      requestBody:
        content:
          application/json:
           schema: PaginationSchema
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: FilesSchema
        '400':
          description: offset not found in request body [OR] content-type is not JSON
          content:
            application/json:
              schema: DescSchema

      tags:
          - File
    """
    if not request.is_json:
        return jsonify(description='Missing JSON in request'), 400
    offset = request.json.get('offset', None)
    limit = request.json.get('limit', 10)
    if offset is None:
        return jsonify(description='Missing offset in request'), 400
    json_array = []
    files_list = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    offset_count = 0
    for file in files_list:
        # TODO
        if offset_count < offset:
            offset_count = offset_count + 1
            continue
        json_array.append(
            {
                'filename': file,
                'type': get_extension(file),
                'date': last_modified(file, '%m/%d/%Y'),
                'time': last_modified(file, '%H.%M %p'),
                'length': get_duration(file)
            }
        )
        if len(json_array) == limit:
            break
    return jsonify(files=json_array), 200


@api.route('/files', methods=['GET'])
@cross_origin()
def get_all_files():
    # TODO MAYBE CHANGES
    """
    ---
    get:
      description: Get every files information on the server
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: FilesSchema

      tags:
          - File
    """
    json_array = []
    files_list = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    for file in files_list:
        # TODO
        json_array.append(
            {
                'filename': file,
                'type': get_extension(file),
                'date': last_modified(file, '%m/%d/%Y'),
                'time': last_modified(file, '%H.%M %p'),
                'length': get_duration(file)
            }
        )
    return jsonify(files=json_array), 200


@api.route('/file/<filename>', methods=['GET'])
@cross_origin()
def get_file(filename):
    """
    ---
    get:
      description: Get a valid downloadable path of <filename> on the server
      parameters:
        - in: path
          name: filename
          required: true
      responses:
        '200':
          description: OK
          content:
            audio/x-wav:
              type: string
              format: binary
        '404':
          description: File Not Found
          content:
            application/json:
              schema: DescSchema

      tags:
          - File
    """
    filename = sanitize_filename(filename)
    files_list = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    for file in files_list:
        if file == filename:
            # TODO
            return send_file(os.path.join(app.config['UPLOAD_FOLDER']) + filename), 200
    return jsonify(description='File not found on server'), 404


@api.route('/predict/<filename>', methods=['GET'])
@cross_origin()
def predict_file(filename):
    # TODO OUTPUT RESPONSE
    """
    ---
    get:
      description: Make the server classified the specific file Ex. Ae.Aegypti_1M_5D_25C_SmallCylinder_Cut1.wav
      parameters:
        - in: path
          name: filename
          required: true
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema: PredictionSchema
        '404':
          description: File Not Found
          content:
            application/json:
              schema: DescSchema

      tags:
          - Prediction
    """
    filename = sanitize_filename(filename)
    files_list = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    for file in files_list:
        if file == filename:
            # TODO
            species_idx = predict(filename)
            return jsonify(species=species_idx), 200
            # return jsonify(species='Aedes Albopictus', gender='M', probability='70%'), 200
    return jsonify(description='File not found on server'), 404


app.register_blueprint(api)

with app.test_request_context():
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)


@app.route("/api/swagger.json")
def create_swagger_spec():
    """
    Swagger API definition.
    """
    return jsonify(spec.to_dict())


app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port='8080')
