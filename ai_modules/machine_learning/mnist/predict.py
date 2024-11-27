import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
from .model import MNISTModel

class MNISTPredictor:
    def __init__(self):
        model_path = os.path.join(
            os.path.dirname(__file__),
            'saved_models',
            'mnist_model.h5'
        )
        self.model = tf.keras.models.load_model(model_path)
    
    def predict(self, image_data):
        try:
            # 将二进制图像数据转换为PIL图像
            image = Image.open(io.BytesIO(image_data)).convert('L')
            
            # 调整图像大小为28x28
            image = image.resize((28, 28))
            
            # 转换为numpy数组
            image = np.array(image)
            
            # 预处理图像
            image = image.reshape(1, 28, 28, 1)
            image = image.astype('float32') / 255
            
            # 预测
            prediction = self.model.predict(image)
            digit = np.argmax(prediction[0])
            confidence = float(prediction[0][digit])
            
            return {
                'digit': int(digit),
                'confidence': confidence
            }
        except Exception as e:
            print(f"预测错误: {str(e)}")
            raise 