# 云部署指南

## Railway 部署步骤

### 1. 注册 Railway 账号
- 访问 https://railway.app/
- 使用 GitHub 账号登录

### 2. 创建新项目
- 点击 "New Project"
- 选择 "Deploy from GitHub repo"
- 连接你的 GitHub 仓库

### 3. 自动部署
- Railway 会自动检测 Python 项目
- 使用 `railway.json` 配置
- 自动安装依赖并启动服务

### 4. 获取访问地址
- 部署完成后，Railway 会提供一个公网地址
- 格式类似：`https://your-app-name.railway.app`

### 5. 访问 API 文档
- 主页面：`https://your-app-name.railway.app/`
- API 文档：`https://your-app-name.railway.app/docs`
- 健康检查：`https://your-app-name.railway.app/health`

## 环境变量配置

Railway 会自动设置：
- `PORT`: 服务端口
- `DATABASE_URL`: PostgreSQL 数据库连接

## 数据库初始化

部署后需要初始化数据：
```bash
# 在 Railway 控制台执行
cd backend && python scripts/seed.py
```

## 其他云平台选项

### Vercel
- 适合静态网站，需要调整配置

### Render
- 类似 Railway，免费额度充足

### Heroku
- 需要信用卡验证，但稳定可靠
