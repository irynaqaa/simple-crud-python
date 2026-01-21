from flask import Flask
from .routes.user import user_bp
from .routes.students import student_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    app.register_blueprint(student_bp)
    return app


app: Flask = create_app()