import time

from flask import Blueprint, jsonify
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db

bp = Blueprint("health", __name__)

@bp.get("/health")
def health():
    return jsonify(status="ok"), 200


@bp.get("/health/db")
def health_db():
    start = time.perf_counter()
    try:
        db.session.execute(text("SELECT 1"))
        db.session.commit()
    except SQLAlchemyError as exc:
        db.session.rollback()
        return jsonify(status="error", detail=str(exc)), 503

    latency_ms = (time.perf_counter() - start) * 1000
    return jsonify(status="ok", latency_ms=round(latency_ms, 2)), 200
