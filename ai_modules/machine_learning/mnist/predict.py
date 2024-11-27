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
            'mnist_model.tflite'
        )
        # 加载TF Lite模型
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        # 获取输入输出细节
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    
    def predict(self, image_data):
        try:
            # 预处理图像
            image = Image.open(io.BytesIO(image_data)).convert('L')
            image = image.resize((28, 28))
            image = np.array(image)
            image = image.reshape(1, 28, 28, 1)
            image = image.astype('float32') / 255
            
            # 设置输入张量
            self.interpreter.set_tensor(self.input_details[0]['index'], image)
            
            # 运行推理
            self.interpreter.invoke()
            
            # 获取输出张量
            output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
            
            # 处理结果
            digit = np.argmax(output_data[0])
            confidence = float(output_data[0][digit])
            
            return {
                'digit': int(digit),
                'confidence': confidence
            }
        except Exception as e:
            print(f"预测错误: {str(e)}")
            raise 