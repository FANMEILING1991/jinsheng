# Vercel 部署指南

## 部署步骤

### 1. 注册 Vercel 账户
- 访问 https://vercel.com/
- 点击 "Sign Up" 或 "Continue with GitHub"
- 使用 GitHub 账户登录（推荐）

### 2. 导入项目
- 登录后点击 "New Project"
- 选择 "Import Git Repository"
- 找到并选择你的仓库：`FANMEILING1991/jinsheng`

### 3. 配置项目
- **Project Name**: `jinsheng-backend`（或保持默认）
- **Framework Preset**: 选择 "Other"
- **Root Directory**: 保持默认（根目录）
- **Build Command**: 留空（Vercel 会自动检测）
- **Output Directory**: 留空
- **Install Command**: 留空

### 4. 环境变量配置
在部署前，添加以下环境变量：
- `ENV`: `production`
- `PORT`: `8000`

### 5. 部署
- 点击 "Deploy"
- Vercel 会自动开始构建和部署
- 等待部署完成（通常需要 2-5 分钟）

## 部署完成后
- 你的应用将在 `https://your-app-name.vercel.app` 运行
- API 文档：`https://your-app-name.vercel.app/docs`
- 健康检查：`https://your-app-name.vercel.app/health`

## Vercel 的优势
- **完全免费**：无使用限制
- **极速部署**：全球边缘网络
- **自动 HTTPS**：SSL 证书自动配置
- **自动部署**：GitHub 推送后自动更新
- **全球 CDN**：访问速度快
- **无服务器架构**：按需扩展

## 注意事项
- Vercel 使用无服务器函数，每次请求有 30 秒超时限制
- 适合 API 服务，但长时间运行的任务有限制
- 数据库需要单独配置（可以使用 Railway 的 PostgreSQL 或 Vercel Postgres）

## 数据库配置建议
由于 Vercel 主要提供无服务器函数，建议：
1. 使用 Railway 的 PostgreSQL 数据库（免费）
2. 或者使用 Vercel Postgres（有免费层）
3. 在环境变量中配置 `DATABASE_URL`

## 自动部署
- 每次推送到 GitHub 的 `main` 分支时，Vercel 会自动重新部署
- 可以在 Vercel 控制台查看部署历史和状态
