from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

APP_NAME = os.getenv("APP_NAME", "FastAPI App")
ENV = os.getenv("ENV", "production")
DATABASE_URL = os.getenv("DATABASE_URL")