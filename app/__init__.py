from flask import Flask
from core.modules.students import students_bp


def create_app() -> Flask:
    """
    Application factory for the Flask app.
    """
    app = Flask(__name__, instance_relative_config=False)

    # Basic configuration; can be overridden by environment variables or config files
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE="sqlite:///app.db",
    )

    # Register Blueprints
    app.register_blueprint(students_bp, url_prefix="/students")

    return app


__all__ = ["create_app"]