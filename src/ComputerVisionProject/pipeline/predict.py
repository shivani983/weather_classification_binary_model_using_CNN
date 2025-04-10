import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
    
    def predict(self):
        # Load the trained model from the specified path
        model = load_model(os.path.join("artifacts/training", "model.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))  # Adjust if needed for your model's expected input size
        test_image = image.img_to_array(test_image)
        
        # Normalize the image (same preprocessing as during training)
        test_image = np.expand_dims(test_image, axis=0)  # Expand dims to simulate batch size
        test_image = test_image / 255.0  # Normalize to [0,1] if it was done during training
        
        # Predict the class
        result = model.predict(test_image)
        
        # If it's a classification model, use argmax to get the class index with the highest probability
        predicted_class_index = np.argmax(result, axis=1)[0]
        print(f"Predicted class index: {predicted_class_index}")

        # Mapping the predicted class index to class labels
        class_labels = ['cloudy', 'foggy', 'rainy', 'sunshine', 'Sunrise']  # Updated for your specific classes
        prediction = class_labels[predicted_class_index]

        return [{"image": prediction}]
