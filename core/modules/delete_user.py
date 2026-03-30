import logging
from some_orm import db, User  # Adjust the import based on actual ORM setup

# Constants
USER_ID = 'user_id'
DB_CONNECTION = 'db_connection_string'
DELETE_USER_SQL = 'DELETE FROM users WHERE id = :user_id'

# Set up logging
logging.basicConfig(level=logging.INFO)

def delete_user(user_id):
    # Validation
    if user_id is None or not isinstance(user_id, int):
        raise ValueError('Invalid User ID')

    try:
        # User Deletion
        user_to_delete = db.session.query(User).filter(User.id == user_id).first()
        if user_to_delete:
            db.session.delete(user_to_delete)
            db.session.commit()
            logging.info(f'User with ID {user_id} deleted successfully.')
            return 'User deleted successfully.'
        else:
            raise ValueError('User not found')
    except Exception as e:
        logging.error(f'Error deleting user with ID {user_id}: {e}')
        return f'Error: {e}'
