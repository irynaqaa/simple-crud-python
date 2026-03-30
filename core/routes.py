from flask import Blueprint, redirect, render_template, request, url_for
from core.delete_user import delete_user

# Create a blueprint for user management routes
user_management_bp = Blueprint('user_management', __name__)

@user_management_bp.route('/delete_user/<int:user_id>', methods=['POST', 'DELETE'])
def delete_user_route(user_id):
    """Handles the deletion of a user by user ID."""
    try:
        # Call the delete_user function to delete the user
        success = delete_user(user_id)
        if success:
            # Redirect to the main interface if deletion was successful
            return redirect(url_for('index'))
        else:
            # Render the delete_user.html template with an error message if deletion fails
            error_message = 'User deletion failed. Please try again.'
            return render_template('delete_user.html', error=error_message)
    except Exception as e:
        # Handle potential exceptions gracefully
        error_message = f'An error occurred: {str(e)}'
        return render_template('delete_user.html', error=error_message)

