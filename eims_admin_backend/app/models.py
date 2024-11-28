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


# models for add-services

def get_packages():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT package_id, package_name, package_type, venue, price, capacity, description
            FROM event_packages
            """
        )
        packages = cursor.fetchall()
        # Transform the result into a list of dictionaries
        return [
            {
                'package_id': item[0],
                'package_name': item[1],
                'package_type': item[2],
                'venue': item[3],
                'price': item[4],
                'capacity': item[5],
                'description': item[6],
            }
            for item in packages
        ]
    finally:
        cursor.close()
        conn.close()

def create_package(package_name, package_type, venue, price, capacity, description):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert the package data into the event_packages table
        cursor.execute(
            "INSERT INTO event_packages (package_name, package_type, venue, price, capacity, description) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (package_name, package_type, venue, price, capacity, description)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting package: {e}")  # Log the error message
        return False
    finally:
        cursor.close()
        conn.close()


def update_package(package_id, package_name, package_type, venue, price, capacity, description):
    if not package_id:
        logger.error("Invalid package_id provided")
        return False

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
            UPDATE event_packages
            SET package_name = %s, package_type = %s, venue = %s, price = %s, capacity = %s, description = %s
            WHERE package_id = %s
        """
        cursor.execute(query, (package_name, package_type, venue, price, capacity, description, package_id))
        if cursor.rowcount == 0:
            logger.warning(f"No package found with package_id {package_id}")
            return False
        conn.commit()
        logger.info(f"Package {package_id} updated successfully.")
        return True
    except Exception as e:
        logger.error(f"Error updating package {package_id}: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()


def delete_package(package_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Delete the package from the event_packages table
        cursor.execute("DELETE FROM event_packages WHERE package_id = %s", (package_id,))
        conn.commit()

        # Return True if the package was deleted
        if cursor.rowcount == 0:
            logger.warning(f"No package found with package_id {package_id}")
            return False
        return True
    except Exception as e:
        logger.error(f"Error deleting package {package_id}: {e}")
        conn.rollback()  # Rollback in case of error
        return False
    finally:
        cursor.close()
        conn.close()


#models for create event
def get_user_id_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT userid FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        if user:
            return user[0]
        else:
            logger.warning(f"No user found with email: {email}")
            return None
    except Exception as e:
        logger.error(f"Error retrieving user ID for email {email}: {str(e)}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_all_booked_wishlist():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                e.events_id, 
                e.userid, 
                e.event_name, 
                e.event_type, 
                e.event_theme, 
                e.event_color, 
                e.venue, 
                e.schedule, 
                e.start_time, 
                e.end_time, 
                e.status,
                u.firstname,
                u.lastname,
                u.contactnumber
            FROM events e
            JOIN users u ON e.userid = u.userid
            WHERE e.status = 'Wishlist'  -- Filter for events with 'Wishlist' status
        """)
        
        events = cursor.fetchall()
        if events:
            return [
                {
                    'events_id': item[0],
                    'userid': item[1],
                    'event_name': item[2],
                    'event_type': item[3],
                    'event_theme': item[4],
                    'event_color': item[5],
                    'venue': item[6],
                    'schedule': item[7],
                    'start_time': item[8],
                    'end_time': item[9],
                    'status': item[10],
                    'firstname': item[11],
                    'lastname': item[12],
                    'contactnumber': item[13]
                }
                for item in events
            ]
        else:
            return []  # No events found
    except Exception as e:
        logging.error(f"Error fetching 'Wishlist' events: {e}")
        return []  # Return empty list if there's an error
    finally:
        cursor.close()
        conn.close()

    
def update_event(events_id, event_name, event_type, event_theme, event_color, venue):
    if not events_id:
        logger.error("Invalid events_id provided")
        return False

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
            UPDATE events
            SET event_name = %s, event_type = %s, event_theme = %s, event_color = %s, venue = %s
            WHERE events_id = %s
        """
        cursor.execute(query, (event_name, event_type, event_theme, event_color, venue, events_id))
        if cursor.rowcount == 0:
            logger.warning(f"No event found with events_id {events_id}")
            return False
        conn.commit()
        logger.info(f"Event {events_id} updated successfully.")
        return True
    except Exception as e:
        logger.error(f"Error updating event {events_id}: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()



def get_packages_wedding():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT package_id, package_name, package_type, venue, price, capacity, description
            FROM event_packages
            WHERE package_type = 'Wedding'
            """
        )
        packages = cursor.fetchall()
        # Transform the result into a list of dictionaries
        return [
            {
                'package_id': item[0],
                'package_name': item[1],
                'package_type': item[2],
                'venue': item[3],
                'price': item[4],
                'capacity': item[5],
                'description': item[6],
            }
            for item in packages
        ]
    finally:
        cursor.close()
        conn.close()












