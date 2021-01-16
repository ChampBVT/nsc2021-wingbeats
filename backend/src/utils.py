from src.config import ALLOWED_EXTENSIONS, SAMPLING_RATE, LENGTH_TARGET, UPLOAD_FOLDER
import librosa
import os


def allowed_file(filename):
    return '.' in filename and get_extension(filename) in ALLOWED_EXTENSIONS


def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()


def check_length(filename):
    x, sr = librosa.load(os.path.join(UPLOAD_FOLDER) + filename, sr=SAMPLING_RATE)
    if len(x) < 2400:
        return False
    else:
        return True
