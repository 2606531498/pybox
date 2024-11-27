import tensorflow as tf
from .model import MNISTModel
import os
import json

def train_model():
    # 加载MNIST数据集
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    
    # 创建模型实例
    model = MNISTModel()
    
    # 训练模型
    history = model.train(x_train, y_train)
    
    # 保存模型
    save_dir = os.path.join(os.path.dirname(__file__), 'saved_models')
    os.makedirs(save_dir, exist_ok=True)
    model.save_model(os.path.join(save_dir, 'mnist_model.tflite'))
    
    # 保存训练历史
    with open(os.path.join(save_dir, 'training_history.json'), 'w') as f:
        json.dump({
            'accuracy': [float(x) for x in history.history['accuracy']],
            'val_accuracy': [float(x) for x in history.history['val_accuracy']],
            'loss': [float(x) for x in history.history['loss']],
            'val_loss': [float(x) for x in history.history['val_loss']]
        }, f)

if __name__ == '__main__':
    train_model() 