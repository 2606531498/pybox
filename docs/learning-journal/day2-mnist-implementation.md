# Day 2 - 实现手写数字识别模型

日期：2024-[MM-DD]

## 今日目标
- [x] 理解深度学习模型的基本概念
- [x] 实现MNIST手写数字识别模型
- [x] 学习TensorFlow框架基础

## 学习内容

### 1. 深度学习基础

1. **卷积神经网络(CNN)结构**
   ```python
   model = Sequential([
       # 第一个卷积层：32个3x3的卷积核
       Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
       MaxPooling2D((2, 2)),  # 最大池化层
       
       # 第二个卷积层：64个3x3的卷积核
       Conv2D(64, (3, 3), activation='relu'),
       MaxPooling2D((2, 2)),
       
       # 第三个卷积层
       Conv2D(64, (3, 3), activation='relu'),
       
       # 将特征图展平为一维向量
       Flatten(),
       
       # 全连接层
       Dense(64, activation='relu'),
       Dropout(0.5),  # 防止过拟合
       
       # 输出层：10个数字的概率
       Dense(10, activation='softmax')
   ])
   ```

2. **模型训练过程**
   - 数据预处理：
     ```python
     # 归一化图像数据
     x_train = x_train.astype('float32') / 255
     
     # 转换标签为one-hot编码
     y_train = to_categorical(y_train)
     ```
   
   - 训练参数：
     ```python
     model.compile(
         optimizer='adam',  # 优化器
         loss='categorical_crossentropy',  # 损失函数
         metrics=['accuracy']  # 评估指标
     )
     ```

### 2. 训练结果分析

观察训练过程输出：
```
Epoch 1/5
accuracy: 0.8058 - loss: 0.5859 - val_accuracy: 0.9825
Epoch 2/5
accuracy: 0.9737 - loss: 0.0931 - val_accuracy: 0.9849
Epoch 3/5
accuracy: 0.9822 - loss: 0.0636 - val_accuracy: 0.9890
Epoch 4/5
accuracy: 0.9854 - loss: 0.0504 - val_accuracy: 0.9887
Epoch 5/5
accuracy: 0.9884 - loss: 0.0396 - val_accuracy: 0.9894
```

1. **性能指标解读**
   - accuracy: 训练集准确率
   - val_accuracy: 验证集准确率
   - loss: 训练集损失值
   - val_loss: 验证集损失值

2. **训练过程分析**
   - 第一轮：模型快速学习，准确率从0提升到80%
   - 后续轮次：准确率稳步提升
   - 最终达到98.94%的验证准确率

### 3. TensorFlow基础概念

1. **张量(Tensor)**
   ```python
   # 创建张量
   import tensorflow as tf
   
   # 0维张量（标量）
   scalar = tf.constant(7)
   
   # 1维张量（向量）
   vector = tf.constant([1, 2, 3])
   
   # 2维张量（矩阵）
   matrix = tf.constant([[1, 2], [3, 4]])
   ```

2. **模型保存和加载**
   ```python
   # 保存模型
   model.save('saved_models/mnist_model.h5')
   
   # 加载模型
   loaded_model = tf.keras.models.load_model('saved_models/mnist_model.h5')
   ```

## 遇到的问题和解决方案

1. **问题：TensorFlow安装失败**
   - 原因：版本兼容性问题
   - 解决方案：
     ```bash
     pip install tensorflow==2.12.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
     ```

2. **问题：训练时内存不足**
   - 原因：批量大小设置过大
   - 解决方案：
     - 减小batch_size
     - 使用数据生成器

## 今日收获

1. 理解了CNN的基本结构和原理
2. 掌握了使用TensorFlow构建模型的方法
3. 学会了解读训练过程的各项指标
4. 理解了模型保存和加载的方法

## 明日计划

- [ ] 实现模型预测接口
- [ ] 优化模型性能
- [ ] 添加可视化功能

## 小贴士

- 训练前先小规模测试
- 定期保存模型检查点
- 注意观察验证集性能
- 使用GPU可以显著加速训练

## 学习资源

- [TensorFlow官方教程](https://tensorflow.org/tutorials)
- [CNN可视化教程](https://poloclub.github.io/cnn-explainer/)
- [MNIST数据集介绍](http://yann.lecun.com/exdb/mnist/)
- [深度学习基础](https://www.deeplearning.ai/) 