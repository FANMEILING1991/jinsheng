import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "backend"))

from app.db import SessionLocal, init_db  # noqa: E402
from app import models  # noqa: E402


def run():
    os.makedirs(ROOT / "backend" / "data", exist_ok=True)
    init_db()
    db = SessionLocal()
    try:
        # Seed certificates
        certs = [
            dict(
                name="人力资源管理师",
                type="职业资格",
                industry="人力资源",
                price=2500.0,
                duration="2-3个月",
                exam_period="半年一考",
                description="覆盖招聘、培训、薪酬、绩效的综合性证书",
            ),
            dict(
                name="PMP 项目管理专业人士",
                type="国际认证",
                industry="项目管理",
                price=4800.0,
                duration="3-4个月",
                exam_period="季度",
                description="国际通用的项目管理认证",
            ),
        ]

        for c in certs:
            entity = models.CertificateInfo(**c)
            db.add(entity)
        db.commit()

        # Link schools
        hr = db.query(models.CertificateInfo).filter(models.CertificateInfo.name == "人力资源管理师").first()
        pmp = db.query(models.CertificateInfo).filter(models.CertificateInfo.name == "PMP 项目管理专业人士").first()

        schools = [
            dict(
                certificate_id=hr.certificate_id,
                name="尚德机构",
                course_content="人资四大模块精讲+冲刺",
                mode="线上",
                fee=2999.0,
                contact_info="400-000-0000; www.sunlands.com",
            ),
            dict(
                certificate_id=pmp.certificate_id,
                name="新东方",
                course_content="PMBOK 知识体系+真题解析",
                mode="线下",
                fee=6800.0,
                contact_info="400-111-1111; www.xdf.cn",
            ),
        ]
        for s in schools:
            db.add(models.SchoolInfo(**s))
        db.commit()

        # Salaries
        salaries = [
            dict(
                certificate_id=hr.certificate_id,
                position="HR 专员",
                region="北京",
                min_salary=8000.0,
                max_salary=15000.0,
            ),
            dict(
                certificate_id=pmp.certificate_id,
                position="项目经理",
                region="上海",
                min_salary=18000.0,
                max_salary=35000.0,
            ),
        ]
        for s in salaries:
            db.add(models.SalaryInfo(**s))
        db.commit()

        print("Seed completed.")
    finally:
        db.close()


if __name__ == "__main__":
    run()


