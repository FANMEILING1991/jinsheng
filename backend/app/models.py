from sqlalchemy import Column, Integer, String, Text, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base


class CertificateInfo(Base):
    __tablename__ = "certificate_info"

    certificate_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    type = Column(String(100), nullable=True, index=True)
    industry = Column(String(100), nullable=True, index=True)
    price = Column(DECIMAL(10, 2), nullable=True)
    duration = Column(String(50), nullable=True)
    exam_period = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)

    schools = relationship("SchoolInfo", back_populates="certificate", cascade="all, delete-orphan")
    salaries = relationship("SalaryInfo", back_populates="certificate", cascade="all, delete-orphan")


class SchoolInfo(Base):
    __tablename__ = "school_info"

    school_id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_id = Column(Integer, ForeignKey("certificate_info.certificate_id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    course_content = Column(Text, nullable=True)
    mode = Column(String(50), nullable=True)
    fee = Column(DECIMAL(10, 2), nullable=True)
    contact_info = Column(Text, nullable=True)

    certificate = relationship("CertificateInfo", back_populates="schools")


class SalaryInfo(Base):
    __tablename__ = "salary_info"

    salary_id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_id = Column(Integer, ForeignKey("certificate_info.certificate_id"), nullable=False, index=True)
    position = Column(String(100), nullable=True, index=True)
    region = Column(String(100), nullable=True, index=True)
    min_salary = Column(DECIMAL(10, 2), nullable=True)
    max_salary = Column(DECIMAL(10, 2), nullable=True)

    certificate = relationship("CertificateInfo", back_populates="salaries")


class UserInfo(Base):
    __tablename__ = "user_info"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    profession = Column(String(100), nullable=True, index=True)
    age = Column(Integer, nullable=True)
    education = Column(String(100), nullable=True, index=True)
    location = Column(String(100), nullable=True, index=True)



