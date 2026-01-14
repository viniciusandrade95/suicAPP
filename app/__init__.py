from flask import Flask
from dotenv import load_dotenv

from .config import Config
from .extensions import db, migrate
from .api.health import bp as health_bp

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    # extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # routes
    app.register_blueprint(health_bp)

    return app
