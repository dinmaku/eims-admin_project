# models.py
import hashlib
from .db import get_db_connection
import logging
from datetime import date, time
import json


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
        allowed_user_types = {'Admin', 'Assistant', 'Staff'}
        if user and user[0] == hashed_password and user[1] in allowed_user_types:
            return True, user[1]  # Return True and user_type
        return False, None
    finally:
        cursor.close()
        conn.close()

#manage-users.py / models     

def create_user(first_name, last_name, username, email, contact_number, password, user_type, address):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Check if email already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE email = %s", (email,))
        if cursor.fetchone()[0] > 0:
            logger.info(f"Duplicate email found: {email}")
            return False, None, "Email already exists"

        # Check if username already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        if cursor.fetchone()[0] > 0:
            logger.info(f"Duplicate username found: {username}")
            return False, None, "Username already exists"

        # Hash the password before inserting it
        hashed_password = hash_password(password)

        # Use the hashed password in the query with correct column names
        cursor.execute(
            "INSERT INTO users (firstname, lastname, username, email, contactnumber, password, user_type, address) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING userid", 
            (first_name, last_name, username, email, contact_number, hashed_password, user_type, address)
        )
        
        # Retrieve the 'userid' of the newly inserted user
        user_id = cursor.fetchone()[0]
        
        # Commit the transaction
        conn.commit()
        
        # Return success flag, user_id, and no error message
        return True, user_id, None

    except Exception as e:
        logger.error(f"Error creating user: {str(e)}")
        conn.rollback()
        return False, None, str(e)
    
    finally:
        cursor.close()
        conn.close()


def create_supplier(userid, service, price):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO suppliers (userid, service, price, status) VALUES (%s, %s, %s, %s)",
            (userid, service, price, 'Active')
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
            WHERE user_type IN ('Assistant', 'Staff')
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

def get_admin_users():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT userid, firstname, lastname, email, contactnumber, user_type
            FROM users
            WHERE user_type IN ('Admin')
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


def get_suppliers_with_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT s.supplier_id, u.firstname, u.lastname, u.email, u.contactnumber, 
                   u.username, u.password, s.service, s.price, s.status, u.userid
            FROM suppliers s
            JOIN users u ON s.userid = u.userid
            WHERE s.status = 'Active'
            ORDER BY s.supplier_id
        """)
        suppliers = cursor.fetchall()
        
        # Convert to list of dictionaries
        suppliers_list = []
        for supplier in suppliers:
            suppliers_list.append({
                'supplier_id': supplier[0],
                'firstname': supplier[1],
                'lastname': supplier[2],
                'email': supplier[3],
                'contactnumber': supplier[4],
                'username': supplier[5],
                'password': supplier[6],
                'service': supplier[7],
                'price': float(supplier[8]) if supplier[8] else 0,
                'status': supplier[9],
                'userid': supplier[10]
            })
        return suppliers_list
    finally:
        cursor.close()
        conn.close()


def get_package_services_with_suppliers():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Query to fetch package service details and associated supplier info
        cursor.execute(
            """
            SELECT ps.package_service_id, ps.supplier_id, ps.external_supplier_name, 
                   ps.external_supplier_contact, ps.external_supplier_price, ps.remarks
            FROM package_service ps
            """
        )
        package_services = cursor.fetchall()

        # Map the query result into a structured dictionary
        return [
            {
                'package_service_id': item[0],
                'supplier_id': item[1],
                'external_supplier_name': item[2],
                'external_supplier_contact': item[3],
                'external_supplier_price': float(item[4]) if item[4] is not None else 0.0,
                'remarks': item[5],
            }
            for item in package_services
        ]
    except Exception as e:
        # Log the exception if needed
        print(f"Error fetching package services: {e}")
        return []
    finally:
        cursor.close()
        conn.close()





def update_suppliers_and_user(
    supplier_id, service, price, 
    userid, firstname, lastname, email, contactnumber, username, password
):
    if not supplier_id or not userid:
        logger.error("Invalid supplier_id or userid provided")
        return False

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Hash the password before updating it
        hashed_password = hash_password(password)

        # Update the `suppliers` table
        cursor.execute(
            """
            UPDATE suppliers
            SET service = %s, price = %s
            WHERE supplier_id = %s
            """,
            (service, price, supplier_id),
        )
        if cursor.rowcount == 0:
            logger.warning(f"No supplier found with supplier_id {supplier_id}")
            return False

        # Update the `users` table
        cursor.execute(
            """
            UPDATE users
            SET firstname = %s, lastname = %s, email = %s, 
                contactnumber = %s, username = %s, password = %s
            WHERE userid = %s
            """,
            (firstname, lastname, email, contactnumber, username, hashed_password, userid),
        )
        if cursor.rowcount == 0:
            logger.warning(f"No user found with userid {userid}")
            return False

        # Commit the transaction if both updates are successful
        conn.commit()
        return True
    except Exception as e:
        logger.error(f"Error updating supplier and user: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()




def update_staff(userid, first_name, last_name, email, contact_number, user_type):
    if not userid:
        logger.error("Invalid userid provided")
        return False
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE users 
            SET first_name = %s, last_name = %s, email = %s, contact_number = %s, user_type = %s 
            WHERE userid = %s
            """,
            (first_name, last_name, email, contact_number, user_type, userid),
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

        # Return True if the package was deleted
        if cursor.rowcount == 0:
            logger.warning(f"No user found with userid {userid}")
            return False
        
        logger.info(f"User with userid {userid} deleted successfully.")
        return True
    except Exception as e:
        logger.error(f"Error deleting user {userid}: {e}")
        conn.rollback()  # Rollback in case of error
        return False
    finally:
        cursor.close()
        conn.close()



#models for add-services

def get_packages():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Get basic package information with event type
        cursor.execute("""
            SELECT 
                p.package_id,
                p.package_name,
                et.event_type_name,
                p.event_type_id,
                p.capacity,
                p.description,
                p.venue_id,
                v.venue_name,
                p.gown_package_id,
                gp.gown_package_name,
                p.additional_capacity_charges,
                p.charge_unit,
                p.total_price,
                p.created_at,
                p.status
            FROM event_packages p
            LEFT JOIN venues v ON p.venue_id = v.venue_id
            LEFT JOIN gown_package gp ON p.gown_package_id = gp.gown_package_id
            LEFT JOIN event_type et ON p.event_type_id = et.event_type_id
            ORDER BY p.created_at DESC
        """)
        rows = cursor.fetchall()
        
        # Convert rows to dictionaries
        packages = []
        for row in rows:
            package = {
                'package_id': row[0],
                'package_name': row[1],
                'event_type_name': row[2],
                'event_type_id': row[3],
                'capacity': row[4],
                'description': row[5],
                'venue_id': row[6],
                'venue_name': row[7],
                'gown_package_id': row[8],
                'gown_package_name': row[9],
                'additional_capacity_charges': float(row[10]) if row[10] else 0,
                'charge_unit': row[11],
                'total_price': float(row[12]) if row[12] else 0,
                'created_at': row[13].strftime('%Y-%m-%d') if row[13] else None,
                'status': row[14]
            }
            
            # Get suppliers for this package
            cursor.execute("""
                SELECT 
                    s.supplier_id,
                    u.firstname,
                    u.lastname,
                    s.service,
                    s.price,
                    ps.remarks
                FROM event_package_services eps
                JOIN package_service ps ON eps.package_service_id = ps.package_service_id
                JOIN suppliers s ON ps.supplier_id = s.supplier_id
                JOIN users u ON s.userid = u.userid
                WHERE eps.package_id = %s
            """, (row[0],))  # Use row[0] for package_id
            
            package['suppliers'] = []
            supplier_rows = cursor.fetchall()
            for supplier_row in supplier_rows:
                package['suppliers'].append({
                    'supplier_id': supplier_row[0],
                    'name': f"{supplier_row[1]} {supplier_row[2]}",
                    'service': supplier_row[3],
                    'price': float(supplier_row[4]) if supplier_row[4] else 0,
                    'remarks': supplier_row[5]
                })
                
            # Get additional services for this package
            cursor.execute("""
                SELECT 
                    a.add_service_id,
                    a.add_service_name,
                    a.add_service_price
                FROM event_package_additional_services epas
                JOIN additional_services a ON epas.add_service_id = a.add_service_id
                WHERE epas.package_id = %s
            """, (row[0],))  # Use row[0] for package_id
            
            package['additional_services'] = []
            service_rows = cursor.fetchall()
            for service_row in service_rows:
                package['additional_services'].append({
                    'service_id': service_row[0],
                    'name': service_row[1],
                    'price': float(service_row[2]) if service_row[2] else 0
                })
            
            packages.append(package)
        
        return packages
    except Exception as e:
        print(f"Error fetching packages: {e}")
        raise e
    finally:
        cursor.close()
        conn.close()

