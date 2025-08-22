from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from ..db import get_db, init_db
from .. import models, schemas


router = APIRouter()


@router.on_event("startup")
def _startup():
    init_db()


@router.get("/certificates", response_model=list[schemas.CertificateInfo])
def search_certificates(
    q: Optional[str] = Query(None, description="关键字：名称/描述/行业/类型"),
    region: Optional[str] = None,
    profession: Optional[str] = None,
    education: Optional[str] = None,
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    query = db.query(models.CertificateInfo)
    if q:
        like = f"%{q}%"
        query = query.filter(
            (models.CertificateInfo.name.ilike(like))
            | (models.CertificateInfo.description.ilike(like))
            | (models.CertificateInfo.industry.ilike(like))
            | (models.CertificateInfo.type.ilike(like))
        )
    # 预留：region/profession/education 可用于更细致的规则
    results = query.offset((page - 1) * page_size).limit(page_size).all()
    return results



