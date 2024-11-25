# models.py

import hashlib
from .db import get_db_connection
import logging
from datetime import date


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#admin login
def check_user(email, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    
    try:
        # Fetch the user entry
        cursor.execute("SELECT password, user_type FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        
        # Ensure user exists, password matches, and user_type is allowed
        allowed_user_types = {'admin', 'assistant', 'staff'}
        if user and user[0] == hashed_password and user[1] in allowed_user_types:
            return True, user[1]  # Return True and user_type
        return False, None
    finally:
        cursor.close()
        conn.close()

#manage-users.py / models     

def create_user(first_name, last_name, email, contact_number, password, user_type, country, city, street):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Hash the password before inserting it
        hashed_password = hash_password(password)

        # Use the hashed password in the query
        cursor.execute(
            "INSERT INTO users (firstname, lastname, email, contactnumber, password, user_type, country, city, street) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING userid", 
            (first_name, last_name, email, contact_number, hashed_password, user_type, country, city, street)
        )
        
        # Retrieve the 'userid' of the newly inserted user
        user_id = cursor.fetchone()[0]
        
        # Commit the transaction
        conn.commit()
        
        # Return success flag and the user_id
        return True, user_id  

    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        return False, None
    
    finally:
        cursor.close()
        conn.close()


def create_vendor(userid, service, min_price, max_price):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO vendor (userid, service, min_price, max_price) VALUES (%s, %s, %s, %s)",
            (userid, service, min_price, max_price)
        )
        conn.commit()
        return True
    finally:
        cursor.close()
        conn.close()


def get_users_by_type():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT userid, firstname, lastname, email, contactnumber, user_type
            FROM users
            WHERE user_type IN ('assistant', 'staff')
            """
        )
        users = cursor.fetchall()
        # Transform the result into a list of dictionaries
        return [
            {
                'userid': item[0],
                'firstname': item[1],
                'lastname': item[2],
                'email': item[3],
                'contactnumber': item[4],
                'user_type': item[5],
            }
            for item in users
        ]
    finally:
        cursor.close()
        conn.close()


def get_vendors_with_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT v.vendor_id, v.userid, v.service, v.min_price, v.max_price, 
                   u.firstname, u.lastname, u.email, u.contactnumber
            FROM vendor v
            JOIN users u ON v.userid = u.userid
            """
        )
        vendors = cursor.fetchall()
        # Transform the result into a list of dictionaries
        return [
            {
                'vendor_id': item[0],
                'userid': item[1],
                'service': item[2],
                'min_price': float(item[3]),
                'max_price': float(item[4]),
                'firstname': item[5],
                'lastname': item[6],
                'email': item[7],
                'contactnumber': item[8],
            }
            for item in vendors
        ]
    finally:
        cursor.close()
        conn.close()


def update_staff(userid, firstname, lastname, email, contactnumber, user_type):
    if not userid:
        logger.error("Invalid userid provided")
        return False
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE users 
            SET firstname = %s, lastname = %s, email = %s, contactnumber = %s, user_type = %s 
            WHERE userid = %s
            """,
            (firstname, lastname, email, contactnumber, user_type, userid),
        )
        if cursor.rowcount == 0:
            logger.warning(f"No user found with userid {userid}")
            return False
        conn.commit()
        return True
    except Exception as e:
        logger.error(f"Error updating staff {userid}: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def delete_user(userid):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # First, delete related events (to avoid foreign key violation)
        cursor.execute("DELETE FROM events WHERE userid = %s", (userid,))
        conn.commit()

        # Then delete the user from the users table
        cursor.execute("DELETE FROM users WHERE userid = %s", (userid,))
        conn.commit()

        return True
    except Exception as e:
        logger.error(f"Error deleting user {userid}: {e}")
        conn.rollback()  # Rollback in case of error
        return False
    finally:
        cursor.close()
        conn.close()
