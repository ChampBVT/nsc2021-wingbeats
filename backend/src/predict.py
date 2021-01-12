import tensorflow as tf


def import_model():
    new_model = tf.keras.models.load_model('../models/modelNew2.h5')
    new_model.summary()
