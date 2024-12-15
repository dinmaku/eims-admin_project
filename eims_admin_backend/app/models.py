# models.py
import hashlib
from .db import get_db_connection
import logging
from datetime import date, time


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
        # Hash the password before inserting it
        hashed_password = hash_password(password)

        # Use the hashed password in the query
        cursor.execute(
            "INSERT INTO users (first_name, last_name, username, email, contact_number, password, user_type, address) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING userid", 
            (first_name, last_name, username, email, contact_number, hashed_password, user_type, address)
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


def create_supplier(userid, service, price):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO suppliers (userid, service, price) VALUES (%s, %s, %s)",
            (userid, service, price)
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
            SELECT userid, first_name, last_name, email, contact_number, user_type
            FROM users
            WHERE user_type IN ('Assistant', 'Staff')
            """
        )
        users = cursor.fetchall()
        # Transform the result into a list of dictionaries
        return [
            {
                'userid': item[0],
                'first_name': item[1],
                'last_name': item[2],
                'email': item[3],
                'contact_number': item[4],
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
        cursor.execute(
            """
            SELECT s.supplier_id, s.userid, s.service, s.price, 
            u.firstname, u.lastname, u.username, u.email, u.contactnumber, u.password
            FROM suppliers s
            JOIN users u ON s.userid = u.userid
            """
        )
        suppliers = cursor.fetchall()
        
        
        return [
        {
            'supplier_id': item[0],
            'userid': item[1],
            'service': item[2],
            'price': float(item[3]) if item[3] is not None else 0.0,
            'firstname': item[4],
            'lastname': item[5],
            'email': item[7],  # Ensure this is the correct column index for email
            'username': item[6],  # Ensure this is the correct column index for username
            'contactnumber': item[8],
            'password': item[9],
        }
        for item in suppliers
    ]
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
        # Get basic package information
        cursor.execute("""
            SELECT 
                p.package_id,
                p.package_name,
                p.package_type,
                p.capacity,
                p.description,
                p.total_price,
                p.venue_id,
                v.venue_name,
                v.venue_price,
                p.gown_package_id,
                gp.gown_package_name,
                gp.gown_package_price
            FROM event_packages p
            LEFT JOIN venues v ON p.venue_id = v.venue_id
            LEFT JOIN gown_package gp ON p.gown_package_id = gp.gown_package_id
        """)
        packages = []
        for row in cursor.fetchall():
            package = {
                'package_id': row[0],
                'package_name': row[1],
                'package_type': row[2],
                'capacity': row[3],
                'description': row[4],
                'total_price': float(row[5]) if row[5] else 0,
                'suppliers': [],
                'outfit_packages': [],
                'additional_services': []
            }

            # Add venue information if exists
            if row[6]:  # venue_id exists
                package['venue_id'] = row[6]
                package['venue_name'] = row[7]
                package['venue_price'] = float(row[8]) if row[8] else 0

            # Add outfit package if exists
            if row[9]:  # gown_package_id exists
                package['outfit_packages'].append({
                    'gown_package_id': row[9],
                    'gown_package_name': row[10],
                    'price': float(row[11]) if row[11] else 0
                })

            # Get suppliers for this package
            cursor.execute("""
                SELECT 
                    ps.package_service_id,
                    ps.supplier_id,
                    u.firstname,
                    u.lastname,
                    s.service,
                    s.price,
                    ps.external_supplier_name,
                    ps.external_supplier_contact,
                    ps.external_supplier_price,
                    ps.remarks
                FROM event_package_services eps
                JOIN package_service ps ON eps.package_service_id = ps.package_service_id
                LEFT JOIN suppliers s ON ps.supplier_id = s.supplier_id
                LEFT JOIN users u ON s.userid = u.userid
                WHERE eps.package_id = %s
            """, (package['package_id'],))

            for supplier_row in cursor.fetchall():
                if supplier_row[1]:  # Internal supplier
                    package['suppliers'].append({
                        'supplier_id': supplier_row[1],
                        'firstname': supplier_row[2],
                        'lastname': supplier_row[3],
                        'service_type': supplier_row[4],
                        'price': float(supplier_row[5]) if supplier_row[5] else 0,
                        'remarks': supplier_row[9]
                    })
                else:  # External supplier
                    package['suppliers'].append({
                        'external_supplier_name': supplier_row[6],
                        'external_supplier_contact': supplier_row[7],
                        'price': float(supplier_row[8]) if supplier_row[8] else 0,
                        'remarks': supplier_row[9]
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
            """, (package['package_id'],))

            for service_row in cursor.fetchall():
                package['additional_services'].append({
                    'add_service_id': service_row[0],
                    'add_service_name': service_row[1],
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
        cursor.execute("BEGIN")
        print("Inserting package data into event_packages")

        # Insert the package data into the event_packages table
        cursor.execute(
            """
            INSERT INTO event_packages (package_name, package_type, venue_id, capacity, 
                                        additional_capacity_charges, charge_unit, description, gown_package_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING package_id
            """,
            (package_data['package_name'], package_data['package_type'], package_data['venue_id'],
             package_data['capacity'], package_data['additional_capacity_charges'],
             package_data['charge_unit'], package_data['description'], package_data['gown_package_id'])
        )
        package_id = cursor.fetchone()[0]
        print(f"Package ID: {package_id}")

        # Insert package services
        for supplier in package_data['suppliers']:
            if supplier['type'] == 'internal':
                print(f"Inserting internal supplier {supplier['supplier_id']}")
                cursor.execute(
                    """
                    INSERT INTO package_service (supplier_id, remarks)
                    VALUES (%s, %s)
                    RETURNING package_service_id
                    """,
                    (supplier['supplier_id'], supplier['remarks'])
                )
            else:
                print(f"Inserting external supplier {supplier['external_supplier_name']}")
                cursor.execute(
                    """
                    INSERT INTO package_service (external_supplier_name, external_supplier_contact, external_supplier_price, remarks)
                    VALUES (%s, %s, %s, %s)
                    RETURNING package_service_id
                    """,
                    (supplier['external_supplier_name'], supplier['external_supplier_contact'], supplier['external_supplier_price'], supplier['remarks'])
                )
            package_service_id = cursor.fetchone()[0]
            print(f"Package Service ID: {package_service_id}")

            # Link package service to the event package
            cursor.execute(
                """
                INSERT INTO event_package_services (package_id, package_service_id)
                VALUES (%s, %s)
                """,
                (package_id, package_service_id)
            )

        # Add additional services prices
        if 'additional_services' in package_data:
            cursor.execute(
                """
                SELECT COALESCE(SUM(add_service_price), 0)
                FROM additional_services
                WHERE add_service_id = ANY(%s)
                """,
                ([service['add_service_id'] for service in package_data['additional_services']],)
            )
            additional_services_price = cursor.fetchone()[0]
            total_price = additional_services_price

            # Insert additional services
            for service in package_data['additional_services']:
                cursor.execute(
                    """
                    INSERT INTO event_package_additional_services (package_id, add_service_id)
                    VALUES (%s, %s)
                    """,
                    (package_id, service['add_service_id'])
                )

        # Calculate total price after inserting package and services
        total_price = calculate_total_price(package_id, cursor)

        # Add venue_price
        cursor.execute(
            """
            SELECT COALESCE(venue_price, 0)
            FROM venues
            WHERE venue_id = %s
            """, (package_data['venue_id'],)
        )
        venue_price = cursor.fetchone()[0]
        total_price += venue_price

        # Add gown_package_price
        if package_data['gown_package_id']:
            cursor.execute(
                """
                SELECT COALESCE(gown_package_price, 0)
                FROM gown_package
                WHERE gown_package_id = %s
                """, (package_data['gown_package_id'],)
            )
            gown_package_price = cursor.fetchone()[0]
            total_price += gown_package_price

        print(f"Total price calculated including venue and gown package prices: {total_price}")

        # Update the total price in the event_packages table
        cursor.execute(
            """
            UPDATE event_packages 
            SET total_price = %s 
            WHERE package_id = %s
            """,
            (total_price, package_id)
        )

        cursor.execute("COMMIT")
        return True
    except Exception as e:
        cursor.execute("ROLLBACK")
        print(f"Error inserting package: {e}")
        return False
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
                package_type = %s,
                capacity = %s,
                description = %s
            WHERE package_id = %s
            RETURNING package_id
        """, (
            package_data['package_name'],
            package_data['package_type'],
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
                e.schedule, 
                e.start_time, 
                e.end_time, 
                e.status,
                ep.package_id, 
                ep.package_name, 
                ep.package_type, 
                ep.capacity, 
                ep.description AS package_description, 
                ep.total_price,
                v.venue_name, 
                v.location, 
                gp.gown_package_name, 
                gp.gown_package_price,
                u.firstname,
                u.lastname,
                u.contactnumber,
                COALESCE(array_agg(json_build_object(
                    'name', COALESCE(su.firstname || ' ' || su.lastname, ps.external_supplier_name),
                    'service', COALESCE(s.service, 'External Supplier'),
                    'price', COALESCE(s.price, ps.external_supplier_price)
                ) ORDER BY su.firstname || ' ' || su.lastname, ps.external_supplier_name), '{}'::json[]) AS suppliers
            FROM events e
            LEFT JOIN event_packages ep ON e.package_id = ep.package_id
            LEFT JOIN venues v ON ep.venue_id = v.venue_id
            LEFT JOIN gown_package gp ON ep.gown_package_id = gp.gown_package_id
            LEFT JOIN users u ON e.userid = u.userid
            LEFT JOIN event_package_services eps ON ep.package_id = eps.package_id
            LEFT JOIN package_service ps ON eps.package_service_id = ps.package_service_id
            LEFT JOIN suppliers s ON ps.supplier_id = s.supplier_id
            LEFT JOIN users su ON s.userid = su.userid
            WHERE e.status = 'Wishlist'  -- Filter for events with 'Wishlist' status
            GROUP BY e.events_id, ep.package_id, v.venue_name, v.location, gp.gown_package_name, gp.gown_package_price, u.firstname, u.lastname, u.contactnumber
        """)
        
        events = cursor.fetchall()
        
        result = []
        for item in events:
            event_dict = {
                'events_id': item[0],
                'userid': item[1],
                'event_name': item[2],
                'event_type': item[3],
                'event_theme': item[4],
                'event_color': item[5],
                'schedule': item[6],
                'start_time': item[7].strftime('%H:%M:%S') if isinstance(item[7], time) else item[7],
                'end_time': item[8].strftime('%H:%M:%S') if isinstance(item[8], time) else item[8],
                'status': item[9],
                'package_id': item[10],
                'package_name': item[11],
                'package_type': item[12],
                'capacity': item[13],
                'package_description': item[14],
                'total_price': item[15],
                'venue_name': item[16],
                'location': item[17],
                'gown_package_name': item[18],
                'gown_package_price': item[19],
                'firstname': item[20],
                'lastname': item[21],
                'contactnumber': item[22],
                'suppliers': item[23]  # Suppliers data
            }
            result.append(event_dict)
        
        return result
    except Exception as e:
        logging.error(f"Error fetching all 'Wishlist' events for admin: {e}")
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


#models for venues

def create_venue(venue_name, location, venue_price):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Insert the package data into the event_packages table
        cursor.execute(
            "INSERT INTO venues (venue_name, location, venue_price) "
            "VALUES (%s, %s, %s)",
            (venue_name, location, venue_price)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting package: {e}")  # Log the error message
        return False
    finally:
        cursor.close()
        conn.close()

# Function to fetch all venues from the venues table
def get_all_venues():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT venue_id, venue_name, location, venue_price FROM venues")
        venues = cursor.fetchall()

        # Transform the result into a list of dictionaries
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


def update_venue(venue_id, venue_name, location, venue_price):
    """
    Updates a venue's details in the database.

    Args:
        venue_id (int): The ID of the venue to update.
        venue_name (str): The new name for the venue.
        location (str): The new location of the venue.
        venue_price (float): The new price for the venue.

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
            SET venue_name = %s, location = %s, venue_price = %s
            WHERE venue_id = %s
        """
        cursor.execute(query, (venue_name, location, venue_price, venue_id))
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





#gown package models
def get_gown_packages():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT gown_package_id, gown_package_name, gown_package_price, description
            FROM gown_package
            """
        )
        gown_packages = cursor.fetchall()
        
        return [
            {
                'gown_package_id': item[0],
                'gown_package_name': item[1],
                'gown_package_price': float(item[2]) if item[2] is not None else 0.0,
                'description': item[3],
            }
            for item in gown_packages
        ]
    finally:
        cursor.close()
        conn.close()


#models for outfit package
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

#additional services models
def create_additional_service(add_service_name, add_service_description, add_service_price):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO additional_services (add_service_name, add_service_description, add_service_price) "
            "VALUES (%s, %s, %s)",
            (add_service_name, add_service_description, add_service_price)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error inserting additional service: {e}")  # Log the error message
        return False
    finally:
        cursor.close()
        conn.close()

# Function to fetch all additional services from the additional_services table
def get_all_additional_services():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT add_service_id, add_service_name, add_service_description, add_service_price FROM additional_services")
        services = cursor.fetchall()

        # Transform the result into a list of dictionaries
        return [
            {
                'add_service_id': item[0],
                'add_service_name': item[1],
                'add_service_description': item[2],
                'add_service_price': item[3]
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
