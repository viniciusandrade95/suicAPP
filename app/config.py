import os
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from dotenv import load_dotenv

ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(ENV_PATH)


def _ensure_sslmode(database_url: str) -> str:
    if not database_url:
        return database_url

    parsed = urlparse(database_url)
    if parsed.scheme not in {"postgres", "postgresql"}:
        return database_url

    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    query.setdefault("sslmode", "require")

    return urlunparse(parsed._replace(query=urlencode(query)))


def _get_pool_size() -> int:
    return int(os.getenv("DB_POOL_SIZE", "5"))


def _get_max_overflow() -> int:
    return int(os.getenv("DB_MAX_OVERFLOW", "10"))


class Config:
    SQLALCHEMY_DATABASE_URI = _ensure_sslmode(
        os.getenv("DATABASE_URL", "sqlite:///app.db")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_size": _get_pool_size(),
        "max_overflow": _get_max_overflow(),
    }
    SECRET_KEY = os.getenv("SECRET_KEY")
