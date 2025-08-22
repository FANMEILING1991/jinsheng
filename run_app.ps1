$ErrorActionPreference = "Stop"

Set-Location -Path $PSScriptRoot

function Ensure-Python() {
  if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "未找到 Python，请先安装 Python 3.11+。" -ForegroundColor Red
    Read-Host "按回车键退出"
    exit 1
  }
}

Ensure-Python

Write-Host "[1/4] 安装后端依赖（SQLite 版）..." -ForegroundColor Cyan
python -m pip install -r .\backend\requirements-sqlite.txt --disable-pip-version-check

Write-Host "[2/4] 启动后端服务..." -ForegroundColor Cyan
Start-Process -WindowStyle Normal powershell -ArgumentList "-NoExit","-Command","python -m uvicorn app.main:app --app-dir backend --host 127.0.0.1 --port 8000 --reload"

Write-Host "[3/4] 初始化示例数据..." -ForegroundColor Cyan
python .\scripts\seed.py

Write-Host "[4/4] 打开接口文档..." -ForegroundColor Cyan
Start-Process "http://127.0.0.1:8000/docs"

Write-Host "服务已启动。若需停止，请关闭后端窗口。" -ForegroundColor Green


