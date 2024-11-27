# AI学习平台安装指南

## 环境要求
- Python 3.9+
- Git
- 虚拟环境工具(venv)

## 安装步骤

### 1. 克隆项目
```bash
git clone [项目地址]
cd ai-learning-platform
```

### 2. 创建虚拟环境
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖
```bash
# 更新pip
python -m pip install --upgrade pip

# 安装依赖
pip install -r requirements.txt
```

### 4. 配置环境变量
创建 `.env` 文件：
```text
FLASK_APP=website/app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
```

### 5. 训练模型
```bash
# 创建模型保存目录
mkdir -p ai_modules/machine_learning/mnist/saved_models

# 运行训练脚本
python ai_modules/machine_learning/mnist/train.py
```

### 6. 运行应用
```bash
python website/app.py
```
访问 http://127.0.0.1:5000 查看网站

## 常见问题解决

### 1. 依赖安装失败
```bash
# 使用国内镜像源安装
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2. TensorFlow安装问题
- Windows用户推荐使用CPU版本
- 确保Python版本兼容（推荐3.9-3.11）

### 3. 模型训练错误
- 确保有足够的磁盘空间
- 检查MNIST数据集下载是否完整
- 验证TensorFlow安装是否正确

### 4. 运行时错误
- 确保虚拟环境已激活
- 检查所有依赖是否安装完整
- 验证模型文件是否存在