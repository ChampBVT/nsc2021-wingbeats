from flask import Flask, send_file, request
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from pathvalidate import sanitize_filename
from flask import Blueprint
import os

UPLOAD_FOLDER = './media'
ALLOWED_EXTENSIONS = ['wav']

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Blueprint('v1', __name__, url_prefix='/api/v1')


@api.route('/wav', methods=['GET'])
@cross_origin()
def get_audio():
    return send_file(os.getcwd() + '/media/test.wav')


@api.route('/mp3', methods=['GET'])
@cross_origin()
def get_audio2():
    return send_file(os.getcwd() + '/media/test2.mp3')


@api.route('/upload', methods=['POST'])
@cross_origin()
def post_audio():
    file = request.files['file']
    filename = sanitize_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    file_type = filename.split('.')[-1]
    if file_type not in ALLOWED_EXTENSIONS:
        return "Allowed File Type "+str(ALLOWED_EXTENSIONS), 400
    return file_type, 200


app.register_blueprint(api)

if __name__ == "__main__":  # port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port='8080')
