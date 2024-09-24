from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
import os
import tensorflow as tf

# hide warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def create_image_generator():
    IMG_HEIGHT = 200
    IMG_WIDTH = 500
    BATCH_SIZE = 16

    # Normalize images and add the custom preprocessing function
    image_generator = ImageDataGenerator(
        rescale=1.0/255,
    )
    
    image_generator = image_generator.flow_from_directory(
        '.',
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        classes=['temp'],   # kinda hacky, but this is the recommended way to use the generator on new data
        color_mode='grayscale', 
    )
    
    return image_generator

def predict(model='multiclass_cnn_UPDATED_ARCHITECTURE4.keras'):
    print("Calculating CNN predictions...")
    model_path = os.path.join('data', 'models', model)
    cnn_model = load_model(model_path, compile=False)
    
    return cnn_model.predict(create_image_generator(), verbose=1)