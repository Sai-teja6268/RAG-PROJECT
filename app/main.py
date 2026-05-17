from fastapi import FastAPI

from app.api.routes import ask, health, ingest
from app.core.config import settings
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    configure_logging()
    api = FastAPI(
        title=settings.app_name,
        description="AI Research & Document Management System",
        version="1.0.0"
    )   
    api.include_router(health.router)
    api.include_router(ask.router)
    api.include_router(ingest.router)
    return api


app = create_app()


def main() -> None:
    print(f"Run the API with: uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()

