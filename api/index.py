from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os

# 创建 FastAPI 应用
app = FastAPI(
    title="证书查询与推荐系统",
    description="提供证书信息查询、搜索和个性化推荐服务",
    version="1.0.0"
)

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class Certificate(BaseModel):
    id: int
    name: str
    description: str
    price: float
    exam_time: str
    validity_period: str
    difficulty: str
    profession: str
    education: str
    region: str

# 示例数据
sample_certificates = [
    Certificate(
        id=1,
        name="注册会计师",
        description="会计行业的顶级证书",
        price=5000.0,
        exam_time="每年5月和10月",
        validity_period="终身有效",
        difficulty="高",
        profession="会计",
        education="本科",
        region="全国"
    ),
    Certificate(
        id=2,
        name="律师资格证",
        description="法律行业的执业证书",
        price=3000.0,
        exam_time="每年9月",
        validity_period="终身有效",
        difficulty="高",
        profession="法律",
        education="本科",
        region="全国"
    ),
    Certificate(
        id=3,
        name="教师资格证",
        description="教育行业的执业证书",
        price=2000.0,
        exam_time="每年3月和11月",
        validity_period="5年",
        difficulty="中等",
        profession="教育",
        education="专科",
        region="全国"
    )
]

@app.get("/")
async def root():
    return {"message": "证书查询与推荐系统 API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "证书查询与推荐系统"}

@app.get("/certificates/", response_model=List[Certificate])
async def get_certificates():
    """获取所有证书列表"""
    return sample_certificates

@app.get("/certificates/{certificate_id}", response_model=Certificate)
async def get_certificate(certificate_id: int):
    """根据ID获取特定证书"""
    for cert in sample_certificates:
        if cert.id == certificate_id:
            return cert
    return {"error": "证书未找到"}

@app.get("/search/")
async def search_certificates(q: str = ""):
    """搜索证书"""
    if not q:
        return sample_certificates
    
    results = []
    for cert in sample_certificates:
        if (q.lower() in cert.name.lower() or 
            q.lower() in cert.description.lower() or
            q.lower() in cert.profession.lower()):
            results.append(cert)
    
    return results

@app.get("/recommend/")
async def get_recommendations(
    profession: Optional[str] = None,
    education: Optional[str] = None,
    region: Optional[str] = None,
    exam_time: Optional[str] = None
):
    """获取个性化推荐"""
    # 推荐权重：职业(5) > 地区(4) > 学历(3) > 考试时间(2)
    recommendations = []
    
    for cert in sample_certificates:
        score = 0
        
        if profession and cert.profession == profession:
            score += 5
        if region and cert.region == region:
            score += 4
        if education and cert.education == education:
            score += 3
        if exam_time and cert.exam_time == exam_time:
            score += 2
            
        if score > 0:
            recommendations.append({"certificate": cert, "score": score})
    
    # 按分数排序
    recommendations.sort(key=lambda x: x["score"], reverse=True)
    
    return recommendations

# 这是 Vercel 需要的
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
