from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    app = FastAPI(title="Certificate Finder & Recommender", version="0.1.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Lazy imports to avoid circular dependencies
    from .routers import users, certificates, search, recommend

    app.include_router(users.router, prefix="/api/users", tags=["users"])
    app.include_router(certificates.router, prefix="/api/certificates", tags=["certificates"])
    app.include_router(search.router, prefix="/api/search", tags=["search"])
    app.include_router(recommend.router, prefix="/api/recommend", tags=["recommend"])

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    return app


app = create_app()



