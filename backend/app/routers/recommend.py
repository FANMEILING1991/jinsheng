from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..db import get_db, init_db
from .. import models, schemas
from ..config import get_settings


router = APIRouter()


@router.on_event("startup")
def _startup():
    init_db()


@router.get("/certificates", response_model=list[schemas.CertificateInfo])
def recommend_certificates(
    profession: Optional[str] = None,
    age: Optional[int] = None,
    education: Optional[str] = None,
    location: Optional[str] = None,
    exam_time: Optional[str] = Query(None, description="考证时间/周期偏好"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    settings = get_settings()
    base_query = db.query(models.CertificateInfo)

    # 召回阶段：宽松匹配，尽量包含潜在相关项
    if profession:
        base_query = base_query.filter(models.CertificateInfo.industry.ilike(f"%{profession}%"))
    if education:
        base_query = base_query.filter(models.CertificateInfo.description.ilike(f"%{education}%"))
    if exam_time:
        base_query = base_query.filter(models.CertificateInfo.exam_period.ilike(f"%{exam_time}%"))

    candidates = base_query.limit(200).all()

    def score(c: models.CertificateInfo) -> int:
        s = 0
        if profession and c.industry and profession.lower() in c.industry.lower():
            s += settings.REC_WEIGHT_PROFESSION
        if education and c.description and education.lower() in c.description.lower():
            s += settings.REC_WEIGHT_EDUCATION
        if location and c.description and location.lower() in c.description.lower():
            s += settings.REC_WEIGHT_LOCATION
        if exam_time and c.exam_period and exam_time.lower() in c.exam_period.lower():
            s += settings.REC_WEIGHT_EXAM_PERIOD
        return s

    ranked = sorted(candidates, key=score, reverse=True)
    start = (page - 1) * page_size
    end = start + page_size
    return ranked[start:end]



