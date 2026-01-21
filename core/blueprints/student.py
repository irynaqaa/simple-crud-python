from flask import Blueprint, flash, redirect, url_for
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from core.models.student import Student
from core.extensions import engine  # pure SQLAlchemy engine

SessionLocal = sessionmaker(bind=engine)

student_bp = Blueprint('student', __name__, url_prefix='/students')


@student_bp.route('/<int:id>/delete', methods=['GET'])
def delete_student(id: int):
    session = SessionLocal()
    try:
        student = session.get(Student, id)
        if not student:
            flash('Student not found.', 'error')
            return redirect(url_for('student.list'))

        session.delete(student)
        session.commit()
        flash('Student deleted successfully.', 'success')
    except SQLAlchemyError as e:
        session.rollback()
        flash(f'An error occurred while deleting the student: {str(e)}', 'error')
    finally:
        session.close()

    return redirect(url_for('student.list'))