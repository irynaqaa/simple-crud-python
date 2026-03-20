from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_wtf.csrf import CSRFProtect
import os
from typing import Dict, Any

app = Flask(__name__)

# Configuration
DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://user:password@localhost/dbname')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')

# Initialize SQLAlchemy and CSRF protection
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

# Error Handling
@app.errorhandler(SQLAlchemyError)
def handle_database_error(error: SQLAlchemyError) -> Dict[str, Any]:
    db.session.rollback()
    return jsonify({"error": str(error)}), 500

@app.errorhandler(400)
def handle_bad_request(error: Exception) -> Dict[str, Any]:
    return jsonify({"error": "Bad Request"}), 400

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)

# Routes
@app.route('/submit', methods=['POST'])
@csrf.exempt
def submit_form() -> Dict[str, Any]:
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return handle_bad_request(400)

    new_user = User(username=data['username'], email=data['email'])
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except SQLAlchemyError as e:
        return handle_database_error(e)

if __name__ == '__main__':
    app.run(debug=True)