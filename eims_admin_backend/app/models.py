# models.py

import hashlib
from .db import get_db_connection
import logging
from datetime import date


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_user(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    
    try:
        cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        return user and user[0] == hashed_password
    finally:
        cursor.close()
        conn.close()

def create_user(first_name, last_name, email, address, contact_number, password, user_type='client'):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    
    try:
        # Check if email exists
        cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
        if cursor.fetchone():
            return False  # Email exists
        
        # Insert new user
        cursor.execute(
            "INSERT INTO users (firstname, lastname, email, address, contactnumber, password, user_type) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (first_name, last_name, email, address, contact_number, hashed_password, user_type)
        )
        conn.commit()
        return True
    finally:
        cursor.close()
        conn.close()