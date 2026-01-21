from . import db


class Student(db.Model):
    __tablename__ = 'datasiswa'

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(255), nullable=False)
    kelas = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Student id={self.id} nama={self.nama} kelas={self.kelas}>"


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<User {self.id}>"


__all__ = ['Student', 'User']