# AI学习平台开发指南

## 项目概述

本项目是一个AI学习平台，集成了多个AI项目实例，首个实现的是MNIST手写数字识别项目。

## 技术栈

### 后端
- Python 3.9+
- Flask 3.0.0
- TensorFlow 2.12.0
- NumPy 1.24.3

### 前端
- HTML5
- CSS3
- JavaScript (原生)

## 项目结构
```
ai-learning-platform/
├── website/                 # 网站前端代码
│   ├── static/             # 静态文件
│   │   ├── css/           # 样式文件
│   │   │   ├── style.css  # 全局样式
│   │   │   └── mnist.css  # MNIST项目样式
│   │   ├── js/            # JavaScript文件
│   │   │   ├── main.js    # 全局脚本
│   │   │   └── mnist.js   # MNIST项目脚本
│   │   └── images/        # 图片资源
│   ├── templates/         # HTML模板
│   │   ├── base.html     # 基础模板
│   │   ├── index.html    # 首页
│   │   └── projects/     # 项目页面
│   │       └── mnist.html # MNIST项目页面
│   └── app.py            # Flask应用主文件
└── ai_modules/            # AI项目代码
    └── machine_learning/
        └── mnist/        # MNIST项目
            ├── model.py  # 模型定义
            ├── train.py  # 训练脚本
            └── predict.py # 预测接口
```

## 开发环境设置

### 1. 环境准备
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置文件
创建 `.env` 文件：
```
FLASK_APP=website/app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
```

## API接口文档

### MNIST手写数字识别

#### 预测接口
- **URL**: `/api/mnist/predict`
- **方法**: POST
- **请求格式**: multipart/form-data
- **参数**:
  - `image`: 图片文件（PNG格式）
- **响应格式**: JSON
```json
{
    "digit": 5,          // 识别的数字
    "confidence": 0.98   // 置信度
}
```
- **错误响应**:
```json
{
    "error": "错误信息"
}
```

## 前端开发指南

### 1. 页面模板
使用Jinja2模板引擎，所有页面继承自 `base.html`：
```html
{% extends "base.html" %}

{% block title %}页面标题{% endblock %}

{% block content %}
    <!-- 页面内容 -->
{% endblock %}
```

### 2. 静态资源
- CSS文件放在 `static/css/` 目录
- JavaScript文件放在 `static/js/` 目录
- 在模板中引用：
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
<script src="{{ url_for('static', filename='js/main.js') }}"></script>
```

### 3. JavaScript开发规范
- 使用ES6+语法
- 模块化组织代码
- 使用async/await处理异步操作
- 添加适当的错误处理

## AI模型开发指南

### 1. 模型结构
```python
model = Sequential([
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
```

### 2. 训练过程
```python
# 数据预处理
x_train = x_train.astype('float32') / 255
y_train = to_categorical(y_train)

# 训练参数
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 训练
history = model.fit(
    x_train, y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.2
)
```

### 3. 模型保存和加载
```python
# 保存模型
model.save('saved_models/mnist_model.h5')

# 加载模型
loaded_model = tf.keras.models.load_model('saved_models/mnist_model.h5')
```

## 部署指南

### 1. 准备工作
- 确保所有依赖已安装
- 检查模型文件是否存在
- 配置环境变量

### 2. 运行应用
```bash
# 开发环境
python website/app.py

# 生产环境（使用gunicorn）
gunicorn -w 4 -b 0.0.0.0:5000 website.app:app
```

## 测试指南

### 1. 单元测试
```bash
# 运行所有测试
python -m pytest tests/

# 运行特定测试
python -m pytest tests/test_mnist.py
```

### 2. API测试
使用Postman或curl测试API：
```bash
curl -X POST -F "image=@test.png" http://localhost:5000/api/mnist/predict
```

## 常见问题解决

### 1. 模型加载错误
- 检查模型文件路径
- 确认TensorFlow版本匹配
- 验证模型文件完整性

### 2. 图像处理问题
- 确保图像格式正确
- 检查图像预处理步骤
- 验证图像大小调整

## 代码风格指南

### Python代码规范
- 遵循PEP 8规范
- 使用类型注解
- 添加适当的文档字符串
- 使用pylint进行代码检查

### JavaScript代码规范
- 使用ESLint
- 遵循Airbnb风格指南
- 使用适当的注释
- 处理所有可能的错误

## 版本控制

### Git工作流
1. 创建功能分支
```bash
git checkout -b feature/new-feature
```

2. 提交代码
```bash
git add .
git commit -m "feat: add new feature"
```

3. 合并到主分支
```bash
git checkout main
git merge feature/new-feature
```

## 学习资源

- [Flask文档](https://flask.palletsprojects.com/)
- [TensorFlow教程](https://tensorflow.org/tutorials)
- [MDN Web文档](https://developer.mozilla.org/)
- [Git教程](https://git-scm.com/book/zh/v2) 