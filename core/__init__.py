from flask import Flask


def create_app() -> Flask:
    """
    Application factory that creates and configures the Flask app,
    then registers all required blueprints.
    """
    app = Flask(__name__)

    # Blueprint registrations – placed after any extension initialization
    from .routes.contacts import contacts_bp
    app.register_blueprint(contacts_bp)

    from .routes.add_student import blueprint as student_bp
    app.register_blueprint(student_bp)

    # Importing the module registers its view(s) on the appropriate blueprint
    from .routes import delete_student  # noqa: F401

    from .blueprints.student_actions import student_actions
    app.register_blueprint(student_actions)

    return app


__all__ = ["create_app"]