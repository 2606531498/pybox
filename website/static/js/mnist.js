class DrawingCanvas {
    constructor() {
        this.canvas = document.getElementById('drawingCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.isDrawing = false;
        this.setupCanvas();
        this.setupEventListeners();
    }
    
    setupCanvas() {
        this.ctx.fillStyle = 'white';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
        this.ctx.strokeStyle = 'black';
        this.ctx.lineWidth = 15;
        this.ctx.lineCap = 'round';
    }
    
    setupEventListeners() {
        this.canvas.addEventListener('mousedown', this.startDrawing.bind(this));
        this.canvas.addEventListener('mousemove', this.draw.bind(this));
        this.canvas.addEventListener('mouseup', this.stopDrawing.bind(this));
        this.canvas.addEventListener('mouseout', this.stopDrawing.bind(this));
        
        // 触摸事件支持
        this.canvas.addEventListener('touchstart', this.handleTouch.bind(this));
        this.canvas.addEventListener('touchmove', this.handleTouch.bind(this));
        this.canvas.addEventListener('touchend', this.stopDrawing.bind(this));
    }
    
    startDrawing(e) {
        this.isDrawing = true;
        this.draw(e);
    }
    
    draw(e) {
        if (!this.isDrawing) return;
        
        const rect = this.canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        this.ctx.beginPath();
        this.ctx.moveTo(this.lastX || x, this.lastY || y);
        this.ctx.lineTo(x, y);
        this.ctx.stroke();
        
        [this.lastX, this.lastY] = [x, y];
    }
    
    stopDrawing() {
        this.isDrawing = false;
        [this.lastX, this.lastY] = [null, null];
    }
    
    handleTouch(e) {
        e.preventDefault();
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent(e.type === 'touchstart' ? 'mousedown' : 'mousemove', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        this.canvas.dispatchEvent(mouseEvent);
    }
    
    clear() {
        this.ctx.fillStyle = 'white';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
    }
    
    getImageData() {
        return this.canvas.toDataURL('image/png');
    }
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    const canvas = new DrawingCanvas();
    const resultContainer = document.querySelector('.result-container');
    const digitSpan = document.querySelector('.result .digit');
    const confidenceSpan = document.querySelector('.result .confidence span');
    
    // 清除按钮
    document.getElementById('clearButton').addEventListener('click', () => {
        canvas.clear();
        resultContainer.style.display = 'none';
    });
    
    // 识别按钮
    document.getElementById('predictButton').addEventListener('click', async () => {
        const button = document.getElementById('predictButton');
        const imageData = canvas.getImageData();
        
        try {
            // 添加加载状态
            button.disabled = true;
            button.classList.add('loading');
            
            // 将Base64图像数据转换为Blob
            const response = await fetch(imageData);
            const blob = await response.blob();
            
            // 创建FormData对象
            const formData = new FormData();
            formData.append('image', blob, 'digit.png');
            
            const result = await fetch('/api/mnist/predict', {
                method: 'POST',
                body: formData
            }).then(res => res.json());
            
            if (result.error) {
                throw new Error(result.error);
            }
            
            // 更新显示结果
            const resultContainer = document.querySelector('.result-container');
            const digitSpan = document.querySelector('.result .digit');
            const confidenceFill = document.querySelector('.confidence-meter .fill');
            const confidenceValue = document.querySelector('.confidence .value');
            
            // 先隐藏结果
            resultContainer.classList.add('hide');
            resultContainer.style.display = 'block';
            
            // 设置新的结果
            digitSpan.textContent = result.digit;
            const confidence = (result.confidence * 100).toFixed(2);
            confidenceValue.textContent = `${confidence}%`;
            confidenceFill.style.width = `${confidence}%`;
            
            // 显示结果
            setTimeout(() => {
                resultContainer.classList.remove('hide');
                resultContainer.classList.add('show');
            }, 50);
            
        } catch (error) {
            alert('识别失败：' + error.message);
        } finally {
            // 移除加载状态
            button.disabled = false;
            button.classList.remove('loading');
        }
    });
    
    // 添加绘画状态指示
    const drawingContainer = document.querySelector('.drawing-container');
    canvas.canvas.addEventListener('mousedown', () => {
        drawingContainer.classList.add('is-drawing');
    });
    canvas.canvas.addEventListener('mouseup', () => {
        drawingContainer.classList.remove('is-drawing');
    });
    canvas.canvas.addEventListener('mouseout', () => {
        drawingContainer.classList.remove('is-drawing');
    });
}); 