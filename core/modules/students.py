from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError
from typing import Any

from core.db import Session  # Direct SQLAlchemy session factory
from core.models import DataSiswa

students_bp = Blueprint("students", __name__, url_prefix="/students")


def get_student_or_404(student_id: int) -> DataSiswa:
    """Retrieve a DataSiswa instance by ID or abort with 404."""
    session = Session()
    try:
        student = session.get(DataSiswa, student_id)
        if student is None:
            abort(404, description=f"Student with id {student_id} not found")
        return student
    finally:
        session.close()


@students_bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit_student(id: int) -> Any:
    session = Session()
    try:
        student = session.get(DataSiswa, id)
        if student is None:
            abort(404, description=f"Student with id {id} not found")

        if request.method == "POST":
            nama = request.form.get("nama", "").strip()
            kelas = request.form.get("kelas", "").strip()

            if not nama or not kelas:
                flash('Both "nama" and "kelas" fields are required.', "error")
                return render_template("students/edit.html", student=student)

            student.nama = nama
            student.kelas = kelas

            try:
                session.commit()
                flash("Student updated successfully.", "success")
                return redirect(url_for("students.list"))  # Adjust endpoint if needed
            except IntegrityError:
                session.rollback()
                flash("An error occurred while updating the student.", "error")
                return render_template("students/edit.html", student=student)

        # GET request
        return render_template("students/edit.html", student=student)
    finally:
        session.close()


def register_students_blueprint(app) -> None:
    """Register the students blueprint with the Flask application."""
    app.register_blueprint(students_bp)