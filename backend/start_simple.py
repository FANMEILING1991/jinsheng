import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Certificate Finder & Recommender")

@app.get("/")
def read_root():
    return {"message": "Certificate Finder API is running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("start_simple:app", host="127.0.0.1", port=8000, reload=True)
