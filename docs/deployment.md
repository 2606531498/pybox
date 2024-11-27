# 部署指南

## GitHub部署
1. 创建仓库
2. 推送代码：
```bash
git remote add origin [仓库地址]
git push -u origin main
```

## Vercel部署
1. 登录Vercel
2. 导入GitHub仓库
3. 配置环境变量：
   - FLASK_ENV=production
   - SECRET_KEY=[你的密钥]

4. 部署成功后，可以通过以下地址访问：
   - [你的Vercel项目地址]

## 注意事项
1. 确保requirements.txt包含所有依赖
2. 模型文件需要在部署时重新训练
3. 检查环境变量配置
4. 测试所有功能是否正常 