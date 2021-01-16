import tensorflow as tf
import librosa
import numpy as np
import os
from src.config import MODEL, SAMPLING_RATE, UPLOAD_FOLDER, LENGTH_TARGET
import sys

model = tf.keras.models.load_model('./models/'+MODEL)


def predict(filename):
    x, sr = librosa.load(os.path.join(UPLOAD_FOLDER) + filename, sr=SAMPLING_RATE)
    predictions = []
    for i in range(0, len(x), int(LENGTH_TARGET / 2)):  # overlap .15s
        y = x[i:i + LENGTH_TARGET]
        if len(y) == LENGTH_TARGET:
            y = tf.reshape(y, (1, y.shape[0], -1))
            predictions.append(np.argmax(model.predict(y)))
    # predictions = [1,2,3,4,5,6,6,6,7,7,7,7,8,8,8,8,8,8,0,0,0,0,0,0,0]
    print(predictions, file=sys.stderr)
    return most_occurrence(predictions)


def most_occurrence(predict_list):
    mo = np.zeros(10)
    for i in predict_list:
        mo[i] = mo[i] + 1
    return int(mo.argmax()), int(mo[mo.argmax()])
