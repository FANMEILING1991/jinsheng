from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr


class SchoolInfo(BaseModel):
    school_id: int
    certificate_id: int
    name: str
    course_content: Optional[str] = None
    mode: Optional[str] = None
    fee: Optional[float] = None
    contact_info: Optional[str] = None

    class Config:
        from_attributes = True


class SalaryInfo(BaseModel):
    salary_id: int
    certificate_id: int
    position: Optional[str] = None
    region: Optional[str] = None
    min_salary: Optional[float] = None
    max_salary: Optional[float] = None

    class Config:
        from_attributes = True


class CertificateInfo(BaseModel):
    certificate_id: int
    name: str
    type: Optional[str] = None
    industry: Optional[str] = None
    price: Optional[float] = None
    duration: Optional[str] = None
    exam_period: Optional[str] = None
    description: Optional[str] = None
    schools: List[SchoolInfo] = []
    salaries: List[SalaryInfo] = []

    class Config:
        from_attributes = True


class CertificateCreate(BaseModel):
    name: str = Field(..., max_length=255)
    type: Optional[str] = Field(None, max_length=100)
    industry: Optional[str] = Field(None, max_length=100)
    price: Optional[float] = None
    duration: Optional[str] = Field(None, max_length=50)
    exam_period: Optional[str] = Field(None, max_length=50)
    description: Optional[str] = None


class UserInfo(BaseModel):
    user_id: int
    name: Optional[str] = None
    email: EmailStr
    profession: Optional[str] = None
    age: Optional[int] = None
    education: Optional[str] = None
    location: Optional[str] = None

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    profession: Optional[str] = None
    age: Optional[int] = None
    education: Optional[str] = None
    location: Optional[str] = None



