from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False, unique=True)

    def __repr__(self):
        return f"<User(name='{self.name}', age='{self.age}', email='{self.email}')>"

    @staticmethod
    def add_user(session, name, age, email):
        new_user = User(name=name, age=age, email=email)
        session.add(new_user)
        session.commit()

# Database engine creation
engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)

# Session factory
Session = sessionmaker(bind=engine)
