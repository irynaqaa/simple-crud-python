from flask import Blueprint, request, redirect, url_for, Response
from typing import Optional

from core import db
from core.models import Student

core_bp = Blueprint('core', __name__)

@core_bp.route('/delete', methods=['GET', 'POST'])
def delete_student() -> Response:
    raw_id: Optional[str] = request.values.get('id')
    student_id: Optional[int] = None

    if raw_id is not None:
        try:
            student_id = int(raw_id)
        except (ValueError, TypeError):
            student_id = None

    if student_id is not None:
        try:
            db.session.query(Student).filter_by(id=student_id).delete()
            db.session.commit()
        except Exception:
            db.session.rollback()

    return redirect(url_for('index'))