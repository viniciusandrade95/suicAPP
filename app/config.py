import os
from pathlib import Path

from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parents[1] / "env"
load_dotenv(ENV_PATH)

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
