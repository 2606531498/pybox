from flask import Flask, request, jsonify, send_from_directory
import os
import sys

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)

# 静态文件路由
@app.route('/')
def serve_static():
    return send_from_directory('../website/templates', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    if path.startswith('static/'):
        return send_from_directory('../website', path)
    return send_from_directory('../website/templates', path)

# API路由
@app.route('/api/mnist/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': '没有上传图片'}), 400
    
    try:
        from ai_modules.machine_learning.mnist.predict import MNISTPredictor
        predictor = MNISTPredictor()
        image_file = request.files['image']
        image_data = image_file.read()
        result = predictor.predict(image_data)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Vercel需要这个handler
def handler(request, context):
    return app(request, context) 