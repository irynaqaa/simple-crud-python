from flask import Blueprint, request, redirect, url_for, flash, render_template
from models import User, db
from sqlalchemy.exc import SQLAlchemyError

core = Blueprint('core', __name__)

@core.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        age = request.form.get('age', '').strip()
        email = request.form.get('email', '').strip()

        if not name or not age or not email:
            flash('All fields are required!', 'error')
            return redirect(url_for('core.add_user'))

        new_user = User(name=name, age=age, email=email)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('core.index'))
        except SQLAlchemyError:
            db.session.rollback()
            flash('Error adding user. Please try again.', 'error')
            return redirect(url_for('core.add_user'))

    return render_template('add_data.html')

@core.route('/users/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully!', 'success')
            return redirect(url_for('core.index'))
        else:
            flash('User not found!', 'error')
            return redirect(url_for('core.index'))
    except SQLAlchemyError:
        db.session.rollback()
        flash('Error deleting user. Please try again.', 'error')
        return redirect(url_for('core.index'))

@core.route('/')
def index():
    try:
        users = User.query.order_by(User.id.desc()).all()
        return render_template('index.html', users=users)
    except SQLAlchemyError:
        flash('Error retrieving users. Please try again.', 'error')
        return render_template('index.html', users=[])

@core.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get(user_id)
    if request.method == 'POST':
        email = request.form.get('email', '').strip()

        if not email:
            flash('Email is required!', 'error')
            return redirect(url_for('core.edit_user', user_id=user_id))

        user.email = email
        try:
            db.session.commit()
            flash('User updated successfully!', 'success')
            return redirect(url_for('core.index'))
        except SQLAlchemyError:
            db.session.rollback()
            flash('Error updating user. Please try again.', 'error')
            return redirect(url_for('core.edit_user', user_id=user_id))

    return render_template('edit.html', user=user)