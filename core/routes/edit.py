from flask import Blueprint, request, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_NAME = os.getenv('DB_NAME')

engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')
Session = sessionmaker(bind=engine)

edit_bp = Blueprint('edit', __name__)

@edit_bp.route('/editAction', methods=['POST'])
def edit_action():
    if request.method != 'POST':
        return jsonify({'error': 'Invalid request method'}), 405

    data = request.get_json()
    user_id = data.get('user_id')
    email = data.get('email')

    if not email:
        return jsonify({'error': 'Email cannot be empty'}), 400

    email = email.strip()

    try:
        session = Session()
        result = session.execute(text("UPDATE users SET email = :email WHERE id = :user_id"), {'email': email, 'user_id': user_id})
        session.commit()

        if result.rowcount == 0:
            return jsonify({'error': 'User not found or no changes made'}), 404

        return jsonify({'message': 'Email updated successfully'}), 200

    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500

    finally:
        session.close()