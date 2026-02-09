from flask import Blueprint, request, render_template, Response
from typing import List

from sqlalchemy.orm import Session

from core.models import Student
from core.database import SessionLocal

student_bp = Blueprint('student', __name__)

@student_bp.route('/add-siswa', methods=['POST'])
def add_student_post() -> Response:
    if 'submit' not in request.form:
        errors: List[str] = ['Form submission missing.']
        return render_template('add_student_result.html', errors=errors, success=False)

    raw_name: str = request.form.get('name', '').strip()
    raw_age: str = request.form.get('age', '').strip()
    raw_email: str = request.form.get('email', '').strip()

    sanitized_name: str = raw_name
    sanitized_age: str = raw_age
    sanitized_email: str = raw_email

    errors: List[str] = []

    if not sanitized_name:
        errors.append('Name is required.')
    if not sanitized_age:
        errors.append('Age is required.')
    if not sanitized_email:
        errors.append('Email is required.')

    if errors:
        return render_template('add_student_result.html', errors=errors, success=False)

    new_student = Student(
        nama=sanitized_name,
        kelas=sanitized_age,
        email=sanitized_email
    )

    session: Session = SessionLocal()
    try:
        session.add(new_student)
        session.commit()
    except Exception as e:
        session.rollback()
        errors.append('Database error: ' + str(e))
        return render_template('add_student_result.html', errors=errors, success=False)
    finally:
        session.close()

    return render_template('add_student_result.html', success=True, errors=[])