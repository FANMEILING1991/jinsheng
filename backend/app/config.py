import os
from functools import lru_cache


class Settings:
    APP_NAME: str = "Certificate Finder & Recommender"
    ENV: str = os.getenv("ENV", "dev")

    # 云部署时使用环境变量 PORT，本地开发使用默认值
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # 云部署时使用 PostgreSQL，本地开发使用 SQLite
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./backend/data/app.db")

    # Pagination defaults
    PAGE_SIZE_DEFAULT: int = int(os.getenv("PAGE_SIZE_DEFAULT", "20"))
    PAGE_SIZE_MAX: int = int(os.getenv("PAGE_SIZE_MAX", "100"))

    # Recommendation weights (defaults from user preference)
    REC_WEIGHT_PROFESSION: int = int(os.getenv("REC_WEIGHT_PROFESSION", "5"))
    REC_WEIGHT_EDUCATION: int = int(os.getenv("REC_WEIGHT_EDUCATION", "3"))
    REC_WEIGHT_LOCATION: int = int(os.getenv("REC_WEIGHT_LOCATION", "4"))
    REC_WEIGHT_EXAM_PERIOD: int = int(os.getenv("REC_WEIGHT_EXAM_PERIOD", "2"))

    # Crawler source priorities (higher first)
    CRAWLER_SOURCES: tuple[str, ...] = tuple(
        os.getenv(
            "CRAWLER_SOURCES",
            "中华考试网,中国教育在线",
        ).split(",")
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()



