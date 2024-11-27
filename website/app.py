import os
import sys
# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from ai_modules.machine_learning.mnist.predict import MNISTPredictor

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# 初始化预测器
mnist_predictor = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects/mnist')
def mnist_page():
    return render_template('projects/mnist.html')

@app.route('/api/mnist/predict', methods=['POST'])
def predict_digit():
    global mnist_predictor
    
    if 'image' not in request.files:
        return jsonify({'error': '没有上传图片'}), 400
        
    try:
        if mnist_predictor is None:
            mnist_predictor = MNISTPredictor()
            
        image_file = request.files['image']
        image_data = image_file.read()
        result = mnist_predictor.predict(image_data)
        return jsonify(result)
    except Exception as e:
        print(f"API error: {str(e)}")  # 添加错误日志
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 