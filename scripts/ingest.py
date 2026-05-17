import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.config import settings
from app.services.ingestion_service import IngestionService


def main() -> None:
    result = IngestionService().ingest(settings.data_dir)
    print(result)


if __name__ == "__main__":
    main()
