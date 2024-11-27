# Day 1 - 项目启动：创建AI学习平台的第一步

日期：2024-[MM-DD]

## 今日目标
- [x] 理解项目结构和虚拟环境的作用
- [x] 学习Flask框架基础知识
- [x] 掌握基本的前端开发知识

## 学习内容

### 1. Python虚拟环境
虚拟环境是Python项目的独立工作空间，它的作用是：

1. **项目隔离**
   - 每个项目有自己的依赖包版本
   - 避免不同项目之间的包版本冲突
   - 保持系统Python环境的清洁

2. **虚拟环境操作**
   ```bash
   # 创建虚拟环境
   python -m venv venv

   # 激活虚拟环境
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate

   # 退出虚拟环境
   deactivate
   ```

3. **依赖管理**
   ```bash
   # 安装依赖
   pip install flask tensorflow numpy pillow

   # 导出依赖列表
   pip freeze > requirements.txt

   # 从依赖列表安装
   pip install -r requirements.txt
   ```

### 2. Flask框架基础
Flask是一个轻量级的Python Web框架，主要概念：

1. **基本结构**
   ```python
   from flask import Flask, render_template

   # 创建Flask应用实例
   app = Flask(__name__)

   # 路由装饰器，将URL映射到函数
   @app.route('/')
   def home():
       return render_template('index.html')
   ```

2. **模板系统**
   - 使用Jinja2模板引擎
   - 支持模板继承和复用
   - 示例：
   ```html
   <!-- base.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}{% endblock %}</title>
   </head>
   <body>
       {% block content %}{% endblock %}
   </body>
   </html>

   <!-- index.html -->
   {% extends "base.html" %}
   {% block title %}首页{% endblock %}
   {% block content %}
       <h1>欢迎访问</h1>
   {% endblock %}
   ```

3. **静态文件处理**
   ```python
   # 在HTML中引用静态文件
   <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
   <script src="{{ url_for('static', filename='js/main.js') }}"></script>
   ```

### 3. 前端开发基础

1. **HTML结构**
   - 语义化标签的使用
   - 良好的文档结构
   ```html
   <header>网站头部</header>
   <nav>导航菜单</nav>
   <main>主要内容</main>
   <footer>网站底部</footer>
   ```

2. **CSS样式**
   - 选择器和优先级
   - Flexbox布局
   ```css
   /* 使用CSS变量定义主题色 */
   :root {
       --primary-color: #2c3e50;
       --secondary-color: #3498db;
   }

   /* Flexbox布局示例 */
   .container {
       display: flex;
       justify-content: space-between;
       align-items: center;
   }
   ```

3. **JavaScript交互**
   - DOM操作
   - 事件处理
   ```javascript
   // 等待DOM加载完成
   document.addEventListener('DOMContentLoaded', () => {
       // 获取元素
       const button = document.querySelector('.button');
       
       // 添加事件监听
       button.addEventListener('click', () => {
           // 处理点击事件
       });
   });
   ```

## 遇到的问题和解决方案

1. **问题：虚拟环境创建失败**
   - 原因：Python路径或权限问题
   - 解决方案：
     1. 确保Python已添加到系统环境变量
     2. 使用管理员权限运行命令行
     3. 检查项目路径是否包含特殊字符

2. **问题：模板渲染错误**
   - 原因：模板文件路径错误
   - 解决方案：
     1. 确保模板文件放在templates目录下
     2. 检查文件名大小写
     3. 使用正确的相对路径

## 今日收获

1. 理解了虚拟环境的重要性和使用方法
2. 掌握了Flask框架的基本概念和用法
3. 学会了前端三件套（HTML/CSS/JS）的基础知识
4. 理解了项目结构的组织方式

## 明日计划

- [ ] 学习数据库集成
- [ ] 实现用户认证功能
- [ ] 深入学习前端框架

## 小贴士

- 养成使用虚拟环境的好习惯
- 经常查看官方文档学习
- 代码要有适当的注释
- 保持良好的代码组织结构

## 学习资源

- [Flask官方文档](https://flask.palletsprojects.com/)
- [MDN Web文档](https://developer.mozilla.org/)
- [Python虚拟环境指南](https://docs.python.org/3/tutorial/venv.html)
- [Git基础教程](https://git-scm.com/book/zh/v2) 