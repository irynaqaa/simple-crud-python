from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import re

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email
        }

    @staticmethod
    def validate_email(email: str) -> bool:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    @staticmethod
    def validate_user_data(name: str, age: int, email: str) -> bool:
        return bool(name) and age > 0 and User.validate_email(email)

    def __repr__(self):
        return f'<User {self.name}, Email: {self.email}>'

    @classmethod
    def delete_user(cls, user_id: int):
        user = cls.query.get(user_id)
        if user:
            db.session.delete(user)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                return False
            return True
        return False

DB_HOST = 'your_db_host'
DB_USER = 'your_db_user'
DB_PASS = 'your_db_password'
DB_NAME = 'your_db_name'