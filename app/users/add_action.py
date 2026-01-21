from flask import Blueprint, request, Response
from sqlalchemy import text
from app.extensions import db
from app.models import User

PAGE_TITLE = "Add Data"

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('/addAction', methods=['POST'])
def add_action() -> Response:
    response = f"<html><head><title>{PAGE_TITLE}</title></head><body>"
    if 'submit' in request.form:
        name: str = request.form.get('name', '')
        age: str = request.form.get('age', '')
        raw_email: str = request.form.get('email', '')

        escaped_email: str | None = db.session.scalar(
            text("SELECT REPLACE(:e, \"'\", \"\\\\'\")"),
            {"e": raw_email}
        )

        if escaped_email and escaped_email.strip():
            user = User(name=name, age=age, email=escaped_email)
            try:
                db.session.add(user)
                db.session.commit()
            except Exception:
                db.session.rollback()
    response += "</body></html>"
    return Response(response, mimetype='text/html')