
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
import os

def create_image_generator():
    path_images = os.path.join('temp')

    IMG_HEIGHT = 200
    IMG_WIDTH = 500
    BATCH_SIZE = 32

    # Normalize images and add the custom preprocessing function
    image_generator = ImageDataGenerator(
        rescale=1.0/255,
    )
    
    image_generator = image_generator.flow_from_directory(
        path_images,
        target_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        color_mode='grayscale'
    )
    
    return image_generator

def predict(model='multiclass_cnn_UPDATED_ARCHITECTURE3.keras'):
    model_path = os.path.join('..', 'data', 'models', model)
    cnn_model = load_model(model_path)
    
    return cnn_model.predict_proba(create_image_generator())
