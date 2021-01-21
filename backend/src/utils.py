from src.config import ALLOWED_EXTENSIONS, SAMPLING_RATE, LENGTH_TARGET, UPLOAD_FOLDER, TIME_ZONE
from datetime import datetime
from pytz import timezone
import librosa
import os
import sys

bangkok = timezone(TIME_ZONE)


def allowed_file(filename):
    return '.' in filename and get_extension(filename) in ALLOWED_EXTENSIONS


def get_extension(filename):
    return filename.rsplit('.', 1)[1].lower()


def check_length(filename):
    x, sr = librosa.load(os.path.join(UPLOAD_FOLDER) + filename, sr=SAMPLING_RATE)
    if len(x) < LENGTH_TARGET:
        return False
    else:
        return True


def last_modified(filename, time_format):
    stat = os.stat(os.path.join(UPLOAD_FOLDER) + filename)
    modified_date = datetime.fromtimestamp(stat.st_mtime, tz=bangkok)
    return modified_date.strftime(time_format)


def get_duration(filename):
    duration = librosa.get_duration(filename=os.path.join(UPLOAD_FOLDER) + filename)
    if duration > 60:
        return to_minutes(duration)
    else:
        return '{:.2f}'.format(duration) + ' seconds'


def to_minutes(seconds):
    seconds = seconds % (24 * 3600)
    minutes = seconds // 60
    seconds %= 60

    return '%02d:%02d' % (minutes, seconds) + ' minutes'
