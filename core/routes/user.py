from flask import Blueprint, render_template, make_response, current_app, Response
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker, Session

from core.models.user import User
from core.extensions import engine

SessionLocal = sessionmaker(bind=engine)

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/', methods=['GET'])
def list_users() -> Response:
    session: Session = SessionLocal()
    try:
        users = session.query(User).order_by(desc(User.id)).all()
    except Exception as e:
        current_app.logger.error(f"User list query failed: {e}")
        return make_response(render_template('error.html', message='Unable to retrieve users.'), 500)
    finally:
        session.close()
    response = make_response(render_template('user_list.html', users=users))
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'
    return response

__all__ = ['user_bp']