import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
import numpy as np

class MNISTModel:
    def __init__(self):
        self.model = Sequential([
            Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Conv2D(64, (3, 3), activation='relu'),
            Flatten(),
            Dense(64, activation='relu'),
            Dropout(0.5),
            Dense(10, activation='softmax')
        ])
        
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
    
    def train(self, x_train, y_train, epochs=5, batch_size=32, validation_split=0.2):
        x_train = x_train.reshape((x_train.shape[0], 28, 28, 1))
        x_train = x_train.astype('float32') / 255
        y_train = to_categorical(y_train)
        
        return self.model.fit(
            x_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split
        )
    
    def save_model(self, path):
        # 保存为TF Lite格式
        converter = tf.lite.TFLiteConverter.from_keras_model(self.model)
        tflite_model = converter.convert()
        with open(path, 'wb') as f:
            f.write(tflite_model)
    
    def predict(self, image):
        # 预处理输入图像
        image = image.reshape(1, 28, 28, 1)
        image = image.astype('float32') / 255
        
        # 预测
        prediction = self.model.predict(image)
        return np.argmax(prediction[0]) 