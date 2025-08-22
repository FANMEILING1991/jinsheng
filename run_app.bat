@echo off
setlocal enabledelayedexpansion

REM 进入脚本所在目录（项目根目录）
cd /d %~dp0

REM 检查 Python
where python >nul 2>nul
if errorlevel 1 (
  echo 未找到 Python，请先安装 Python 3.11+。
  pause
  exit /b 1
)

echo [1/4] 安装后端依赖（SQLite 版，无需 Postgres 驱动）...
python -m pip install -r backend\requirements-sqlite.txt --disable-pip-version-check
if errorlevel 1 (
  echo 依赖安装失败。
  pause
  exit /b 1
)

echo [2/4] 启动后端服务...
start "backend" cmd /c "cd backend ^&^& python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload ^|^| pause"

echo [3/4] 初始化示例数据...
python scripts\seed.py

echo [4/4] 打开接口文档...
start "" http://127.0.0.1:8000/docs

echo 服务已启动。如需停止，请关闭名为 backend 的窗口。
pause


