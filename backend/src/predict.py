def import_model():
    import tensorflow as tf
    new_model = tf.keras.models.load_model('./models/modelNew2.h5')
    print(new_model.summary())
