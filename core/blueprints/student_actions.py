from flask import Blueprint, request, current_app, make_response
from sqlalchemy.exc import IntegrityError
from typing import Optional

# Adjust import paths as needed for your project structure
from core.extensions import db
from core.models.student import Student

student_actions = Blueprint('student_actions', __name__)

def _extract_str(value: Optional[str]) -> str:
    return value.strip() if isinstance(value, str) else ""

def _extract_int(value: str) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

@student_actions.route('/edit-action', methods=['POST'])
def edit_action():
    # Check DB connection
    if not getattr(db, "session", None):
        return make_response("Database connection unavailable", 500)

    # Determine request payload source
    payload = request.get_json(silent=True) or {}
    form_data = request.form or {}

    # Detect 'update' flag
    update_flag = payload.get('update') or form_data.get('update')
    if not update_flag:
        return make_response('', 204)

    # Extract raw inputs
    raw_id = _extract_str(payload.get('id') or form_data.get('id'))
    raw_name = _extract_str(payload.get('name') or form_data.get('name'))
    raw_age = _extract_str(payload.get('age') or form_data.get('age'))
    raw_email = _extract_str(payload.get('email') or form_data.get('email'))

    # Validate required fields
    if not raw_email:
        return make_response("Email is required", 400)

    record_id = _extract_int(raw_id)
    if record_id is None or record_id <= 0:
        return make_response("Invalid record identifier", 400)

    # Retrieve existing student record
    student: Optional[Student] = db.session.get(Student, record_id)
    if not student:
        return make_response("Record not found", 404)

    # Update fields if provided
    if raw_name:
        student.name = raw_name
    if raw_age:
        age_int = _extract_int(raw_age)
        if age_int is not None:
            student.age = age_int
    student.email = raw_email

    # Commit changes with error handling
    try:
        db.session.commit()
    except IntegrityError as ie:
        db.session.rollback()
        current_app.logger.error(f"Integrity error while updating student {record_id}: {ie}")
        return make_response(f"Database update failed: {str(ie)}", 500)
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Unexpected error while updating student {record_id}: {e}")
        return make_response(f"Database update failed: {str(e)}", 500)

    return make_response("Record updated successfully", 200)

__all__ = ["student_actions"]