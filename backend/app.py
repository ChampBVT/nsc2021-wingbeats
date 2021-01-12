from flask import Flask, send_file, request
from flask_cors import CORS, cross_origin
from pathvalidate import sanitize_filename
from flask import Blueprint, jsonify
from src.utils import allowed_file, get_extension
from src.config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from src.predict import import_model
import os

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Blueprint('v1', __name__, url_prefix='/api/v1')


@api.route('/upload', methods=['POST'])
@cross_origin()
def post_audio():
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify(description="File not found in request"), 400
    file = request.files['file']
    filename = old_filename = sanitize_filename(file.filename)
    file_ext = get_extension(filename)
    if not allowed_file(filename):
        return jsonify(description="Allowed " + str(ALLOWED_EXTENSIONS) + " received " + file_ext), 400
    # TODO
    duplicate_counts = 0
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER']) + '/' + filename):
        filename = old_filename.replace('.' + file_ext, '') + " (" + str(duplicate_counts) + ")." + file_ext
        duplicate_counts = duplicate_counts + 1
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return jsonify(description='Uploaded ' + filename), 201


@api.route('/files', methods=['GET'])
@cross_origin()
def get_all_files():
    json_array = []
    files_list = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    for file in files_list:
        # TODO
        json_array.append({'filename': file, 'type': file.split('.')[-1]})
    return jsonify(files=json_array), 200


@api.route('/file/<filename>', methods=['GET'])
@cross_origin()
def get_file(filename):
    filename = sanitize_filename(filename)
    files_list = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    for file in files_list:
        if file == filename:
            # TODO
            return send_file(os.path.join(app.config['UPLOAD_FOLDER']) + '/' + filename), 200
    return jsonify(description='File not found on server'), 400


@api.route('/predict/<filename>', methods=['GET'])
@cross_origin()
def predict_file(filename):
    filename = sanitize_filename(filename)
    files_list = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    for file in files_list:
        if file == filename:
            # TODO
            import_model()
            return jsonify(species='Aedes Albopictus', gender='M', probability='70%'), 200
    import_model()
    return jsonify(description='File not found on server'), 400


app.register_blueprint(api)

if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port='8080')
