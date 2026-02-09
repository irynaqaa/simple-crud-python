from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(255), nullable=False)
    age: int = Column(Integer, nullable=False)
    email: str = Column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"<Contact {self.id} {self.name}>"


class Student(Base):
    __tablename__ = "students"

    id: int = Column(Integer, primary_key=True)
    nama: str = Column(String(120), nullable=False)
    kelas: str = Column(String(20), nullable=False)
    email: str | None = Column(String(255), nullable=True)

    def __repr__(self) -> str:
        return f"<Student {self.id} {self.nama}>"