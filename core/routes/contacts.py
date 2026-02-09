from typing import List, Optional

from flask import Blueprint, request, render_template, redirect, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SessionType

from core.models import Contact
from core.db import engine  # Assumes an SQLAlchemy Engine is defined in core/db.py

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

contacts_bp = Blueprint('contacts', __name__, url_prefix='/contacts')


@contacts_bp.route('/add', methods=['GET', 'POST'])
def add_contact() -> str:
    if request.method == 'GET':
        return render_template('contacts/add.html')

    if 'submit' not in request.form:
        return redirect(url_for('contacts.add_contact'))

    name: str = request.form.get('name', '').strip()
    age_str: str = request.form.get('age', '').strip()
    email: str = request.form.get('email', '').strip()

    errors: List[str] = []
    if not name:
        errors.append('Name field is empty.')
    if not age_str:
        errors.append('Age field is empty.')
    if not email:
        errors.append('Email field is empty.')

    age_int: Optional[int] = None
    if age_str:
        try:
            age_int = int(age_str)
        except ValueError:
            errors.append('Age field is empty.')

    if errors:
        return render_template('contacts/add.html', errors=errors)

    session: SessionType = SessionLocal()
    try:
        new_contact = Contact(name=name, age=age_int, email=email)
        session.add(new_contact)
        session.commit()
    except Exception:
        session.rollback()
        errors.append('Database error occurred.')
        return render_template('contacts/add.html', errors=errors)
    finally:
        session.close()

    return render_template('contacts/add.html', success=True)