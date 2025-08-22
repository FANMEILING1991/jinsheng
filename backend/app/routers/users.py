from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from ..db import get_db, init_db
from .. import models, schemas


router = APIRouter()


@router.on_event("startup")
def _startup():
    init_db()


@router.post("/", response_model=schemas.UserInfo)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.UserInfo).filter(models.UserInfo.email == payload.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="email already exists")
    user = models.UserInfo(
        email=payload.email,
        name=payload.name,
        profession=payload.profession,
        age=payload.age,
        education=payload.education,
        location=payload.location,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/", response_model=list[schemas.UserInfo])
def list_users(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    query = db.query(models.UserInfo)
    users = query.offset((page - 1) * page_size).limit(page_size).all()
    return users



