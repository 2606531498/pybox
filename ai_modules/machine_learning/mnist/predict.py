import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

class MNISTPredictor:
    def __init__(self):
        model_path = os.path.join(
            os.path.dirname(__file__),
            'saved_models',
            'mnist_model'
        )
        self.model = tf.keras.models.load_model(model_path)
    
    def predict(self, image_data):
        try:
            # 预处理图像
            image = Image.open(io.BytesIO(image_data)).convert('L')
            image = image.resize((28, 28))
            image = np.array(image)
            image = image.reshape(1, 28, 28, 1)
            image = image.astype('float32') / 255
            
            # 运行推理
            predictions = self.model.predict(image)
            digit = np.argmax(predictions[0])
            confidence = float(predictions[0][digit])
            
            return {
                'digit': int(digit),
                'confidence': confidence
            }
        except Exception as e:
            print(f"预测错误: {str(e)}")
            raise