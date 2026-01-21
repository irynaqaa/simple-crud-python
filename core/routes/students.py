from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from core import db
from core.models import Student

students_bp = Blueprint('students', __name__, url_prefix='/students')


@students_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id: int):
    try:
        student = Student.query.get_or_404(id)

        if request.method == 'GET':
            return render_template('edit_student.html', student=student)

        # POST handling
        nama: str = request.form.get('nama', '').strip()
        kelas: str = request.form.get('kelas', '').strip()
        has_error: bool = False

        if not nama:
            flash('Nama is required.', 'error')
            has_error = True
        if not kelas:
            flash('Kelas is required.', 'error')
            has_error = True

        form_data = {'nama': nama, 'kelas': kelas}

        if has_error:
            return render_template('edit_student.html', student=student, form_data=form_data)

        # Update model fields
        student.nama = nama
        student.kelas = kelas

        try:
            db.session.commit()
            flash('Student updated successfully.', 'success')
            return redirect(url_for('students.list'))
        except Exception:
            db.session.rollback()
            current_app.logger.exception('Error updating student with id %s', id)
            flash('An error occurred while updating the student.', 'error')
            return render_template('edit_student.html', student=student, form_data=form_data)

    except Exception:
        current_app.logger.exception('Unexpected error in edit_student for id %s', id)
        flash('An unexpected error occurred.', 'error')
        return redirect(url_for('students.list'))