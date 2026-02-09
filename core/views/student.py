from flask import Blueprint, request, jsonify, abort, current_app
from typing import Dict, Any, List
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError

# Assuming the SQLAlchemy engine is initialized in core.extensions
from core.extensions import engine
# Assuming the Student model is defined in core.models.student
from core.models.student import Student

# Create a session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

student_bp = Blueprint('student', __name__, url_prefix='/students')


def _student_to_dict(student: Student) -> Dict[str, Any]:
    return {
        "id": student.id,
        "name": student.name,
        "age": student.age,
        "email": student.email,
    }


@student_bp.route('/', methods=['GET'])
def get_students() -> Any:
    """Retrieve a list of all students."""
    with SessionLocal() as session:
        students: List[Student] = session.query(Student).all()
        result = [_student_to_dict(s) for s in students]
        return jsonify(result), 200


@student_bp.route('/<int:student_id>', methods=['GET'])
def get_student(student_id: int) -> Any:
    """Retrieve a single student by ID."""
    with SessionLocal() as session:
        student: Student | None = session.get(Student, student_id)
        if not student:
            abort(404, description=f"Student with id {student_id} not found.")
        return jsonify(_student_to_dict(student)), 200


@student_bp.route('/', methods=['POST'])
def create_student() -> Any:
    """Create a new student."""
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON payload.")

    name = data.get("name")
    age = data.get("age")
    email = data.get("email")

    if not (name and isinstance(age, int) and email):
        abort(400, description="Missing or invalid student fields.")

    new_student = Student(name=name, age=age, email=email)

    with SessionLocal() as session:
        session.add(new_student)
        try:
            session.commit()
            session.refresh(new_student)
        except SQLAlchemyError as e:
            session.rollback()
            current_app.logger.error(f"Error creating student: {e}")
            abort(500, description="Database error while creating student.")
        return jsonify(_student_to_dict(new_student)), 201


@student_bp.route('/<int:student_id>', methods=['PUT'])
def update_student(student_id: int) -> Any:
    """Update an existing student."""
    data = request.get_json()
    if not data:
        abort(400, description="Invalid JSON payload.")

    with SessionLocal() as session:
        student: Student | None = session.get(Student, student_id)
        if not student:
            abort(404, description=f"Student with id {student_id} not found.")

        name = data.get("name")
        age = data.get("age")
        email = data.get("email")

        if name is not None:
            student.name = name
        if isinstance(age, int):
            student.age = age
        if email is not None:
            student.email = email

        try:
            session.commit()
            session.refresh(student)
        except SQLAlchemyError as e:
            session.rollback()
            current_app.logger.error(f"Error updating student {student_id}: {e}")
            abort(500, description="Database error while updating student.")

        return jsonify(_student_to_dict(student)), 200


@student_bp.route('/<int:student_id>', methods=['DELETE'])
def delete_student(student_id: int) -> Any:
    """Delete a student."""
    with SessionLocal() as session:
        student: Student | None = session.get(Student, student_id)
        if not student:
            abort(404, description=f"Student with id {student_id} not found.")

        session.delete(student)
        try:
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            current_app.logger.error(f"Error deleting student {student_id}: {e}")
            abort(500, description="Database error while deleting student.")

        return jsonify({"message": f"Student {student_id} deleted."}), 200


__all__ = ["student_bp"]