import os
import jwt
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
from application.encryption import Encryption

"""Module to handle authentication."""

class User(BaseModel):
    """Class to represent a user."""
    username: str
    email: str
    full_name: str
    disabled: bool

class Token(BaseModel):
    """Class to represent a token."""
    access_token: str
    token_type: str

pwd_context = CryptContext(schemes=['bcrypt'], default='bcrypt')
SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
security = HTTPBearer()
encryption = Encryption()

# Implement authentication logic here

def verify_password(plain_password, hashed_password):
    """Verify a password."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Get a password hash."""
    return pwd_context.hash(password)

def authenticate_user(fake_db, username: str, password: str):
    """Authenticate a user."""
    user = fake_db.get(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create an access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: HTTPAuthorizationCredentials = Depends(security)):
    """Get the current user."""
    credentials_exception = HTTPException(
        status_code=401,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = Token(access_token=token.credentials, token_type='bearer')
    except jwt.PyJWTError:
        raise credentials_exception
    user = fake_db.get(username)
    if user is None:
        raise credentials_exception
    return user
