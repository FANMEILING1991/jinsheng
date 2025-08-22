from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..db import get_db, init_db
from .. import models, schemas


router = APIRouter()


@router.on_event("startup")
def _startup():
    init_db()


@router.post("/", response_model=schemas.CertificateInfo)
def create_certificate(payload: schemas.CertificateCreate, db: Session = Depends(get_db)):
    entity = models.CertificateInfo(
        name=payload.name,
        type=payload.type,
        industry=payload.industry,
        price=payload.price,
        duration=payload.duration,
        exam_period=payload.exam_period,
        description=payload.description,
    )
    db.add(entity)
    db.commit()
    db.refresh(entity)
    return entity


@router.get("/", response_model=list[schemas.CertificateInfo])
def list_certificates(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    industry: Optional[str] = None,
    type: Optional[str] = None,
):
    query = db.query(models.CertificateInfo)
    if industry:
        query = query.filter(models.CertificateInfo.industry == industry)
    if type:
        query = query.filter(models.CertificateInfo.type == type)
    items = query.offset((page - 1) * page_size).limit(page_size).all()
    return items


@router.get("/{certificate_id}", response_model=schemas.CertificateInfo)
def get_certificate(certificate_id: int, db: Session = Depends(get_db)):
    entity = db.query(models.CertificateInfo).filter(models.CertificateInfo.certificate_id == certificate_id).first()
    if not entity:
        raise HTTPException(status_code=404, detail="certificate not found")
    return entity



