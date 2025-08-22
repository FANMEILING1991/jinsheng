## Backend - Certificate Finder & Recommender

### 本地运行

1. 创建并激活虚拟环境（可选）
2. 安装依赖
```
pip install -r requirements.txt
```
3. 运行（默认 SQLite 在 `./data/app.db`）
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
4. 访问接口文档
```
http://localhost:8000/docs
```

### 初始化示例数据
```
python scripts/seed.py
```

### 环境变量
- `DATABASE_URL`：例 `postgresql+psycopg2://user:pass@localhost:5432/certdb`

### 目录结构
```
backend/
  app/
    main.py
    config.py
    db.py
    models.py
    schemas.py
    routers/
      users.py
      certificates.py
      search.py
      recommend.py
scripts/
  seed.py
```