def create_package(package_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        print("Received data:", package_data)
        
        # Insert into event_packages first
        cursor.execute("""
            INSERT INTO event_packages (
                package_name, event_type_id, venue_id, capacity,
                additional_capacity_charges, charge_unit, description,
                gown_package_id, total_price
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s
            ) RETURNING package_id
        """, (
            package_data['package_name'],
            package_data['event_type_id'],
            package_data['venue_id'],
            package_data['capacity'],
            package_data['additional_capacity_charges'],
            package_data['charge_unit'],
            package_data['description'],
            package_data['gown_package_id'],
            package_data['total_price']
        ))
        
        package_id = cursor.fetchone()[0]
        print(f"Package ID: {package_id}")
        
        # Handle suppliers through package_service table
        for supplier in package_data['suppliers']:
            # First create entry in package_service
            cursor.execute("""
                INSERT INTO package_service (
                    supplier_id, remarks
                ) VALUES (
                    %s, %s
                ) RETURNING package_service_id
            """, (
                supplier['supplier_id'],
                supplier['remarks']
            ))
            package_service_id = cursor.fetchone()[0]
            
            # Then link it in event_package_services
            cursor.execute("""
                INSERT INTO event_package_services (
                    package_id, package_service_id
                ) VALUES (
                    %s, %s
                )
            """, (
                package_id,
                package_service_id
            ))
        
        # Handle additional services
        if 'additional_services' in package_data:
            for service in package_data['additional_services']:
                cursor.execute("""
                    INSERT INTO event_package_additional_services (
                        package_id, add_service_id
                    ) VALUES (
                        %s, %s
                    )
                """, (
                    package_id,
                    service['add_service_id']
                ))
        
        conn.commit()
        return package_id
        
    except Exception as e:
        conn.rollback()
        print(f"Error creating package: {e}")
        raise e
    finally:
        cursor.close()
        conn.close()

def calculate_total_price(package_id, cursor):
    """Calculate the total price of a package including all services."""
    total_price = 0

    # Get supplier prices
    cursor.execute(
        """
        SELECT COALESCE(SUM(s.price), 0)
        FROM event_package_services eps
        JOIN package_service ps ON eps.package_service_id = ps.package_service_id
        JOIN suppliers s ON ps.supplier_id = s.supplier_id
        WHERE eps.package_id = %s
        """,
        (package_id,)
    )
    supplier_price = cursor.fetchone()[0]
    total_price += supplier_price

    # Get external supplier prices
    cursor.execute(
        """
        SELECT COALESCE(SUM(ps.external_supplier_price), 0)
        FROM event_package_services eps
        JOIN package_service ps ON eps.package_service_id = ps.package_service_id
        WHERE eps.package_id = %s AND ps.external_supplier_price IS NOT NULL
        """,
        (package_id,)
    )
    external_price = cursor.fetchone()[0]
    total_price += external_price

    # Get additional services prices
    cursor.execute(
        """
        SELECT COALESCE(SUM(ads.add_service_price), 0)
        FROM event_package_additional_services pas
        JOIN additional_services ads ON pas.add_service_id = ads.add_service_id
        WHERE pas.package_id = %s
        """,
        (package_id,)
    )
    additional_services_price = cursor.fetchone()[0]
    total_price += additional_services_price

    return total_price

def calculate_gown_package_price(gown_package_id, cursor):
    cursor.execute(
        """
        SELECT COALESCE(SUM(o.rent_price), 0)
        FROM gown_package_outfits gpo
        JOIN outfits o ON gpo.outfit_id = o.outfit_id
        WHERE gpo.gown_package_id = %s
        """, (gown_package_id,)
    )
    result = cursor.fetchone()
    logging.info(f"Calculated price for gown_package_id {gown_package_id}: {result[0]}")
    return result[0] if result[0] is not None else 0.00

def update_gown_package_price(gown_package_id, cursor):
    gown_package_price = calculate_gown_package_price(gown_package_id, cursor)
    cursor.execute(
        """
        UPDATE gown_package
        SET gown_package_price = %s
        WHERE gown_package_id = %s
        """, (gown_package_price, gown_package_id)
    )
    logging.info(f"Updated price for gown_package_id {gown_package_id} to {gown_package_price}")





def update_package(package_id, package_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("BEGIN")

        # Update basic package information
        cursor.execute("""
            UPDATE event_packages 
            SET package_name = %s,
                capacity = %s,
                description = %s
            WHERE package_id = %s
            RETURNING package_id
        """, (
            package_data['package_name'],
            package_data['capacity'],
            package_data['description'],
            package_id
        ))

        if cursor.rowcount == 0:
            cursor.execute("ROLLBACK")
            return False

        # Clear existing inclusions
        cursor.execute("DELETE FROM event_package_services WHERE package_id = %s", (package_id,))
        cursor.execute("DELETE FROM event_package_additional_services WHERE package_id = %s", (package_id,))

        total_price = 0

        # Process new inclusions
        for inclusion in package_data['inclusions']:
            if inclusion['type'] == 'supplier':
                # Add supplier
                if 'supplier_id' in inclusion['data']:
                    # Internal supplier
                    cursor.execute("""
                        INSERT INTO package_service (supplier_id, remarks)
                        VALUES (%s, %s)
                        RETURNING package_service_id
                    """, (inclusion['data']['supplier_id'], inclusion.get('remarks', '')))
                else:
                    # External supplier
                    cursor.execute("""
                        INSERT INTO package_service (
                            external_supplier_name,
                            external_supplier_contact,
                            external_supplier_price,
                            remarks
                        )
                        VALUES (%s, %s, %s, %s)
                        RETURNING package_service_id
                    """, (
                        inclusion['data']['external_supplier_name'],
                        inclusion['data']['external_supplier_contact'],
                        inclusion['data']['external_supplier_price'],
                        inclusion.get('remarks', '')
                    ))
                
                package_service_id = cursor.fetchone()[0]
                cursor.execute("""
                    INSERT INTO event_package_services (package_id, package_service_id)
                    VALUES (%s, %s)
                """, (package_id, package_service_id))
                
                total_price += float(inclusion['data'].get('price', 0))

            elif inclusion['type'] == 'venue':
                # Update venue
                cursor.execute("""
                    UPDATE event_packages
                    SET venue_id = %s
                    WHERE package_id = %s
                """, (inclusion['data']['selectVenueId'], package_id))
                
                total_price += float(inclusion['data'].get('price', 0))

            elif inclusion['type'] == 'outfit':
                # Update outfit package
                cursor.execute("""
                    UPDATE event_packages
                    SET gown_package_id = %s
                    WHERE package_id = %s
                """, (inclusion['data']['gown_package_id'], package_id))
                
                total_price += float(inclusion['data'].get('price', 0))

            elif inclusion['type'] == 'service':
                # Add additional service
                cursor.execute("""
                    INSERT INTO event_package_additional_services (package_id, add_service_id)
                    VALUES (%s, %s)
                """, (package_id, inclusion['data']['add_service_id']))
                
                total_price += float(inclusion['data'].get('price', 0))

        # Update total price
        cursor.execute("""
            UPDATE event_packages
            SET total_price = %s
            WHERE package_id = %s
        """, (total_price, package_id))

        cursor.execute("COMMIT")
        return True

    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error updating package: {e}")
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
        
        logger.info(f"Package with package_id {package_id} deleted successfully.")
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
        # Comprehensive query to fetch all event details with related package and additional data
        cursor.execute("""
            WITH event_details AS (
                SELECT 
                    e.events_id, 
                    e.userid, 
                    e.event_name, 
                    e.event_type, 
                    e.event_theme, 
                    e.event_color, 
                    e.schedule::text as schedule, 
                    e.start_time::text as start_time, 
                    e.end_time::text as end_time, 
                    e.status,
                    e.onsite_firstname,
                    e.onsite_lastname,
                    e.onsite_contact,
                    e.onsite_address,
                    ep.package_id, 
                    ep.package_name, 
                    et.event_type_name AS package_type, 
                    ep.capacity, 
                    ep.description AS package_description,
                    ep.total_price,
                    ep.additional_capacity_charges,
                    ep.charge_unit,
                    v.venue_id, 
                    v.venue_name, 
                    v.location AS venue_location,
                    v.venue_price,
                    gp.gown_package_id, 
                    gp.gown_package_name, 
                    gp.gown_package_price,
                    u.firstname AS firstname, 
                    u.lastname AS lastname, 
                    u.contactnumber AS contactnumber,
                    u.email AS email
                FROM 
                    events e
                LEFT JOIN users u ON e.userid = u.userid
                LEFT JOIN event_packages ep ON e.package_id = ep.package_id
                LEFT JOIN event_type et ON ep.event_type_id = et.event_type_id
                LEFT JOIN venues v ON ep.venue_id = v.venue_id
                LEFT JOIN gown_package gp ON ep.gown_package_id = gp.gown_package_id
                WHERE 
                    e.status = 'Wishlist'
            ),
            suppliers AS (
                SELECT 
                    ep.package_id, 
                    json_agg(
                        json_build_object(
                            'supplier_id', s.supplier_id,
                            'service', s.service,
                            'price', s.price,
                            'supplier_firstname', u.firstname,
                            'supplier_lastname', u.lastname,
                            'supplier_email', u.email,
                            'external_supplier_name', ps.external_supplier_name,
                            'external_supplier_contact', ps.external_supplier_contact,
                            'external_supplier_price', ps.external_supplier_price,
                            'remarks', ps.remarks
                        )
                    ) FILTER (WHERE s.supplier_id IS NOT NULL OR ps.external_supplier_name IS NOT NULL) AS suppliers
                FROM 
                    event_packages ep
                LEFT JOIN 
                    event_package_services eps ON ep.package_id = eps.package_id
                LEFT JOIN 
                    package_service ps ON eps.package_service_id = ps.package_service_id
                LEFT JOIN 
                    suppliers s ON ps.supplier_id = s.supplier_id
                LEFT JOIN 
                    users u ON s.userid = u.userid
                GROUP BY 
                    ep.package_id
            ),
            event_venues AS (
                SELECT 
                    e.events_id,
                    json_agg(
                        json_build_object(
                            'venue_id', v.venue_id,
                            'venue_name', v.venue_name,
                            'location', v.location,
                            'venue_price', v.venue_price,
                            'venue_capacity', v.venue_capacity,
                            'description', v.description
                        )
                    ) FILTER (WHERE v.venue_id IS NOT NULL) AS venues
                FROM 
                    events e
                LEFT JOIN 
                    event_venues ev ON e.events_id = ev.events_id
                LEFT JOIN 
                    venues v ON ev.venue_id = v.venue_id
                WHERE 
                    e.status = 'Wishlist'
                GROUP BY 
                    e.events_id
            ),
            package_additional_services AS (
                SELECT 
                    ep.package_id, 
                    json_agg(
                        json_build_object(
                            'add_service_id', ads.add_service_id,
                            'add_service_name', ads.add_service_name,
                            'add_service_description', ads.add_service_description,
                            'add_service_price', ads.add_service_price
                        )
                    ) FILTER (WHERE ads.add_service_id IS NOT NULL) AS additional_services
                FROM 
                    event_packages ep
                LEFT JOIN 
                    event_package_additional_services epas ON ep.package_id = epas.package_id
                LEFT JOIN 
                    additional_services ads ON epas.add_service_id = ads.add_service_id
                GROUP BY 
                    ep.package_id
            )
            SELECT 
                ed.*,
                COALESCE(ev.venues, '[]'::json) AS venues,
                COALESCE(s.suppliers, '[]'::json) AS suppliers,
                COALESCE(pas.additional_services, '[]'::json) AS additional_services
            FROM 
                event_details ed
            LEFT JOIN 
                event_venues ev ON ed.events_id = ev.events_id
            LEFT JOIN 
                suppliers s ON ed.package_id = s.package_id
            LEFT JOIN 
                package_additional_services pas ON ed.package_id = pas.package_id
        """)
        
        # Fetch results
        results = cursor.fetchall()
        
        # Get column names
        columns = [desc[0] for desc in cursor.description]
        
        # Convert to list of dicts
        wishlist = []
        for row in results:
            item = dict(zip(columns, row))
            wishlist.append(item)
            
        return wishlist
    except Exception as e:
        logging.error(f"Error in get_all_booked_wishlist: {str(e)}")
        raise e
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


#models for venues

def create_venue(venue_name, location, description, venue_capacity):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO venues (venue_name, location, description, venue_capacity, venue_price, status) VALUES (%s, %s, %s, %s, %s, %s)",
            (venue_name, location, description, venue_capacity, 0, 'Active')
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error in create_venue: {str(e)}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

# Function to fetch all venues from the venues table
def get_all_venues():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT venue_id, venue_name, location, venue_price, 
                   venue_capacity, description, status 
            FROM venues 
            WHERE status = 'Active'
        """)
        venues = cursor.fetchall()

        # Transform the result into a list of dictionaries
        return [
            {
                'venue_id': item[0],
                'venue_name': item[1],
                'location': item[2],
                'venue_price': item[3],
                'venue_capacity': item[4],
                'description': item[5],
                'status': item[6]
            }
            for item in venues
        ]
    finally:
        cursor.close()
        conn.close()

def delete_venue(venue_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Start a transaction and delete from event_packages first to avoid foreign key issues
        cursor.execute("DELETE FROM event_packages WHERE venue_id = %s", (venue_id,))
        conn.commit()

        cursor.execute("DELETE FROM venues WHERE venue_id = %s", (venue_id,))
        conn.commit()

        # Check if any rows were affected
        if cursor.rowcount == 0:
            logger.warning(f"No venue found with venue_id {venue_id}")
            return False
        
        logger.info(f"Venue with venue_id {venue_id} deleted successfully.")
        return True
    except Exception as e:
        logger.error(f"Error deleting venue {venue_id}: {e}")
        conn.rollback()  # Rollback in case of error
        return False
    finally:
        cursor.close()
        conn.close()


def update_venue(venue_id, venue_name, location, venue_price, venue_capacity, description):
    """
    Updates a venue's details in the database.

    Args:
        venue_id (int): The ID of the venue to update.
        venue_name (str): The new name for the venue.
        location (str): The new location of the venue.
        venue_price (float): The new price for the venue.
        venue_capacity (int): The new capacity for the venue.
        description (str): The new description for the venue.

    Returns:
        bool: True if the update is successful, False otherwise.
    """
    if not venue_id:
        logger.error("Invalid venue_id provided")
        return False

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
            UPDATE venues
            SET venue_name = %s, location = %s, venue_price = %s, venue_capacity = %s, description = %s
            WHERE venue_id = %s
        """
        cursor.execute(query, (venue_name, location, venue_price, venue_capacity, description, venue_id))
        if cursor.rowcount == 0:
            logger.warning(f"No venue found with venue_id {venue_id}")
            return False
        conn.commit()
        logger.info(f"Venue {venue_id} updated successfully.")
        return True
    except Exception as e:
        logger.error(f"Error updating venue {venue_id}: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def get_active_venues():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT venue_id, venue_name, location, venue_price, description, venue_capacity, status
            FROM venues
            WHERE status = 'Active'
            ORDER BY venue_id
        """)
        venues = cursor.fetchall()
        
        venues_list = []
        for venue in venues:
            venues_list.append({
                'venue_id': venue[0],
                'venue_name': venue[1],
                'location': venue[2],
                'venue_price': float(venue[3]) if venue[3] else 0,
                'description': venue[4],
                'venue_capacity': venue[5],
                'status': venue[6]
            })
        return venues_list
    finally:
        cursor.close()
        conn.close()

def get_inactive_venues():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT venue_id, venue_name, location, venue_price, description, venue_capacity, status
            FROM venues
            WHERE status = 'Inactive'
            ORDER BY venue_id
        """)
        venues = cursor.fetchall()
        
        venues_list = []
        for venue in venues:
            venues_list.append({
                'venue_id': venue[0],
                'venue_name': venue[1],
                'location': venue[2],
                'venue_price': float(venue[3]) if venue[3] else 0,
                'description': venue[4],
                'venue_capacity': venue[5],
                'status': venue[6]
            })
        return venues_list
    finally:
        cursor.close()
        conn.close()

def toggle_venue_status(venue_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # First get current status
        cursor.execute("SELECT status FROM venues WHERE venue_id = %s", (venue_id,))
        current_status = cursor.fetchone()
        
        if not current_status:
            return False, "Venue not found"
            
        # Toggle the status
        new_status = 'Inactive' if current_status[0] == 'Active' else 'Active'
        
        cursor.execute(
            "UPDATE venues SET status = %s WHERE venue_id = %s",
            (new_status, venue_id)
        )
        conn.commit()
        return True, new_status
    except Exception as e:
        conn.rollback()
        return False, str(e)
    finally:
        cursor.close()
        conn.close()

def update_venue_price(venue_id, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE venues SET venue_price = %s WHERE venue_id = %s",
            (price, venue_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating venue price: {str(e)}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

#gown package models
def get_gown_packages():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT gown_package_id, gown_package_name, description, gown_package_price, status
            FROM gown_package
            WHERE status = 'Active'
            ORDER BY gown_package_id
        """)
        packages = cursor.fetchall()
        return [
            {
                'gown_package_id': package[0],
                'gown_package_name': package[1],
                'description': package[2],
                'gown_package_price': float(package[3]) if package[3] else 0,
                'status': package[4]
            }
            for package in packages
        ]
    finally:
        cursor.close()
        conn.close()

def get_inactive_packages():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        logger.info("Executing query to fetch inactive gown packages")
        cursor.execute("""
            SELECT gown_package_id, gown_package_name, description, gown_package_price, status
            FROM gown_package
            WHERE status = 'Inactive' OR status IS NULL
            ORDER BY gown_package_id
        """)
        packages = cursor.fetchall()
        logger.info(f"Found {len(packages)} inactive packages")
        
        result = [
            {
                'gown_package_id': package[0],
                'gown_package_name': package[1],
                'description': package[2],
                'gown_package_price': float(package[3]) if package[3] else 0,
                'status': package[4] or 'Active'  # Default to Active if NULL
            }
            for package in packages
        ]
        logger.info("Successfully processed package data")
        return result
    except Exception as e:
        logger.error(f"Error fetching inactive packages: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def toggle_package_status(package_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # First get the current status
        cursor.execute("SELECT status FROM gown_package WHERE gown_package_id = %s", (package_id,))
        result = cursor.fetchone()
        if not result:
            logger.error(f"No package found with id {package_id}")
            return False
            
        current_status = result[0] or 'Active'  # Default to Active if None
        logger.info(f"Current status for package {package_id}: {current_status}")
        
        # Toggle the status
        new_status = 'Inactive' if current_status == 'Active' else 'Active'
        logger.info(f"New status will be: {new_status}")
        
        cursor.execute("""
            UPDATE gown_package 
            SET status = %s 
            WHERE gown_package_id = %s
        """, (new_status, package_id))
        
        conn.commit()
        logger.info(f"Successfully updated package {package_id} status to {new_status}")
        return True
    except Exception as e:
        conn.rollback()
        logger.error(f"Error toggling package status: {str(e)}")
        return False
    finally:
        cursor.close()
        conn.close()

def get_all_gown_packages():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT gown_package_id, gown_package_name, gown_package_price, description FROM gown_package")
        gown_packages = cursor.fetchall()

        # Transform the result into a list of dictionaries
        return [
            {
                'gown_package_id': item[0],
                'gown_package_name': item[1],
                'gown_package_price': item[2],
                'description': item[3]

            }
            for item in gown_packages
        ]
    finally:
        cursor.close()
        conn.close()



def add_gown_package(gown_package_name, description, outfits):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert gown package
        cursor.execute("""
            INSERT INTO gown_package (gown_package_name, description)
            VALUES (%s, %s) RETURNING gown_package_id
        """, (gown_package_name, description))
        
        gown_package_id = cursor.fetchone()[0]

        # Insert outfits associated with the gown package
        for outfit_id in outfits:
            cursor.execute("""
                INSERT INTO gown_package_outfits (gown_package_id, outfit_id)
                VALUES (%s, %s)
            """, (gown_package_id, outfit_id))

        # Update gown package price based on outfits
        update_gown_package_price(gown_package_id, cursor)
        
        # Commit transaction
        conn.commit()

        return gown_package_id
    except Exception as e:
        conn.rollback()
        logging.error(f"Error adding gown package: {e}")
        raise e
    finally:
        cursor.close()
        conn.close()



def get_all_outfits():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT outfit_id, outfit_name, outfit_type, outfit_color, outfit_desc, rent_price, status, outfit_img, size, weight FROM outfits")
        outfits = cursor.fetchall()

        # Transform the result into a list of dictionaries
        return [
            {
                'outfit_id': item[0],
                'outfit_name': item[1],
                'outfit_type': item[2],
                'outfit_color': item[3],
                'outfit_desc': item[4],
                'rent_price': item[5],
                'status': item[6],
                'outfit_img': item[7],
                'size': item[8],
                'weight': item[9]
            }
            for item in outfits
        ]
    finally:
        cursor.close()
        conn.close()

def create_outfit(outfit_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Insert outfit data
        cursor.execute("""
            INSERT INTO outfits (outfit_name, outfit_type, outfit_color, outfit_desc, 
                               rent_price, status, outfit_img, size, weight)
            VALUES (%(outfit_name)s, %(outfit_type)s, %(outfit_color)s, %(outfit_desc)s,
                    %(rent_price)s, %(status)s, %(outfit_img)s, %(size)s, %(weight)s)
            RETURNING outfit_id
        """, {
            'outfit_name': outfit_data.get('outfit_name'),
            'outfit_type': outfit_data.get('outfit_type'),
            'outfit_color': outfit_data.get('outfit_color'),
            'outfit_desc': outfit_data.get('outfit_desc'),
            'rent_price': float(outfit_data.get('rent_price', 0)),
            'status': 'Available',  # Default status
            'outfit_img': outfit_data.get('outfit_img'),
            'size': outfit_data.get('size'),
            'weight': float(outfit_data.get('weight', 0))
        })
        
        outfit_id = cursor.fetchone()[0]
        
        # Create archive entry
        archive_data = outfit_data.get('archive', {})
        cursor.execute("""
            INSERT INTO outfit_archive (outfit_id, creation_address, creation_date,
                                      owner, retail_price, usage)
            VALUES (%s, %s, CURRENT_DATE, %s, %s, 0)
        """, (
            outfit_id,
            archive_data.get('creation_address'),
            archive_data.get('owner'),
            float(archive_data.get('retail_price', 0)) if archive_data.get('retail_price') else 0
        ))
        
        conn.commit()
        return True, outfit_id, "Outfit created successfully"
        
    except Exception as e:
        conn.rollback()
        logger.error(f"Error creating outfit: {str(e)}")
        return False, None, str(e)
    finally:
        cursor.close()
        conn.close()

#additional services models
def create_additional_service(add_service_name, add_service_description):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO additional_services (add_service_name, add_service_description, add_service_price, status) VALUES (%s, %s, %s, %s)",
            (add_service_name, add_service_description, 0, 'Active')
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error creating additional service: {str(e)}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def update_additional_service_price(service_id, price):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE additional_services SET add_service_price = %s WHERE add_service_id = %s",
            (price, service_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating additional service price: {str(e)}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def get_active_additional_services():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT add_service_id, add_service_name, add_service_description, 
                   add_service_price, status 
            FROM additional_services 
            WHERE status = 'Active' 
            ORDER BY add_service_id
        """)
        services = cursor.fetchall()
        return [
            {
                'add_service_id': service[0],
                'add_service_name': service[1],
                'add_service_description': service[2],
                'add_service_price': float(service[3]),
                'status': service[4]
            }
            for service in services
        ]
    except Exception:
        return []
    finally:
        cursor.close()
        conn.close()

def get_inactive_additional_services():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM additional_services WHERE status = 'Inactive' ORDER BY add_service_id"
        )
        services = cursor.fetchall()
        return [
            {
                'add_service_id': service[0],
                'add_service_name': service[1],
                'add_service_description': service[2],
                'add_service_price': float(service[3]),
                'status': service[4]
            }
            for service in services
        ]
    except Exception as e:
        print(f"Error getting inactive additional services: {str(e)}")
        return []
    finally:
        cursor.close()
        conn.close()

def toggle_additional_service_status(service_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE additional_services SET status = CASE WHEN status = 'Active' THEN 'Inactive' ELSE 'Active' END WHERE add_service_id = %s",
            (service_id,)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error toggling additional service status: {str(e)}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

# Function to fetch all additional services from the additional_services table
def get_all_additional_services():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT add_service_id, add_service_name, add_service_description, 
                   add_service_price, status 
            FROM additional_services 
            WHERE status = 'Active'
        """)
        services = cursor.fetchall()

        # Transform the result into a list of dictionaries
        return [
            {
                'add_service_id': item[0],
                'add_service_name': item[1],
                'add_service_description': item[2],
                'add_service_price': item[3],
                'status': item[4]
            }
            for item in services
        ]
    finally:
        cursor.close()
        conn.close()

def update_additional_service(add_service_id, add_service_name, add_service_description, add_service_price):
    if not add_service_id:
        logger.error("Invalid add_service_id provided")
        return False

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        query = """
            UPDATE additional_services
            SET add_service_name = %s, add_service_description = %s, add_service_price = %s
            WHERE add_service_id = %s
        """
        cursor.execute(query, (add_service_name, add_service_description, add_service_price, add_service_id))
        if cursor.rowcount == 0:
            logger.warning(f"No additional service found with add_service_id {add_service_id}")
            return False
        conn.commit()
        logger.info(f"Additional service {add_service_id} updated successfully.")
        return True
    except Exception as e:
        logger.error(f"Error updating additional service {add_service_id}: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def get_event_types():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT event_type_id, event_type_name 
            FROM event_type 
            ORDER BY event_type_name
        """)
        rows = cursor.fetchall()
        event_types = [
            {
                'event_type_id': row[0],
                'event_type_name': row[1]
            }
            for row in rows
        ]
        return event_types
    except Exception as e:
        print(f"Error fetching event types: {e}")
        raise e
    finally:
        cursor.close()
        conn.close()

def initialize_event_types():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # First check if we already have event types
        cursor.execute("SELECT COUNT(*) FROM event_type")
        count = cursor.fetchone()[0]
        logging.info(f"Current event type count: {count}")
        
        if count == 0:
            # Insert default event types
            event_types = [
                'Wedding',
                'Birthday',
                'Corporate Event',
                'Anniversary',
                'Graduation',
                'Family Gathering',
                'Reunion',
                'Conference',
                'Seminar',
                'Other'
            ]
            
            for event_type in event_types:
                logging.info(f"Inserting event type: {event_type}")
                cursor.execute(
                    "INSERT INTO event_type (event_type_name) VALUES (%s)",
                    (event_type,)
                )
            
            conn.commit()
            logging.info("Default event types initialized successfully")
        else:
            logging.info("Event types already exist, skipping initialization")
        
    except Exception as e:
        conn.rollback()
        logging.error(f"Error initializing event types: {e}")
        raise e
    finally:
        cursor.close()
        conn.close()

def create_event_type(event_type_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Check if event type already exists
        cursor.execute("SELECT event_type_id FROM event_type WHERE event_type_name = %s", (event_type_name,))
        if cursor.fetchone():
            raise ValueError("Event type already exists")

        # Insert new event type
        cursor.execute(
            "INSERT INTO event_type (event_type_name) VALUES (%s) RETURNING event_type_id",
            (event_type_name,)
        )
        new_event_type_id = cursor.fetchone()[0]
        conn.commit()
        
        return {
            'event_type_id': new_event_type_id,
            'event_type_name': event_type_name
        }
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()


        
def add_event_item(userid, event_name, event_type, event_theme, event_color, package_id, suppliers, venues, schedule=None, start_time=None, end_time=None, status='Wishlist', onsite_firstname=None, onsite_lastname=None, onsite_contact=None, onsite_address=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("BEGIN")

        # Calculate total price from suppliers and venues
        total_price = 0
        for supplier in suppliers:
            if not supplier.get('is_removed'):
                if supplier.get('external_supplier_price'):
                    total_price += float(supplier.get('external_supplier_price', 0))
                else:
                    total_price += float(supplier.get('price', 0))
        
        for venue in venues:
            if not venue.get('is_removed'):
                total_price += float(venue.get('price', 0))

        # Prepare JSON data for modifications
        modified_suppliers = {
            'added': [dict(s) for s in suppliers if s.get('is_added')],
            'removed': [dict(s) for s in suppliers if s.get('is_removed')],
            'modified': [dict(s) for s in suppliers if s.get('is_modified')]
        }
        
        modified_venues = {
            'added': [dict(v) for v in venues if v.get('is_added')],
            'removed': [dict(v) for v in venues if v.get('is_removed')],
            'modified': [dict(v) for v in venues if v.get('is_modified')]
        }

        # Insert into events table with the package_id reference and modifications
        cursor.execute("""
            INSERT INTO events (
                userid, event_name, event_type, event_theme, event_color, 
                package_id, schedule, start_time, end_time, status,
                onsite_firstname, onsite_lastname, onsite_contact, onsite_address,
                modified_suppliers, modified_venues, total_price
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s) 
            RETURNING events_id
        """, (
            userid, event_name, event_type, event_theme, event_color, 
            package_id, schedule, start_time, end_time, status,
            onsite_firstname, onsite_lastname, onsite_contact, onsite_address,
            json.dumps(modified_suppliers),  # Convert dict to JSON string
            json.dumps(modified_venues),     # Convert dict to JSON string
            total_price
        ))
        events_id = cursor.fetchone()[0]

        # Process suppliers
        for supplier in suppliers:
            if not supplier.get('is_removed'):  # Don't add removed suppliers
                cursor.execute("""
                    INSERT INTO event_suppliers (
                        events_id, supplier_id, is_modified,
                        modified_price, external_supplier_name, 
                        external_supplier_contact, external_supplier_price
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    events_id,
                    supplier.get('supplier_id'),
                    supplier.get('is_modified', False) or supplier.get('is_added', False),
                    supplier.get('price'),
                    supplier.get('external_supplier_name'),
                    supplier.get('external_supplier_contact'),
                    supplier.get('external_supplier_price')
                ))

        # Process venues
        for venue in venues:
            if not venue.get('is_removed'):  # Don't add removed venues
                cursor.execute("""
                    INSERT INTO event_venues (
                        events_id, venue_id, is_modified,
                        modified_price
                    )
                    VALUES (%s, %s, %s, %s)
                """, (
                    events_id,
                    venue['venue_id'],
                    venue.get('is_modified', False) or venue.get('is_added', False),
                    venue.get('price')
                ))

        cursor.execute("COMMIT")
        return events_id

    except Exception as e:
        cursor.execute("ROLLBACK")
        logger.error(f"Error in add_event_item: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def get_event_details(event_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Get event details with package information
        cursor.execute("""
            SELECT e.*, ep.package_name, ep.capacity, ep.description as package_description,
                   ep.total_price as package_price, ep.additional_capacity_charges,
                   ep.charge_unit, gp.gown_package_name, gp.gown_package_price,
                   u.firstname AS firstname, u.lastname AS lastname, u.contactnumber AS contactnumber,
                   u.email AS email
            FROM events e
            LEFT JOIN event_packages ep ON e.package_id = ep.package_id
            LEFT JOIN gown_package gp ON ep.gown_package_id = gp.gown_package_id
            LEFT JOIN users u ON e.userid = u.userid
            WHERE e.events_id = %s
        """, (event_id,))
        event = cursor.fetchone()
        
        if not event:
            return None

        # Get suppliers with modifications
        cursor.execute("""
            SELECT es.*, s.firstname, s.lastname, s.service,
                   s.price as supplier_price, u.email
            FROM event_suppliers es
            LEFT JOIN suppliers s ON es.supplier_id = s.supplier_id
            LEFT JOIN users u ON s.userid = u.userid
            WHERE es.events_id = %s
        """, (event_id,))
        suppliers = cursor.fetchall()

        # Get venues with modifications
        cursor.execute("""
            SELECT ev.*, v.venue_name, v.location,
                   v.venue_price as original_price
            FROM event_venues ev
            LEFT JOIN venues v ON ev.venue_id = v.venue_id
            WHERE ev.events_id = %s
        """, (event_id,))
        venues = cursor.fetchall()

        # Get additional services
        cursor.execute("""
            SELECT ads.add_service_id, ads.add_service_name,
                   ads.add_service_description, ads.add_service_price
            FROM event_package_additional_services epas
            JOIN additional_services ads ON epas.add_service_id = ads.add_service_id
            WHERE epas.package_id = %s
        """, (event['package_id'],))
        services = cursor.fetchall()

        # Format the response
        event_details = {
            'event_id': event[0],
            'userid': event[1],
            'event_name': event[2],
            'event_type': event[3],
            'event_theme': event[4],
            'event_color': event[5],
            'package_id': event[6],
            'schedule': event[7],
            'start_time': event[8].strftime('%H:%M') if event[8] else None,
            'end_time': event[9].strftime('%H:%M') if event[9] else None,
            'status': event[10],
            'onsite_firstname': event[11],
            'onsite_lastname': event[12],
            'onsite_contact': event[13],
            'onsite_address': event[14],
            'total_price': float(event[15]) if event[15] else 0,
            'package_name': event[16],
            'package_description': event[17],
            'capacity': event[18],
            'package_price': float(event[19]) if event[19] else 0,
            'additional_capacity_charges': float(event[20]) if event[20] else 0,
            'charge_unit': event[21],
            'services': []
        }

        # Format services
        for service in services:
            service_detail = {
                'package_service_id': service[0],
                'supplier_id': service[1],
                'external_supplier_name': service[2],
                'external_supplier_contact': service[3],
                'external_supplier_price': float(service[4]) if service[4] else 0,
                'remarks': service[5],
                'is_modified': service[6],
                'service': service[7],
                'supplier_price': float(service[8]) if service[8] else 0,
                'supplier_firstname': service[9],
                'supplier_lastname': service[10],
                'supplier_email': service[11]
            }
            event_details['services'].append(service_detail)

        return event_details

    except Exception as e:
        logger.error(f"Error getting event details: {str(e)}")
        raise e
    finally:
        cursor.close()
        conn.close()

def track_service_modification(events_id, package_service_id, modification_type, original_price=None, modified_price=None, remarks=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO modified_event_services 
            (event_id, package_service_id, modification_type, original_price, modified_price, remarks)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING modification_id
        """, (events_id, package_service_id, modification_type, original_price, modified_price, remarks))
        
        modification_id = cursor.fetchone()[0]
        conn.commit()
        return modification_id
    except Exception as e:
        conn.rollback()
        logger.error(f"Error tracking service modification: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def add_service_customization(events_id, package_service_id, custom_price=None, custom_details=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO event_service_customizations 
            (event_id, package_service_id, custom_price, custom_details)
            VALUES (%s, %s, %s, %s)
            RETURNING customization_id
        """, (events_id, package_service_id, custom_price, custom_details))
        
        customization_id = cursor.fetchone()[0]
        conn.commit()
        return customization_id
    except Exception as e:
        conn.rollback()
        logger.error(f"Error adding service customization: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def get_event_modifications(events_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Get all modifications for the event
        cursor.execute("""
            SELECT m.modification_id, m.package_service_id, m.modification_type,
                   m.original_price, m.modified_price, m.remarks,
                   COALESCE(ps.supplier_id::text, ps.external_supplier_name) as supplier_identifier,
                   ps.external_supplier_contact, ps.external_supplier_price
            FROM modified_event_services m
            JOIN package_service ps ON m.package_service_id = ps.package_service_id
            WHERE m.event_id = %s
            ORDER BY m.created_at
        """, (events_id,))
        
        modifications = cursor.fetchall()
        
        # Get all customizations for the event
        cursor.execute("""
            SELECT c.customization_id, c.package_service_id, c.custom_price,
                   c.custom_details,
                   COALESCE(ps.supplier_id::text, ps.external_supplier_name) as supplier_identifier
            FROM event_service_customizations c
            JOIN package_service ps ON c.package_service_id = ps.package_service_id
            WHERE c.event_id = %s
            ORDER BY c.created_at
        """, (events_id,))
        
        customizations = cursor.fetchall()
        
        return {
            'modifications': [{
                'modification_id': m[0],
                'package_service_id': m[1],
                'modification_type': m[2],
                'original_price': float(m[3]) if m[3] else None,
                'modified_price': float(m[4]) if m[4] else None,
                'remarks': m[5],
                'supplier_identifier': m[6],
                'external_supplier_contact': m[7],
                'external_supplier_price': float(m[8]) if m[8] else None
            } for m in modifications],
            'customizations': [{
                'customization_id': c[0],
                'package_service_id': c[1],
                'custom_price': float(c[2]) if c[2] else None,
                'custom_details': c[3],
                'supplier_identifier': c[4]
            } for c in customizations]
        }
    finally:
        cursor.close()
        conn.close()

def get_all_events():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT events_id, event_name, event_type, schedule, 
                   start_time, end_time, status
            FROM events
            ORDER BY schedule
        """)
        events = cursor.fetchall()
        return events
    except Exception as e:
        logger.error(f"Error in get_all_events: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def get_events_by_date(date):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT events_id
            FROM events
            WHERE DATE(schedule) = DATE(%s)
        """, (date,))
        events = cursor.fetchall()
        return events
    except Exception as e:
        logger.error(f"Error in get_events_by_date: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def get_event_types_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT event_type, COUNT(*) as count
            FROM events
            WHERE event_type IS NOT NULL
            GROUP BY event_type
            ORDER BY count DESC
        """)
        
        events_count = cursor.fetchall()
        result = []
        for event in events_count:
            result.append({
                'type': event[0],  # event_type
                'count': int(event[1])  # count
            })
        return result
        
    except Exception as e:
        logger.error(f"Error in get_event_types_count: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def get_events_by_month_and_type():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT 
                event_type,
                EXTRACT(MONTH FROM schedule)::integer as month,
                COUNT(*) as count
            FROM events
            WHERE event_type IS NOT NULL
                AND EXTRACT(YEAR FROM schedule) = EXTRACT(YEAR FROM CURRENT_DATE)
            GROUP BY event_type, EXTRACT(MONTH FROM schedule)
            ORDER BY EXTRACT(MONTH FROM schedule), event_type
        """)
        
        events_data = cursor.fetchall()
        
        # Get unique event types
        cursor.execute("""
            SELECT DISTINCT event_type
            FROM events
            WHERE event_type IS NOT NULL
            ORDER BY event_type
        """)
        event_types = [row[0] for row in cursor.fetchall()]
        
        # Process the data
        months = list(range(1, 13))  # 1 to 12
        result = {
            'months': months,
            'eventTypes': event_types,
            'data': {}
        }
        
        # Initialize data structure
        for event_type in event_types:
            result['data'][event_type] = [0] * 12  # Initialize with zeros for all months
        
        # Fill in the actual counts
        for row in events_data:
            event_type, month, count = row
            # Adjust month index to 0-based for array
            month_index = int(month) - 1
            result['data'][event_type][month_index] = int(count)
        
        return result
        
    except Exception as e:
        logger.error(f"Error in get_events_by_month_and_type: {str(e)}")
        raise
    finally:
        cursor.close()
        conn.close()

def get_inactive_suppliers():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT s.supplier_id, u.firstname, u.lastname, u.email, u.contactnumber, 
                   u.username, u.password, s.service, s.price, s.status, u.userid
            FROM suppliers s
            JOIN users u ON s.userid = u.userid
            WHERE s.status = 'Inactive'
            ORDER BY s.supplier_id
        """)
        suppliers = cursor.fetchall()
        
        suppliers_list = []
        for supplier in suppliers:
            suppliers_list.append({
                'supplier_id': supplier[0],
                'firstname': supplier[1],
                'lastname': supplier[2],
                'email': supplier[3],
                'contactnumber': supplier[4],
                'username': supplier[5],
                'password': supplier[6],
                'service': supplier[7],
                'price': float(supplier[8]) if supplier[8] else 0,
                'status': supplier[9],
                'userid': supplier[10]
            })
        return suppliers_list
    finally:
        cursor.close()
        conn.close()

def add_supplier_social_media(supplier_id, platform, handle, url=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO supplier_social_media (supplier_id, platform, handle, url)
            VALUES (%s, %s, %s, %s)
            RETURNING social_media_id
        """, (supplier_id, platform, handle, url))
        
        social_media_id = cursor.fetchone()[0]
        conn.commit()
        return True, social_media_id

    except Exception as e:
        conn.rollback()
        logger.error(f"Error adding supplier social media: {str(e)}")
        return False, None

    finally:
        cursor.close()
        conn.close()

def get_supplier_social_media(supplier_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT social_media_id, platform, handle, url 
            FROM supplier_social_media 
            WHERE supplier_id = %s
        """, (supplier_id,))
        
        social_media = cursor.fetchall()
        return [{
            'social_media_id': sm[0],
            'platform': sm[1],
            'handle': sm[2],
            'url': sm[3]
        } for sm in social_media]

    finally:
        cursor.close()
        conn.close()

class Supplier:
    def __init__(self, supplier_id, userid=None, service=None, price=None, status=None):
        self.supplier_id = supplier_id
        self.userid = userid
        self.service = service
        self.price = price
        self.status = status

    def get_social_media(self):
        cursor = None
        conn = None
        try:
            print(f"Getting social media for supplier_id: {self.supplier_id}")
            query = """
                SELECT social_media_id, platform, handle, url 
                FROM supplier_social_media 
                WHERE supplier_id = %s
            """
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, (self.supplier_id,))
            social_media = cursor.fetchall()
            print(f"Raw social media data: {social_media}")
            
            # Convert tuple results to dictionaries
            result = [{
                'social_media_id': row[0],
                'platform': row[1],
                'handle': row[2],
                'url': row[3]
            } for row in social_media]
            
            print(f"Formatted social media: {result}")
            return result
        except Exception as e:
            print(f"Error fetching social media: {str(e)}")
            return []
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

def initialize_supplier_social_media():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Create the table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS supplier_social_media (
                social_media_id INT AUTO_INCREMENT PRIMARY KEY,
                supplier_id INT NOT NULL,
                platform VARCHAR(50) NOT NULL,
                handle VARCHAR(100) NOT NULL,
                url VARCHAR(255),
                FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
            )
        """)
        conn.commit()
        print("supplier_social_media table initialized successfully")
    except Exception as e:
        print(f"Error initializing supplier_social_media table: {str(e)}")
    finally:
        cursor.close()
        conn.close()

def get_active_outfits():
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT outfit_id, outfit_name, outfit_type, outfit_color, 
                   outfit_desc, rent_price, status, outfit_img, size, weight
            FROM outfits 
            WHERE status = 'Active'
            ORDER BY outfit_id
        """)
        outfits = cursor.fetchall()
        return [{
            'outfit_id': outfit[0],
            'outfit_name': outfit[1],
            'outfit_type': outfit[2],
            'outfit_color': outfit[3],
            'outfit_desc': outfit[4],
            'rent_price': float(outfit[5]) if outfit[5] else 0,
            'status': outfit[6],
            'outfit_img': outfit[7],
            'size': outfit[8],
            'weight': float(outfit[9]) if outfit[9] else 0
        } for outfit in outfits]
    except Exception:
        return []
    finally:
        cursor.close()
        conn.close()

def add_event_outfit(events_id, outfit_type, outfit_id=None, gown_package_id=None):
    try:
        with get_db_cursor() as cursor:
            cursor.execute("""
                INSERT INTO event_outfits (events_id, outfit_type, outfit_id, gown_package_id)
                VALUES (%s, %s, %s, %s)
                RETURNING event_outfit_id
            """, (events_id, outfit_type, outfit_id, gown_package_id))
            result = cursor.fetchone()
            return result[0] if result else None
    except Exception as e:
        print(f"Error adding event outfit: {str(e)}")
        return None

def get_event_outfits(events_id):
    try:
        with get_db_cursor() as cursor:
            # Get individual outfits
            cursor.execute("""
                SELECT eo.event_outfit_id, eo.outfit_type, 
                       o.outfit_id, o.outfit_name, o.outfit_type as outfit_category, o.size, o.rent_price,
                       gp.gown_package_id, gp.gown_package_name, gp.gown_package_price
                FROM event_outfits eo
                LEFT JOIN outfits o ON eo.outfit_id = o.outfit_id
                LEFT JOIN gown_packages gp ON eo.gown_package_id = gp.gown_package_id
                WHERE eo.events_id = %s
            """, (events_id,))
            outfits = cursor.fetchall()
            
            return [{
                'event_outfit_id': outfit[0],
                'outfit_type': outfit[1],
                'outfit_id': outfit[2],
                'outfit_name': outfit[3],
                'outfit_category': outfit[4],
                'size': outfit[5],
                'rent_price': float(outfit[6]) if outfit[6] else None,
                'gown_package_id': outfit[7],
                'gown_package_name': outfit[8],
                'gown_package_price': float(outfit[9]) if outfit[9] else None
            } for outfit in outfits]
    except Exception as e:
        print(f"Error getting event outfits: {str(e)}")
        return []

def toggle_supplier_status(supplier_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # First get current status
        cursor.execute("SELECT status FROM suppliers WHERE supplier_id = %s", (supplier_id,))
        current_status = cursor.fetchone()

        if not current_status:
            return ("not_found", None)

        # Toggle the status
        new_status = 'Inactive' if current_status[0] == 'Active' else 'Active'
        
        cursor.execute(
            "UPDATE suppliers SET status = %s WHERE supplier_id = %s",
            (new_status, supplier_id)
        )
        
        conn.commit()
        return new_status
    finally:
        cursor.close()
        conn.close()

def get_available_suppliers():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT s.supplier_id, u.firstname, u.lastname, s.service, s.price
            FROM suppliers s
            JOIN users u ON s.userid = u.userid
            WHERE s.status = 'Active'
        """)
        suppliers = cursor.fetchall()

        # Transform the result into a list of dictionaries
        return [
            {
                'supplier_id': item[0],
                'firstname': item[1],
                'lastname': item[2],
                'service': item[3],
                'price': item[4]
            }
            for item in suppliers
        ]
    finally:
        cursor.close()
        conn.close()

def get_available_venues():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT venue_id, venue_name, location, venue_price FROM venues WHERE status = 'Active'")
        venues = cursor.fetchall()

        return [
            {
                'venue_id': item[0],
                'venue_name': item[1],
                'location': item[2],
                'venue_price': item[3]
            }
            for item in venues
        ]
    finally:
        cursor.close()
        conn.close()

def get_available_gown_packages():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT gown_package_id, gown_package_name, gown_package_price FROM gown_package WHERE status = 'Active'")
        packages = cursor.fetchall()

        return [
            {
                'gown_package_id': item[0],
                'gown_package_name': item[1],
                'gown_package_price': item[2]
            }
            for item in packages
        ]
    finally:
        cursor.close()
        conn.close()

def get_package_details_by_id(package_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT ep.package_id, ep.package_name, et.event_type_name, ep.capacity, ep.description, ep.total_price,
                   ep.additional_capacity_charges, ep.charge_unit,
                   v.venue_name, v.location, v.venue_price,
                   gp.gown_package_name, gp.gown_package_price,
                   array_agg(ps.package_service_id) AS package_service_ids,
                   array_agg(ps.supplier_id) AS supplier_ids,
                   array_agg(s.service) AS services,
                   array_agg(s.price) AS service_prices,
                   array_agg(u.firstname) AS supplier_firstnames,
                   array_agg(u.lastname) AS supplier_lastnames,
                   array_agg(u.email) AS supplier_emails,
                   array_agg(ps.external_supplier_name) AS external_supplier_names,
                   array_agg(ps.external_supplier_contact) AS external_supplier_contacts,
                   array_agg(ps.external_supplier_price) AS external_supplier_prices,
                   array_agg(ps.remarks) AS remarks
            FROM event_packages ep
            LEFT JOIN event_type et ON ep.event_type_id = et.event_type_id
            LEFT JOIN venues v ON ep.venue_id = v.venue_id
            LEFT JOIN gown_package gp ON ep.gown_package_id = gp.gown_package_id
            LEFT JOIN event_package_services eps ON ep.package_id = eps.package_id
            LEFT JOIN package_service ps ON eps.package_service_id = ps.package_service_id
            LEFT JOIN suppliers s ON ps.supplier_id = s.supplier_id
            LEFT JOIN users u ON s.userid = u.userid
            WHERE ep.package_id = %s
            GROUP BY ep.package_id, et.event_type_name, v.venue_name, v.location, v.venue_price, 
                     gp.gown_package_name, gp.gown_package_price
        """, (package_id,))
        
        row = cursor.fetchone()
        if row:
            return {
                'package_id': row[0],
                'package_name': row[1],
                'event_type_name': row[2],
                'capacity': row[3],
                'description': row[4],
                'total_price': float(row[5]) if row[5] else 0,
                'additional_capacity_charges': float(row[6]) if row[6] else 0,
                'charge_unit': row[7],
                'venue_name': row[8],
                'venue_location': row[9],
                'venue_price': float(row[10]) if row[10] else 0,
                'gown_package_name': row[11],
                'gown_package_price': float(row[12]) if row[12] else 0,
                'package_service_ids': row[13] if row[13] and row[13][0] is not None else [],
                'supplier_ids': row[14] if row[14] and row[14][0] is not None else [],
                'services': row[15] if row[15] and row[15][0] is not None else [],
                'service_prices': [float(p) if p else 0 for p in row[16]] if row[16] and row[16][0] is not None else [],
                'supplier_firstnames': row[17] if row[17] and row[17][0] is not None else [],
                'supplier_lastnames': row[18] if row[18] and row[18][0] is not None else [],
                'supplier_emails': row[19] if row[19] and row[19][0] is not None else [],
                'external_supplier_names': row[20] if row[20] and row[20][0] is not None else [],
                'external_supplier_contacts': row[21] if row[21] and row[21][0] is not None else [],
                'external_supplier_prices': [float(p) if p else 0 for p in row[22]] if row[22] and row[22][0] is not None else [],
                'remarks': row[23] if row[23] and row[23][0] is not None else []
            }
        return None
    finally:
        cursor.close()
        conn.close()