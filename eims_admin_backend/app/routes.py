#routes.py
from flask import Flask, request, jsonify, send_file, make_response
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import os
import logging
from .db import get_db_connection
from .models import (
    check_user, create_user, create_supplier, get_users_by_type,
    get_admin_users, get_suppliers_with_users, get_package_services_with_suppliers,
    update_suppliers_and_user, update_staff, delete_user, get_packages,
    create_package, update_package, delete_package, get_user_id_by_email,
    get_all_booked_wishlist, update_event, get_packages_wedding,
    create_venue, get_all_venues, delete_venue, update_venue,
    get_active_venues, get_inactive_venues, toggle_venue_status,
    update_venue_price, get_gown_packages, get_inactive_packages,
    toggle_package_status, get_all_gown_packages, add_gown_package,
    create_additional_service, update_additional_service_price,
    get_active_additional_services, get_inactive_additional_services,
    toggle_additional_service_status, get_all_additional_services,
    update_additional_service, get_event_types, initialize_event_types,
    create_event_type, add_event_item, get_event_package_configuration,
    get_event_details, track_service_modification, add_service_customization,
    get_event_modifications, get_all_events, get_events_by_date,
    get_event_types_count, get_events_by_month_and_type, get_inactive_suppliers,
    add_supplier_social_media, get_supplier_social_media, initialize_supplier_social_media,
    get_active_outfits, add_event_outfit, get_event_outfits,
    toggle_supplier_status, get_available_suppliers, get_available_venues,
    get_available_gown_packages, get_package_details_by_id,
    track_outfit_modification, track_individual_outfit_modification,
    track_additional_service_modification, get_all_outfits, create_outfit,
    create_wishlist_package, get_wishlist_package, get_event_wishlists,
    update_wishlist_package, delete_wishlist_package, Supplier,
    update_wishlist_supplier_status, update_wishlist_outfit_status,
    update_wishlist_additional_service_status, delete_wishlist_outfit_direct,
    delete_wishlist_service_direct, delete_wishlist_supplier_direct, delete_wishlist_venue_direct,
    fetch_upcoming_events, create_invoice, get_invoice_by_id, get_invoice_by_event,
    update_invoice, record_payment, get_payments_by_invoice,
    get_all_discounts, get_active_discounts, get_inactive_discounts,
    update_wishlist_venue_status, get_wishlist_venues
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

SECRET_KEY = os.getenv('eims', 'fallback_jwt_secret')

def init_routes(app):
    # Initialize CORS with proper configuration
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:5173"],
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "supports_credentials": True
        },
        r"/*": {
            "origins": ["http://localhost:5173"],
            "allow_headers": ["Content-Type", "Authorization"],
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "supports_credentials": True
        }
    })
    
    # Initialize tables
    initialize_event_types()
    initialize_supplier_social_media()
    
    @app.route('/login', methods=['POST'])
    def login():
        try:
            # Get the login data
            data = request.get_json(force=True, silent=True) or {}
            email = data.get('email')
            password = data.get('password')

            # Check if email and password are provided
            if not email or not password:
                logger.info("Missing email or password")
                return jsonify({'message': 'Email and password are required!'}), 400

            # Check the user credentials
            is_valid, user_type = check_user(email, password)
            if is_valid:
                # Generate JWT token with additional claims
                access_token = create_access_token(identity=email, additional_claims={"user_type": user_type})

                return jsonify({
                    'message': 'Login successful!',
                    'access_token': access_token,
                    'user_type': user_type
                }), 200
            else:
                logger.info("Invalid credentials or unauthorized user type")
                return jsonify({'message': '* Invalid email, password, or unauthorized access.'}), 401

        except Exception as e:
            logger.error(f"Error during login: {e}")
            return jsonify({'message': 'An error occurred during login.'}), 500

        
    # Decorator to protect routes and check token
    def token_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'msg': 'Token is missing'}), 403

            try:
                # Remove 'Bearer ' from the token string
                token = token.split(" ")[1]
                # Decode the token using the secret key
                decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return jsonify({'msg': 'Token has expired'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'msg': 'Invalid token'}), 401

            # Token is valid, pass control to the original route function
            return f(decoded_token, *args, **kwargs)

        return decorated_function
    
    @app.route('/check-auth', methods=['GET'])
    @jwt_required()
    def check_auth():
        try:
            # Access the identity from the decoded JWT token
            current_user = get_jwt_identity()  # This is the email (identity) you set in the JWT token
            return jsonify({"msg": f"Token is valid for user: {current_user}"}), 200
        except Exception as e:
            return jsonify({'msg': f'Error: {str(e)}'}), 422
        
    @app.route('/refresh', methods=['POST'])
    @jwt_required(refresh=True)
    def refresh():
        current_user = get_jwt_identity()
        new_access_token = create_access_token(identity=current_user)
        return jsonify(access_token=new_access_token)


    @app.route('/logout', methods=['POST'])
    @jwt_required()  # This decorator ensures that the request has a valid JWT token
    def logout():
        try:
            # Prepare the response and unset the JWT cookie
            response = jsonify({'message': 'Successfully logged out.'})
            unset_jwt_cookies(response)  # This clears the JWT cookie, if using cookies for JWT
            return response, 200
        except Exception as e:
            return jsonify({'message': f"Error during logout: {str(e)}"}), 500



#routes for manage users


    @app.route('/add-user', methods=['POST'])
    def add_user():
        try:
            data = request.get_json()
            
            # Create the user
            user_created, user_id, error_message = create_user(
                first_name=data['firstName'],
                last_name=data['lastName'],
                username=data['username'],
                email=data['email'],
                contact_number=data['contactNumber'],
                password=data['password'],
                user_type=data['user_type'],
                address=data['address']
            )

            if user_created:
                if data['user_type'] == 'Suppliers':
                    # Insert the supplier entry after the user is created
                    supplier_created = create_supplier(
                        userid=user_id,
                        service=data['service'],
                        price=data['price']
                    )
                    if supplier_created:
                        logger.info("Supplier data inserted successfully")
                    else:
                        logger.error("Failed to create supplier")
                        return jsonify({"message": "Failed to create supplier"}), 500
                logger.info("User data validated and inserted into the database successfully")
                return jsonify({"message": "User registered successfully"}), 201
            else:
                logger.error(f"User creation failed: {error_message}")
                return jsonify({"message": error_message}), 400

        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            return jsonify({"message": "Internal server error"}), 500



        

    @app.route('/created-users', methods=['GET'])
    @jwt_required()
    def get_users_by_type_route():
        try:
            # Fetch users with user_type 'assistant' or 'staff'
            users = get_users_by_type()
            return jsonify(users), 200
        except Exception as e:
            logger.error(f"Error fetching users: {e}")
            return jsonify({'message': 'An error occurred while fetching users'}), 500

    @app.route('/get_admin', methods=['GET', 'OPTIONS'])
    @jwt_required()
    def get_admin_list():
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            # Fetch users with user_type 'Admin'
            users = get_admin_users()
            response = jsonify(users)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        except Exception as e:
            logger.error(f"Error fetching admin users: {e}")
            response = jsonify({'message': 'An error occurred while fetching admin users'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500



    @app.route('/suppliers', methods=['GET'])
    @jwt_required()
    def get_suppliers_route():
        try:
            # Fetch suppliers with their associated user details
            suppliers = get_suppliers_with_users()
            return jsonify(suppliers), 200
        except Exception as e:
            logger.error(f"Error fetching suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching suppliers'}), 500

    @app.route('/package-service-suppliers', methods=['GET'])
    @jwt_required()
    def get_event_service_suppliers_route():
        try:
            # Fetch suppliers with their associated user details
            suppliers = get_package_services_with_suppliers()
            return jsonify(suppliers), 200
        except Exception as e:
            logger.error(f"Error fetching suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching suppliers'}), 500
        

    @app.route('/gown-packages', methods=['GET'])
    @jwt_required()
    def get_gown_packages_route():
        try:
            gown_packages = get_gown_packages()
            return jsonify(gown_packages), 200
        except Exception as e:
            logger.error(f"Error fetching gown packages: {e}")
            return jsonify({'message': 'An error occurred while fetching gown packages'}), 500
        

    @app.route('/edit-supplier/<int:supplier_id>', methods=['PUT'])
    @jwt_required()
    def edit_supplier(supplier_id):
        try:
            data = request.get_json()
            logger.info(f"Received data: {data}")  # Log incoming data

            # Get existing supplier data
            conn = get_db_connection()
            cursor = conn.cursor()

            # First, get the existing supplier data
            cursor.execute("SELECT service FROM suppliers WHERE supplier_id = %s", (supplier_id,))
            supplier_data = cursor.fetchone()

            if not supplier_data:
                return jsonify({"message": "Supplier not found"}), 404

            existing_service = supplier_data[0]

            # If only price is being updated, use existing service
            if 'price' in data and len(data) == 1:
                cursor.execute(
                    "UPDATE suppliers SET price = %s WHERE supplier_id = %s",
                    (data['price'], supplier_id)
                )
            else:
                # Handle full supplier update
                if 'service' not in data or 'price' not in data:
                    return jsonify({"message": "Supplier-specific fields 'service' and 'price' are required"}), 400

                cursor.execute(
                    "UPDATE suppliers SET service = %s, price = %s WHERE supplier_id = %s",
                    (data['service'], data['price'], supplier_id)
                )

            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({"message": "Supplier updated successfully"}), 200

        except Exception as e:
            logger.error(f"Error in edit_supplier route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500

    @app.route('/edit-supplier-rate/<int:supplier_id>', methods=['PUT'])
    @jwt_required()
    def update_supplier_rate(supplier_id):
        try:
            data = request.get_json()
            price = data.get('price')
            
            if price is None:
                return jsonify({'message': 'Price is required'}), 400

            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "UPDATE suppliers SET price = %s WHERE supplier_id = %s",
                (price, supplier_id)
            )
            
            conn.commit()
            cursor.close()
            conn.close()

            return jsonify({'message': 'Supplier rate updated successfully'}), 200

        except Exception as e:
            logger.error(f"Error updating supplier rate: {e}")
            return jsonify({'message': 'An error occurred while updating supplier rate'}), 500

    @app.route('/created-users/<int:userid>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def edit_staff(userid):
        try:
            if not userid:
                return jsonify({"message": "Invalid user ID"}), 400

            data = request.get_json(force=True, silent=True) or {}
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            email = data.get('email')
            contact = data.get('contactnumber') 
            user_type = data.get('user_type')

            # Validate that all required fields are provided
            if not all([firstname, lastname, email, contact, user_type]):
                return jsonify({"message": "All fields are required"}), 400

            # Update the user data
            if update_staff(userid, firstname, lastname, email, contact, user_type):
                return jsonify({"message": "Staff updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update staff. User not found or database error occurred."}), 404
        except Exception as e:
            logger.error(f"Error in edit_staff route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500




    @app.route('/created-users/<int:userid>', methods=['DELETE'])
    @jwt_required()
    def delete_users(userid):
        """
        Deletes a user and related events based on the user ID.
        """
        try:
            result = delete_user(userid)
            if result:
                return jsonify({"message": "User and related events deleted successfully"}), 200
            else:
                return jsonify({"message": "Failed to delete user and related events"}), 404
        except Exception as e:
            logger.error(f"Error in delete_users route: {e}")
            return jsonify({"message": "An error occurred while deleting the user"}), 500





#routes for add-services

    @app.route('/created-packages', methods=['GET'])
    @jwt_required()
    def get_packages_route():
        try:
            # Fetch all event packages
            packages = get_packages()
            return jsonify(packages), 200
        except Exception as e:
            logger.error(f"Error fetching packages: {e}")
            return jsonify({'message': 'An error occurred while fetching packages'}), 500

    @app.route('/create-package', methods=['POST'])
    @jwt_required()
    def create_package_route():
        data = request.get_json()
        logger.info("Received data:", data)

        required_fields = ['package_name', 'event_type_id', 'venue_id', 'capacity', 
                         'additional_capacity_charges', 'charge_unit', 'description', 
                         'suppliers', 'gown_package_id', 'total_price']

        if not all(field in data for field in required_fields):
            return jsonify({"error": "All fields are required"}), 400

        try:
            data['capacity'] = int(data['capacity'])
            data['additional_capacity_charges'] = Decimal(str(data['additional_capacity_charges']))
            data['charge_unit'] = int(data['charge_unit'])
            data['gown_package_id'] = int(data['gown_package_id']) if data['gown_package_id'] else None
            data['event_type_id'] = int(data['event_type_id'])
            data['total_price'] = Decimal(str(data['total_price']))

            if not isinstance(data['suppliers'], list):
                return jsonify({"error": "Suppliers must be a list"}), 400

            for supplier in data['suppliers']:
                if 'type' not in supplier or supplier['type'] not in ['internal', 'external']:
                    return jsonify({"error": "Invalid supplier type"}), 400

            package_id = create_package(data)
            if package_id:
                return jsonify({"message": "Package created successfully", "package_id": package_id}), 201
            else:
                return jsonify({"error": "Failed to create package"}), 500

        except ValueError as e:
            return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
        except Exception as e:
            logger.error(f"Error in create_package_route: {e}")
            return jsonify({"error": str(e)}), 500

        

    @app.route('/created-package/<int:package_id>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def edit_package(package_id):
        try:
            if not package_id:
                return jsonify({"message": "Invalid package ID"}), 400

            data = request.get_json(force=True, silent=True) or {}
            required_fields = ["package_name", "package_type", "capacity", "price", "description", "inclusions"]

            # Ensure all required fields are present
            if not all(field in data for field in required_fields):
                return jsonify({"message": "Missing required fields"}), 400

            # Update the package data
            if update_package(package_id, data):
                return jsonify({"message": "Package updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update package. Package not found or database error occurred."}), 404
        except Exception as e:
            logger.error(f"Error in edit_package route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500
            
            
    @app.route('/created-package/<int:package_id>', methods=['DELETE'])
    @jwt_required()
    def delete_package_route(package_id):
        try:
            if delete_package(package_id):
                return jsonify({"message": "Package deleted successfully"}), 200
            else:
                return jsonify({"message": "Package not found or could not be deleted"}), 404
        except Exception as e:
            logger.error(f"Error deleting package: {e}")
            return jsonify({"message": "An error occurred while deleting the package"}), 500

            
    


#manage events routes
    @app.route('/booked-wishlist', methods=['GET', 'OPTIONS'])
    @jwt_required()
    def get_booked_wishlist_route():
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            # Get all booked wishlists
            booked_wishlists = get_all_booked_wishlist()
            logger.info(f"Booked wishlists data: {booked_wishlists}")
            
            response = jsonify(booked_wishlists)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        except Exception as e:
            logger.error(f"Error getting booked wishlist: {str(e)}")
            response = jsonify({
                'success': False,
                'message': str(e)
            })
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/booked-wishlist/<int:events_id>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def update_booked_wishlist(events_id):
        try:
            if not events_id:
                return jsonify({"message": "Invalid event ID"}), 400

            data = request.get_json(force=True, silent=True) or {}
            required_fields = ["event_name", "event_type", "event_theme", "event_color", "venue"]

            # Ensure all required fields are present
            if not all(field in data and data[field] for field in required_fields):
                return jsonify({"message": "All fields are required"}), 400

            # Extract data
            event_name = data["event_name"]
            event_type = data["event_type"]
            event_theme = data["event_theme"]
            event_color = data["event_color"]
            venue = data["venue"]

            # Update the event data
            if update_event(events_id, event_name, event_type, event_theme, event_color, venue):
                return jsonify({"message": "Event updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update event. Event not found or database error occurred."}), 404
        except Exception as e:
            logger.error(f"Error in update_booked_wishlist route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500



#create event routes


    @app.route('/created-packages-wedding', methods=['GET'])
    @jwt_required()
    def get_packages_wedding_route():
        try:
            # Fetch all event packages
            packages = get_packages_wedding()
            return jsonify(packages), 200
        except Exception as e:
            logger.error(f"Error fetching packages: {e}")
            return jsonify({'message': 'An error occurred while fetching packages'}), 500




#venues routes

    @app.route('/venues', methods=['POST'])
    @jwt_required()
    def add_venue():
        try:
            data = request.get_json()
            venue_name = data.get('venue_name')
            location = data.get('location')
            description = data.get('description')
            venue_capacity = data.get('venue_capacity')

            if not all([venue_name, location, description, venue_capacity]):
                return jsonify({'message': 'Missing required fields'}), 400

            success = create_venue(venue_name, location, description, venue_capacity)
            if success:
                return jsonify({'message': 'Venue added successfully'}), 200
            else:
                return jsonify({'message': 'Failed to add venue'}), 400

        except Exception as e:
            logger.error(f"Error adding venue: {e}")
            return jsonify({'message': 'An error occurred while adding the venue'}), 500

    @app.route('/venues/<int:venue_id>', methods=['PUT'])
    @jwt_required()
    def update_venue_route(venue_id):
        data = request.get_json()
        venue_name = data.get('venue_name')
        location = data.get('location')
        venue_price = data.get('venue_price')
        venue_capacity = data.get('venue_capacity')
        description = data.get('description')

        if not all([venue_name, location, venue_price, venue_capacity]):
            return jsonify({'message': 'Missing required fields'}), 400

        try:
            success = update_venue(venue_id, venue_name, location, venue_price, venue_capacity, description)
            if success:
                return jsonify({'message': 'Venue updated successfully'}), 200
            else:
                return jsonify({'message': 'Venue not found'}), 404
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @app.route('/venues', methods=['GET'])
    @jwt_required()
    def get_venues_route():
        try:
            # Fetch all event packages
            packages = get_all_venues()
            return jsonify(packages), 200
        except Exception as e:
            logger.error(f"Error fetching packages: {e}")
            return jsonify({'message': 'An error occurred while fetching packages'}), 500

    @app.route('/inactive-venues', methods=['GET'])
    @jwt_required()
    def get_inactive_venues_route():
        try:
            venues = get_inactive_venues()
            return jsonify(venues), 200
        except Exception as e:
            logger.error(f"Error fetching inactive venues: {e}")
            return jsonify({'message': 'An error occurred while fetching inactive venues'}), 500

    @app.route('/toggle-venue-status/<int:venue_id>', methods=['PUT'])
    @jwt_required()
    def toggle_venue_status_route(venue_id):
        try:
            success, result = toggle_venue_status(venue_id)
            if success:
                return jsonify({
                    'message': 'Venue status updated successfully',
                    'new_status': result
                }), 200
            else:
                return jsonify({'message': result}), 400
        except Exception as e:
            logger.error(f"Error updating venue status: {e}")
            return jsonify({'message': 'An error occurred while updating venue status'}), 500

    @app.route('/update-venue-price/<int:venue_id>', methods=['PUT'])
    @jwt_required()
    def update_venue_price_route(venue_id):
        try:
            data = request.get_json()
            price = data.get('price')
            
            if price is None:
                return jsonify({"message": "Price is required"}), 400
                
            success = update_venue_price(venue_id, price)
            if success:
                return jsonify({"message": "Venue price updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update venue price"}), 400
        except Exception as e:
            logger.error(f"Error updating venue price: {e}")
            return jsonify({"message": "An error occurred while updating venue price"}), 500

    @app.route('/events', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def create_event():
        if request.method == 'OPTIONS':
            # Handle preflight request
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'POST,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        try:
            # Get user ID from JWT token
            email = get_jwt_identity()
            userid = get_user_id_by_email(email)
            
            if not userid:
                response = jsonify({
                    'success': False,
                    'message': 'Invalid user token'
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 401

            data = request.get_json()
            
            # Extract base event data
            event_data = {
                'userid': userid,  # Use the userid from JWT token
                'event_name': data.get('event_name'),
                'event_type': data.get('event_type'),
                'event_theme': data.get('event_theme'),
                'event_color': data.get('event_color'),
                'package_id': data.get('package_id'),
                'schedule': data.get('schedule'),
                'start_time': data.get('start_time'),
                'end_time': data.get('end_time'),
                'status': data.get('status', 'Wishlist'),
                'onsite_firstname': data.get('onsite_firstname'),
                'onsite_lastname': data.get('onsite_lastname'),
                'onsite_contact': data.get('onsite_contact'),
                'onsite_address': data.get('onsite_address'),
                'total_price': data.get('total_price', 0),
                'booking_type': data.get('booking_type', 'Onsite')
            }

            # Package configuration data
            package_config = {
                'suppliers': data.get('suppliers', []),
                'outfits': data.get('outfits', []),
                'services': data.get('services', []),
                'additional_items': data.get('additional_items', [])
            }

            # Add event and its configurations
            events_id = add_event_item(**event_data, **package_config)

            if events_id:
                response = jsonify({
                    'success': True,
                    'message': 'Event created successfully',
                    'events_id': events_id
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 201
            else:
                response = jsonify({
                    'success': False,
                    'message': 'Failed to create event'
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 500

        except Exception as e:
            logger.error(f"Error creating event: {str(e)}")
            response = jsonify({
                'success': False,
                'message': f'Error creating event: {str(e)}'
            })
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

#routes for outfit packages

    @app.route('/gown-packages', methods=['GET'])
    @jwt_required()
    def get_all_gown_packages_route():
        try:
            # Fetch all gown packages
            packages = get_all_gown_packages()
            return jsonify(packages), 200
        except Exception as e:
            logger.error(f"Error fetching gown packages: {e}")
            return jsonify({'message': 'An error occurred while fetching gown packages'}), 500
        
        
    @app.route('/outfits', methods=['GET'])
    @jwt_required()
    def get_outfits_route():
        try:
            # Fetch all outfits
            outfits = get_all_outfits()
            return jsonify(outfits), 200
        except Exception as e:
            logger.error(f"Error fetching outfits: {e}")
            return jsonify({'message': 'An error occurred while fetching outfits'}), 500

    @app.route('/outfits', methods=['POST'])
    @jwt_required()
    def create_new_outfit():
        try:
            # Get data from request
            data = request.get_json()
            
            # Validate required fields
            required_fields = ['outfit_name', 'outfit_type', 'outfit_color', 'rent_price', 'size', 'weight']
            for field in required_fields:
                if not data.get(field):
                    return jsonify({'message': f'Missing required field: {field}'}), 400
            
            # Create the outfit
            success, outfit_id, message = create_outfit(data)
            
            if success:
                return jsonify({
                    'message': message,
                    'outfit_id': outfit_id
                }), 201
            else:
                return jsonify({'message': message}), 400
                
        except Exception as e:
            logger.error(f"Error in create_new_outfit: {str(e)}")
            return jsonify({'message': 'An error occurred while creating the outfit'}), 500

    @app.route('/add-gown-package', methods=['POST'])
    @jwt_required()
    def add_gown_package_route():
        try:
            data = request.get_json(force=True, silent=True) or {}
            gown_package_name = data.get('gown_package_name')
            description = data.get('description')
            outfits = data.get('outfits')  # List of outfit IDs

            if not all([gown_package_name, outfits]):
                return jsonify({'message': 'Missing required data'}), 400

            gown_package_id = add_gown_package(gown_package_name, description, outfits)
            return jsonify({'message': 'Gown package added successfully', 'gown_package_id': gown_package_id}), 201
        except Exception as e:
            logger.error(f"Error adding gown package: {e}")
            return jsonify({'message': 'An error occurred while adding the gown package'}), 500

    @app.route('/outfits', methods=['GET'])
    @jwt_required()
    def outfits_route():
        try:
            outfits = get_active_outfits()
            return jsonify(outfits), 200
        except Exception:
            return jsonify({'message': 'An error occurred while fetching outfits'}), 500


#additional services routes

    @app.route('/additional-services', methods=['GET', 'POST'])
    @jwt_required()
    def additional_services_route():
        if request.method == 'GET':
            try:
                services = get_active_additional_services()
                return jsonify(services), 200
            except Exception as e:
                return jsonify({'message': 'An error occurred while fetching additional services'}), 500
        elif request.method == 'POST':
            try:
                data = request.get_json(force=True, silent=True) or {}
                add_service_name = data.get('add_service_name')
                add_service_description = data.get('add_service_description')

                if not all([add_service_name, add_service_description]):
                    return jsonify({"error": "All fields are required: add_service_name, add_service_description"}), 400

                success = create_additional_service(add_service_name, add_service_description)

                if success:
                    return jsonify({"message": "Service created successfully"}), 200
                else:
                    return jsonify({"error": "Failed to create service"}), 500
            except Exception as e:
                return jsonify({"error": "An internal server error occurred"}), 500

    @app.route('/update-service/<int:add_service_id>', methods=['PUT'])
    @jwt_required()
    def update_service_details(add_service_id):
        try:
            if not add_service_id:
                return jsonify({"message": "Invalid service ID"}), 400

            data = request.json
            required_fields = ["add_service_name", "add_service_description", "add_service_price"]

            if data is None or not all(field in data and data.get(field) for field in required_fields):
                return jsonify({"message": "All fields are required"}), 400

            add_service_name = data["add_service_name"]
            add_service_description = data["add_service_description"]
            add_service_price = data["add_service_price"]

            if update_additional_service(add_service_id, add_service_name, add_service_description, add_service_price):
                return jsonify({"message": "Service updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update service. Service not found or database error occurred."}), 404
        except Exception as e:
            logger.error(f"Error in update_service_details route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500

    @app.route('/event-types', methods=['GET'])
    def get_event_types_route():
        try:
            event_types = get_event_types()
            return jsonify(event_types), 200
        except Exception as e:
            logger.error(f"Error fetching event types: {e}")
            return jsonify({"error": str(e)}), 500

    @app.route('/create-event-type', methods=['POST'])
    @jwt_required()
    def create_event_type_route():
        try:
            data = request.get_json()
            if not data or 'event_type_name' not in data:
                return jsonify({'error': 'Event type name is required'}), 400

            try:
                new_event_type = create_event_type(data['event_type_name'])
                return jsonify({
                    'message': 'Event type created successfully',
                    'event_type': new_event_type
                }), 201
            except ValueError as ve:
                return jsonify({'error': str(ve)}), 400
            except Exception as e:
                return jsonify({'error': str(e)}), 500

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/event-types-count', methods=['GET'])
    def get_event_types_count_route():
        try:
            result = get_event_types_count()
            return jsonify(result), 200
        except Exception as e:
            print(f"Error in get_event_types_count_route: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @app.route('/wishlist', methods=['POST'])
    @jwt_required()
    def add_wishlist():
        try:
            # Get user ID from JWT token
            email = get_jwt_identity()
            userid = get_user_id_by_email(email)
            
            if not userid:
                return jsonify({
                    'success': False,
                    'message': 'Invalid user token'
                }), 401

            data = request.get_json()
            
            # Extract base event data
            event_data = {
                'userid': userid,  # Use the userid from JWT token
                'event_name': data.get('event_name'),
                'event_type': data.get('event_type'),
                'event_theme': data.get('event_theme'),
                'event_color': data.get('event_color'),
                'package_id': data.get('package_id'),
                'schedule': data.get('schedule'),
                'start_time': data.get('start_time'),
                'end_time': data.get('end_time'),
                'status': data.get('status', 'Wishlist'),
                'onsite_firstname': data.get('onsite_firstname'),
                'onsite_lastname': data.get('onsite_lastname'),
                'onsite_contact': data.get('onsite_contact'),
                'onsite_address': data.get('onsite_address'),
                'total_price': data.get('total_price', 0),
                'booking_type': data.get('booking_type', 'Onsite')
            }

            # Package configuration data
            package_config = {
                'suppliers': data.get('suppliers', []),
                'outfits': data.get('outfits', []),
                'services': data.get('services', []),
                'additional_items': data.get('additional_items', [])
            }

            # Add event and its configurations
            events_id = add_event_item(**event_data, **package_config)

            return jsonify({
                'success': True,
                'message': 'Wishlist added successfully',
                'events_id': events_id
            }), 201
        except Exception as e:
            logger.error(f"Error adding wishlist: {str(e)}")
            return jsonify({
                'success': False,
                'message': f'Error adding wishlist: {str(e)}'
            }), 500

    @app.route('/available-suppliers', methods=['GET'])
    @jwt_required()
    def get_available_suppliers_route():
        try:
            suppliers = get_available_suppliers()
            return jsonify(suppliers), 200
        except Exception as e:
            logger.error(f"Error fetching available suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching available suppliers'}), 500

    @app.route('/available-venues', methods=['GET'])
    @jwt_required()
    def get_available_venues_route():
        try:
            venues = get_available_venues()
            return jsonify(venues), 200
        except Exception as e:
            logger.error(f"Error fetching available venues: {e}")
            return jsonify({'message': 'An error occurred while fetching available venues'}), 500

    @app.route('/available-gown-packages', methods=['GET'])
    @jwt_required()
    def get_available_gown_packages_route():
        try:
            gown_packages = get_available_gown_packages()
            return jsonify(gown_packages), 200
        except Exception as e:
            logger.error(f"Error fetching available gown packages: {e}")
            return jsonify({'message': 'An error occurred while fetching available gown packages'}), 500

    @app.route('/packages/<int:package_id>', methods=['GET'])
    @jwt_required()
    def get_package_details(package_id):
        try:
            package = get_package_details_by_id(package_id)  # Implement this function to fetch package details
            if not package:
                return jsonify({'message': 'Package not found'}), 404
            return jsonify(package), 200
        except Exception as e:
            logger.error(f"Error fetching package details: {e}")
            return jsonify({'message': 'An error occurred while fetching package details'}), 500


    @app.route('/created-venues', methods=['GET'])
    @jwt_required()
    def get_created_venues():
        try:
            venues = get_all_venues()
            return jsonify(venues), 200
        except Exception as e:
            logger.error(f"Error fetching venues: {e}")
            return jsonify({'message': 'An error occurred while fetching venues'}), 500

    @app.route('/created-suppliers', methods=['GET'])
    @jwt_required()
    def get_created_suppliers():
        try:
            suppliers = get_suppliers_with_users()
            return jsonify(suppliers), 200
        except Exception as e:
            logger.error(f"Error fetching suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching suppliers'}), 500

    @app.route('/created-gown-packages', methods=['GET'])
    @jwt_required()
    def get_created_gown_packages():
        try:
            packages = get_all_gown_packages()
            return jsonify(packages), 200
        except Exception as e:
            logger.error(f"Error fetching gown packages: {e}")
            return jsonify({'message': 'An error occurred while fetching gown packages'}), 500

    @app.route('/booked-wishlist', methods=['GET'])
    @jwt_required()
    def get_booked_wishlist():
        try:
            email = get_jwt_identity()
            userid = get_user_id_by_email(email)
            
            if userid is None:
                return jsonify({'message': 'User not found'}), 404

            booked_wishlist = get_all_booked_wishlist()
            return jsonify(booked_wishlist), 200
        except Exception as e:
            logger.error(f"Error fetching booked wishlist: {str(e)}")
            return jsonify({'message': f'Error fetching wishlist: {str(e)}'}), 500

    @app.route('/events/all', methods=['GET', 'OPTIONS'])
    @jwt_required()
    def get_all_events_route():
        if request.method == 'OPTIONS':
            response = make_response()
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response

        try:
            events = get_all_events()
            # Convert dates to ISO format for JSON serialization
            for event in events:
                if event['schedule']:
                    event['schedule'] = event['schedule'].isoformat()
                if event['start_time']:
                    event['start_time'] = event['start_time'].isoformat()
                if event['end_time']:
                    event['end_time'] = event['end_time'].isoformat()
            
            response = jsonify(events)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response

        except Exception as e:
            logger.error(f"Error in get_all_events_route: {str(e)}")
            response = jsonify({'message': 'An error occurred while fetching events'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/events/date/<date>', methods=['GET'])
    @jwt_required()
    def get_events_by_date_route(date):
        try:
            events = get_events_by_date(date)
            return jsonify([{
                'events_id': event['events_id']
            } for event in events]), 200
        except Exception as e:
            logger.error(f"Error in get_events_by_date_route: {str(e)}")
            return jsonify({'message': 'An error occurred while fetching events for date'}), 500

    @app.route('/events/<int:event_id>', methods=['GET'])
    @jwt_required()
    def get_event_route(event_id):
        try:
            # Get detailed event information with all inclusions
            event_details = get_event_details(event_id)
            
            if not event_details:
                return jsonify({'message': 'Event not found'}), 404
            
            # Get any wishlist package for this event
            if 'wishlist_id' in event_details:
                wishlist_details = get_wishlist_package(event_details['wishlist_id'])
                if wishlist_details:
                    event_details['wishlist_package'] = wishlist_details
            
            # Format time and decimal values for JSON serialization
            if 'start_time' in event_details and event_details['start_time'] is not None:
                event_details['start_time'] = event_details['start_time'].strftime('%H:%M:%S')
                
            if 'end_time' in event_details and event_details['end_time'] is not None:
                event_details['end_time'] = event_details['end_time'].strftime('%H:%M:%S')
                
            if 'total_price' in event_details and event_details['total_price'] is not None:
                event_details['total_price'] = float(event_details['total_price'])
            
            # Make sure all pricing data is properly formatted for the frontend
            if 'suppliers' in event_details and event_details['suppliers']:
                for supplier in event_details['suppliers']:
                    if 'price' in supplier and supplier['price'] is not None:
                        supplier['price'] = float(supplier['price'])
                        
            if 'outfits' in event_details and event_details['outfits']:
                for outfit in event_details['outfits']:
                    if 'price' in outfit and outfit['price'] is not None:
                        outfit['price'] = float(outfit['price'])
                        
            if 'venue' in event_details and event_details['venue']:
                if 'venue_price' in event_details['venue'] and event_details['venue']['venue_price'] is not None:
                    event_details['venue']['venue_price'] = float(event_details['venue']['venue_price'])
            
            return jsonify(event_details), 200
        except Exception as e:
            logger.error(f"Error in get_event_route: {str(e)}")
            return jsonify({'message': f'An error occurred while fetching event details: {str(e)}'}), 500

    @app.route('/events-by-month', methods=['GET'])
    def get_events_by_month_route():
        try:
            result = get_events_by_month_and_type()
            return jsonify(result), 200
        except Exception as e:
            print(f"Error in get_events_by_month_route: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @app.route('/toggle-supplier-status/<int:supplier_id>', methods=['PUT'])
    @jwt_required()
    def toggle_supplier_status(supplier_id):
        try:
            from .models import toggle_supplier_status as toggle_status
            result = toggle_status(supplier_id)
            if isinstance(result, tuple) and result[0] == "not_found":
                return jsonify({"message": "Supplier not found"}), 404
            return jsonify({
                'message': 'Supplier status updated successfully',
                'new_status': result
            }), 200
        except Exception as e:
            logger.error(f"Error updating supplier status: {e}")
            return jsonify({'message': 'An error occurred while updating supplier status'}), 500

    @app.route('/inactive-suppliers', methods=['GET'])
    @jwt_required()
    def get_inactive_suppliers_route():
        try:
            suppliers = get_inactive_suppliers()
            return jsonify(suppliers), 200
        except Exception as e:
            logger.error(f"Error fetching inactive suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching inactive suppliers'}), 500

    @app.route('/inactive-additional-services', methods=['GET'])
    @jwt_required()
    def get_inactive_additional_services_route():
        try:
            services = get_inactive_additional_services()
            return jsonify(services), 200
        except Exception as e:
            logger.error(f"Error fetching inactive additional services: {e}")
            return jsonify({'message': 'An error occurred while fetching inactive additional services'}), 500

    @app.route('/toggle-additional-service-status/<int:service_id>', methods=['PUT'])
    @jwt_required()
    def toggle_additional_service_status_route(service_id):
        try:
            success = toggle_additional_service_status(service_id)
            if success:
                return jsonify({'message': 'Additional service status updated successfully'}), 200
            else:
                return jsonify({'message': 'Failed to update additional service status'}), 400
        except Exception as e:
            logger.error(f"Error updating additional service status: {e}")
            return jsonify({'message': 'An error occurred while updating additional service status'}), 500

    @app.route('/update-additional-service-price/<int:service_id>', methods=['PUT'])
    @jwt_required()
    def update_additional_service_price_route(service_id):
        try:
            data = request.get_json()
            price = data.get('price')
            
            if price is None:
                return jsonify({"message": "Price is required"}), 400
                
            success = update_additional_service_price(service_id, price)
            if success:
                return jsonify({"message": "Additional service price updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update additional service price"}), 400
        except Exception as e:
            logger.error(f"Error updating additional service price: {e}")
            return jsonify({"message": "An error occurred while updating additional service price"}), 500

    @app.route('/add-supplier-social-media', methods=['POST'])
    @jwt_required()
    def add_supplier_social_media_route():
        try:
            data = request.get_json()
            supplier_id = data.get('supplier_id')
            platform = data.get('platform')
            handle = data.get('handle')
            url = data.get('url')

            if not all([supplier_id, platform, handle]):
                return jsonify({'error': 'Missing required fields'}), 400

            success, social_media_id = add_supplier_social_media(supplier_id, platform, handle, url)

            if success:
                return jsonify({
                    'message': 'Social media added successfully',
                    'social_media_id': social_media_id
                }), 200
            else:
                return jsonify({'error': 'Failed to add social media'}), 500

        except Exception as e:
            logger.error(f"Error adding social media: {str(e)}")
            return jsonify({'error': 'Failed to add social media'}), 500

    @app.route('/api/supplier/<int:supplier_id>/social-media', methods=['GET', 'OPTIONS'])
    @jwt_required()  # Add JWT protection
    def get_supplier_social_media_route(supplier_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            logger.info(f"Fetching social media for supplier_id: {supplier_id}")
            social_media = get_supplier_social_media(supplier_id)
            logger.info(f"Found social media: {social_media}")
            response = jsonify(social_media)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response
        except Exception as e:
            logger.error(f"Error fetching social media: {str(e)}")
            response = jsonify({'error': str(e)})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/inactive-packages', methods=['GET'])
    @jwt_required()
    def get_inactive_packages_route():
        try:
            from . import models  # Import models at function level to avoid circular imports
            packages = models.get_inactive_packages()
            return jsonify(packages)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/toggle-package-status/<int:package_id>', methods=['PUT'])
    @jwt_required()
    def toggle_package_status_route(package_id):
        try:
            from . import models  # Import models at function level to avoid circular imports
            success = models.toggle_package_status(package_id)
            if success:
                return jsonify({'message': 'Package status updated successfully'}), 200
            else:
                return jsonify({'error': 'Failed to update package status'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/inactive-gown-packages', methods=['GET'])
    @jwt_required()
    def get_inactive_gown_packages_route():
        try:
            logger.info("Fetching inactive gown packages")
            from . import models  # Import models at function level to avoid circular imports
            packages = models.get_inactive_packages()
            logger.info(f"Found {len(packages)} inactive packages")
            return jsonify(packages)
        except Exception as e:
            logger.error(f"Error fetching inactive packages: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @app.route('/toggle-gown-package-status/<int:package_id>', methods=['PUT'])
    @jwt_required()
    def toggle_gown_package_status_route(package_id):
        try:
            logger.info(f"Toggling status for package {package_id}")
            from . import models  # Import models at function level to avoid circular imports
            success = models.toggle_package_status(package_id)
            if success:
                logger.info(f"Successfully toggled status for package {package_id}")
                return jsonify({'message': 'Package status updated successfully'}), 200
            else:
                logger.error(f"Failed to toggle status for package {package_id}")
                return jsonify({'error': 'Failed to update package status'}), 400
        except Exception as e:
            logger.error(f"Error toggling package status: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @app.route('/event/<int:events_id>/outfits', methods=['GET'])
    @jwt_required()
    def get_event_outfits_route(events_id):
        try:
            outfits = get_event_outfits(events_id)
            return jsonify(outfits)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/event/<int:events_id>/outfit', methods=['POST'])
    @jwt_required()
    def add_event_outfit_route(events_id):
        try:
            data = request.get_json()
            outfit_type = data.get('type')
            
            if outfit_type == 'individual_outfit':
                outfit_id = data.get('outfit_id')
                event_outfit_id = add_event_outfit(events_id, outfit_type, outfit_id=outfit_id)
            elif outfit_type == 'outfit_package':
                gown_package_id = data.get('gown_package_id')
                event_outfit_id = add_event_outfit(events_id, outfit_type, gown_package_id=gown_package_id)
            else:
                return jsonify({'error': 'Invalid outfit type'}), 400

            if event_outfit_id:
                return jsonify({'event_outfit_id': event_outfit_id}), 201
            else:
                return jsonify({'error': 'Failed to add outfit'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/events/<int:events_id>/modify-outfit', methods=['POST'])
    def modify_event_outfit(events_id):
        try:
            data = request.get_json()
            outfit_id = data.get('outfit_id')
            gown_package_id = data.get('gown_package_id')
            modification_type = data.get('modification_type')
            original_price = data.get('original_price')
            modified_price = data.get('modified_price')
            remarks = data.get('remarks')

            success = track_outfit_modification(
                events_id, outfit_id, gown_package_id,
                modification_type, original_price,
                modified_price, remarks
            )

            if success:
                return jsonify({'message': 'Outfit modification tracked successfully'}), 200
            return jsonify({'error': 'Failed to track outfit modification'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/events/<int:events_id>/modify-individual-outfit', methods=['POST'])
    def modify_individual_outfit(events_id):
        try:
            outfit_data = request.get_json()
            success = track_individual_outfit_modification(events_id, outfit_data)

            if success:
                return jsonify({'message': 'Individual outfit modification tracked successfully'}), 200
            return jsonify({'error': 'Failed to track individual outfit modification'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/events/<int:events_id>/modify-additional-service', methods=['POST'])
    def modify_additional_service(events_id):
        try:
            data = request.get_json()
            service_id = data.get('service_id')
            modification_type = data.get('modification_type')
            original_price = data.get('original_price')
            modified_price = data.get('modified_price')
            remarks = data.get('remarks')

            success = track_additional_service_modification(
                events_id, service_id, modification_type,
                original_price, modified_price, remarks
            )

            if success:
                return jsonify({'message': 'Additional service modification tracked successfully'}), 200
            return jsonify({'error': 'Failed to track additional service modification'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/wishlist-packages', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def create_wishlist_package_route():
        if request.method == 'OPTIONS':
            # Handle preflight request
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'POST,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        try:
            # Get user ID from token
            email = get_jwt_identity()
            userid = get_user_id_by_email(email)
            
            if userid is None:
                response = jsonify({
                    'success': False,
                    'message': 'User not found'
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 404

            data = request.get_json()

            # Create wishlist package and its related data
            wishlist_id = create_wishlist_package(
                events_id=data.get('events_id'),
                package_data=data
            )

            if wishlist_id:
                response = jsonify({
                    'success': True,
                    'message': 'Wishlist package created successfully',
                    'wishlist_id': wishlist_id
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 201
            else:
                response = jsonify({
                    'success': False,
                    'message': 'Failed to create wishlist package'
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 500

        except Exception as e:
            logger.error(f"Error creating wishlist package: {str(e)}")
            response = jsonify({
                'success': False,
                'message': f'Error creating wishlist package: {str(e)}'
            })
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/wishlist-packages/<int:wishlist_id>', methods=['PUT', 'OPTIONS'])
    @jwt_required()
    def update_wishlist_package_route(wishlist_id):
        if request.method == 'OPTIONS':
            # Handle preflight request
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'PUT,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        try:
            # Get user ID from token
            email = get_jwt_identity()
            userid = get_user_id_by_email(email)
            
            if userid is None:
                response = jsonify({
                    'success': False,
                    'message': 'User not found'
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 404

            data = request.get_json()
            
            # Log the data received for debugging
            logger.info(f"Updating wishlist package {wishlist_id} with data: {data}")
            
            # Verify venue_status is received properly
            venue_status = data.get('venue_status', 'Pending')
            logger.info(f"Venue status received: {venue_status}")
            
            # Update wishlist package and its related data
            result = update_wishlist_package(wishlist_id, data)
            
            if result:
                response = jsonify({
                    'success': True,
                    'message': 'Wishlist package updated successfully',
                    'wishlist_id': wishlist_id,
                    'venue_status': venue_status  # Include this in the response
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            else:
                response = jsonify({
                    'success': False,
                    'message': 'Failed to update wishlist package'
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 500
                
        except Exception as e:
            logging.error(f"Error updating wishlist package: {str(e)}")
            response = jsonify({
                'success': False,
                'message': f'Error updating wishlist package: {str(e)}'
            })
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/events/schedules', methods=['GET', 'OPTIONS'])
    @cross_origin(supports_credentials=True, origins=['http://localhost:5173'])
    def get_event_schedules():
        if request.method == 'OPTIONS':
            response = make_response()
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response

        try:
            # Get all events with their schedules
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("""
                SELECT e.events_id, e.event_name, e.schedule, e.start_time, e.end_time, e.status
                FROM events e
                WHERE e.schedule IS NOT NULL
                ORDER BY e.schedule
            """)
            events = cur.fetchall()
            cur.close()
            conn.close()

            # Format the response
            schedules = []
            for event in events:
                schedules.append({
                    'events_id': event[0],
                    'event_name': event[1],
                    'schedule': event[2].strftime('%Y-%m-%d') if event[2] else None,
                    'start_time': event[3].strftime('%H:%M') if event[3] else None,
                    'end_time': event[4].strftime('%H:%M') if event[4] else None,
                    'status': event[5]
                })

            return jsonify(schedules)

        except Exception as e:
            app.logger.error(f"Error fetching event schedules: {str(e)}")
            return jsonify({'error': str(e)}), 500

    @app.route('/additional-services', methods=['GET', 'OPTIONS'])
    @jwt_required()
    def get_additional_services():
        conn = None
        cursor = None
        
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT 
                    add_service_id,
                    add_service_name,
                    add_service_description,
                    add_service_price,
                    status
                FROM additional_services
                WHERE status = 'Active'
                ORDER BY add_service_name
            """)
            
            services = [{
                'add_service_id': row[0],
                'add_service_name': row[1],
                'add_service_description': row[2],
                'add_service_price': float(row[3]) if row[3] else 0,
                'status': row[4]
            } for row in cursor.fetchall()]
            
            response = jsonify(services)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        except Exception as e:
            logger.error(f"Error getting additional services: {str(e)}")
            response = jsonify({
                'success': False,
                'message': str(e)
            })
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @app.route('/api/wishlist-suppliers/<int:wishlist_supplier_id>', methods=['PUT'])
    @jwt_required()
    def update_wishlist_supplier_status_route(wishlist_supplier_id):
        try:
            data = request.get_json()
            status = data.get('status')
            
            if not status:
                return jsonify({'message': 'Status is required'}), 400
                
            success, message = update_wishlist_supplier_status(wishlist_supplier_id, status)
            
            if success:
                return jsonify({'message': message}), 200
            else:
                return jsonify({'message': message}), 400
                
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @app.route('/api/wishlist-outfits/<int:wishlist_outfit_id>', methods=['PUT', 'OPTIONS'])
    @jwt_required()
    def update_wishlist_outfit_status_route(wishlist_outfit_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'PUT,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            data = request.get_json()
            status = data.get('status')
            
            if not status:
                return jsonify({'message': 'Status is required'}), 400
                
            success, message = update_wishlist_outfit_status(wishlist_outfit_id, status)
            
            if success:
                response = jsonify({'message': message})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            else:
                response = jsonify({'message': message})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 400
                
        except Exception as e:
            response = jsonify({'message': str(e)})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/api/wishlist-additional-services/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_wishlist_additional_service_status_route(id):
        try:
            data = request.get_json()
            status = data.get('status')
            
            if not status:
                return jsonify({'message': 'Status is required'}), 400
                
            success, message = update_wishlist_additional_service_status(id, status)
            
            if success:
                return jsonify({'message': message}), 200
            else:
                return jsonify({'message': message}), 400
                
        except Exception as e:
            return jsonify({'message': str(e)}), 500

    @app.route('/api/wishlist-additional-services/update-status', methods=['PUT', 'OPTIONS'])
    @jwt_required()
    def update_wishlist_additional_service_status_by_ids_route():
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'PUT,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            data = request.get_json()
            wishlist_id = data.get('wishlist_id')
            add_service_id = data.get('add_service_id')
            status = data.get('status')
            
            if not all([wishlist_id, add_service_id, status]):
                return jsonify({'message': 'Missing required fields'}), 400
                
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE wishlist_additional_services SET status = %s WHERE wishlist_id = %s AND add_service_id = %s",
                    (status, wishlist_id, add_service_id)
                )
                conn.commit()
                response = jsonify({'message': 'Status updated successfully'})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            except Exception as e:
                logger.error(f"Error updating wishlist additional service status: {e}")
                conn.rollback()
                return jsonify({'message': 'Failed to update status'}), 500
            finally:
                cursor.close()
                conn.close()
                
        except Exception as e:
            logger.error(f"Error in update_wishlist_additional_service_status_by_ids_route: {e}")
            return jsonify({'message': 'An error occurred while updating status'}), 500

    @app.route('/events/<int:events_id>/status', methods=['PUT'])
    @jwt_required()
    def update_event_status(events_id):
        try:
            data = request.get_json()
            new_status = data.get('status')
            
            if not new_status:
                return jsonify({
                    'success': False,
                    'message': 'Status is required'
                }), 400

            conn = get_db_connection()
            cursor = conn.cursor()
            
            try:
                cursor.execute("""
                    UPDATE events 
                    SET status = %s 
                    WHERE events_id = %s 
                    RETURNING events_id
                """, (new_status, events_id))
                
                updated_id = cursor.fetchone()
                conn.commit()
                
                if updated_id:
                    return jsonify({
                        'success': True,
                        'message': f'Event status updated to {new_status}'
                    }), 200
                else:
                    return jsonify({
                        'success': False,
                        'message': 'Event not found'
                    }), 404
                    
            except Exception as e:
                conn.rollback()
                return jsonify({
                    'success': False,
                    'message': str(e)
                }), 500
            finally:
                cursor.close()
                conn.close()
                
        except Exception as e:
            return jsonify({
                'success': False,
                'message': str(e)
            }), 500

    @app.route('/api/wishlist-outfits-direct/<int:wishlist_outfit_id>', methods=['DELETE', 'OPTIONS'])
    @jwt_required()
    def delete_wishlist_outfit_direct_route(wishlist_outfit_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'DELETE,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            success = delete_wishlist_outfit_direct(wishlist_outfit_id)
            
            if success:
                response = jsonify({'message': 'Outfit deleted successfully'})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            else:
                return jsonify({'message': 'Failed to delete outfit'}), 500
                
        except Exception as e:
            logger.error(f"Error deleting wishlist outfit: {e}")
            return jsonify({'message': 'An error occurred while deleting outfit'}), 500

    @app.route('/api/wishlist-services-direct/<int:service_id>', methods=['DELETE', 'OPTIONS'])
    @jwt_required()
    def delete_wishlist_service_direct_route(service_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'DELETE,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            success = delete_wishlist_service_direct(service_id)
            
            if success:
                response = jsonify({'message': 'Service deleted successfully'})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            else:
                return jsonify({'message': 'Failed to delete service'}), 500
                
        except Exception as e:
            logger.error(f"Error deleting wishlist service: {e}")
            return jsonify({'message': 'An error occurred while deleting service'}), 500

    @app.route('/api/wishlist-suppliers-direct/<int:wishlist_supplier_id>', methods=['DELETE', 'OPTIONS'])
    @jwt_required()
    def delete_wishlist_supplier_direct_route(wishlist_supplier_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'DELETE,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            success = delete_wishlist_supplier_direct(wishlist_supplier_id)
            
            if success:
                response = jsonify({'message': 'Supplier deleted successfully'})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            else:
                return jsonify({'message': 'Failed to delete supplier'}), 500
                
        except Exception as e:
            logger.error(f"Error deleting wishlist supplier: {e}")
            return jsonify({'message': 'An error occurred while deleting supplier'}), 500

    @app.route('/api/wishlist-venues-direct/<int:wishlist_venue_id>', methods=['DELETE', 'OPTIONS'])
    @jwt_required()
    def delete_wishlist_venue_direct_route(wishlist_venue_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'DELETE,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            success = delete_wishlist_venue_direct(wishlist_venue_id)
            
            if success:
                response = jsonify({'message': 'Venue deleted successfully'})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            else:
                return jsonify({'message': 'Failed to delete venue'}), 500
                
        except Exception as e:
            logger.error(f"Error deleting wishlist venue: {e}")
            return jsonify({'message': 'An error occurred while deleting venue'}), 500

    @app.route('/api/wishlist-packages/<int:wishlist_id>/venue-status', methods=['PUT', 'OPTIONS'])
    @jwt_required()
    def update_wishlist_venue_status_route(wishlist_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'PUT,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            data = request.get_json()
            venue_status = data.get('venue_status')
            
            if not venue_status:
                return jsonify({'message': 'Venue status is required'}), 400
                
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute(
                    "UPDATE wishlist_packages SET venue_status = %s WHERE wishlist_id = %s",
                    (venue_status, wishlist_id)
                )
                conn.commit()
                response = jsonify({'message': 'Venue status updated successfully', 'success': True})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            except Exception as e:
                logger.error(f"Error updating wishlist venue status: {e}")
                conn.rollback()
                return jsonify({'message': 'Failed to update venue status', 'success': False}), 500
            finally:
                cursor.close()
                conn.close()
                
        except Exception as e:
            logger.error(f"Error in update_wishlist_venue_status_route: {e}")
            return jsonify({'message': 'An error occurred while updating venue status', 'success': False}), 500

    @app.route('/api/upcoming-events', methods=['GET'])
    @jwt_required()
    def get_upcoming_events():
        try:
            events = fetch_upcoming_events()
            return jsonify(events)
        except Exception as e:
            logger.error(f"Error in get_upcoming_events route: {str(e)}")
            return jsonify({'error': str(e)}), 500
    
    @app.route('/api/check-events-status', methods=['GET'])
    @jwt_required()
    def check_events_status():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT events_id, event_name, status
                FROM events
                ORDER BY events_id
            """)
            
            events = []
            for row in cursor.fetchall():
                events.append({
                    'events_id': row[0],
                    'event_name': row[1],
                    'status': row[2]
                })
            
            cursor.close()
            conn.close()
            
            return jsonify(events)
        except Exception as e:
            logger.error(f"Error in check_events_status route: {str(e)}")
            return jsonify({'error': str(e)}), 500

    # Invoice related endpoints
    @app.route('/api/invoices', methods=['POST'])
    @jwt_required()
    def create_invoice_route():
        try:
            data = request.get_json()
            
            required_fields = ['events_id', 'invoice_number', 'invoice_date', 
                              'total_amount', 'final_amount', 'status']
            
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Missing required fields"}), 400
            
            # Check if an invoice already exists for this event
            existing_invoice = get_invoice_by_event(data['events_id'])
            if existing_invoice:
                return jsonify({
                    "message": "Invoice already exists for this event",
                    "invoice": existing_invoice
                }), 200
            
            # Create invoice if none exists
            invoice = create_invoice(data)
            
            if invoice:
                return jsonify(invoice), 201
            else:
                return jsonify({"error": "Failed to create invoice"}), 500
        except Exception as e:
            logger.error(f"Error creating invoice: {e}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/invoices/<int:invoice_id>', methods=['GET'])
    @jwt_required()
    def get_invoice_route(invoice_id):
        try:
            invoice = get_invoice_by_id(invoice_id)
            
            if not invoice:
                return jsonify({"error": "Invoice not found"}), 404
            
            return jsonify(invoice), 200
        except Exception as e:
            logger.error(f"Error retrieving invoice: {e}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/invoices/event/<int:event_id>', methods=['GET', 'OPTIONS'])
    @jwt_required(optional=True)  # Make JWT optional to handle OPTIONS requests
    def get_invoice_by_event_route(event_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        try:
            # Only verify JWT for actual data requests
            verify_jwt_in_request()
            
            invoice = get_invoice_by_event(event_id)
            
            if not invoice:
                response = jsonify({"error": "No invoice found for this event"})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 404
            
            response = jsonify(invoice)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        except Exception as e:
            logger.error(f"Error retrieving invoice for event: {e}")
            response = jsonify({"error": str(e)})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500
    
    @app.route('/api/invoices/<int:invoice_id>', methods=['PUT'])
    @jwt_required()
    def update_invoice_route(invoice_id):
        try:
            data = request.get_json()
            
            # Validate input data
            required_fields = []  # No strictly required fields for update
            missing_fields = [field for field in required_fields if field not in data]
            
            if missing_fields:
                return jsonify({
                    "error": f"Missing required fields: {', '.join(missing_fields)}"
                }), 400
                
            # Get the current invoice to check if it already has a discount
            current_invoice = get_invoice_by_id(invoice_id)
            if not current_invoice:
                return jsonify({"error": "Invoice not found"}), 404
                
            # If trying to update discount and invoice already has a discount set, prevent it
            if ('discount_id' in data or 'discount_amount' in data) and current_invoice.get('discount_id') is not None:
                return jsonify({
                    "error": "A discount has already been applied to this invoice and cannot be changed"
                }), 400
            
            # Handle discount fields
            if 'discount_id' in data:
                if data['discount_id'] == '' or data['discount_id'] is None:
                    data['discount_id'] = None
                    # If removing discount, also set discount_amount to 0
                    if 'discount_amount' not in data:
                        data['discount_amount'] = 0
            
            updated_invoice = update_invoice(invoice_id, data)
            
            if not updated_invoice:
                return jsonify({"error": "Invoice not found or no fields to update"}), 404
            
            return jsonify(updated_invoice), 200
        except Exception as e:
            logger.error(f"Error updating invoice: {e}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/payments', methods=['POST'])
    @jwt_required()
    def record_payment_route():
        try:
            data = request.get_json()
            
            required_fields = ['invoice_id', 'amount', 'payment_method', 
                              'payment_date', 'recorded_by']
            
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Missing required fields"}), 400
            
            payment = record_payment(data)
            
            if payment:
                return jsonify(payment), 201
            else:
                return jsonify({"error": "Failed to record payment"}), 500
        except Exception as e:
            logger.error(f"Error recording payment: {e}")
            return jsonify({"error": str(e)}), 500
    
    @app.route('/api/payments/invoice/<int:invoice_id>', methods=['GET'])
    @jwt_required()
    def get_payments_by_invoice_route(invoice_id):
        try:
            payments = get_payments_by_invoice(invoice_id)
            return jsonify(payments), 200
        except Exception as e:
            logger.error(f"Error retrieving payments: {e}")
            return jsonify({"error": str(e)}), 500

    # Route without the /api prefix for compatibility with frontend
    @app.route('/invoices/event/<int:event_id>', methods=['GET', 'OPTIONS'])
    @jwt_required(optional=True)
    def get_invoice_by_event_route_compat(event_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        try:
            # Verify JWT for actual data requests
            verify_jwt_in_request()
            
            invoice = get_invoice_by_event(event_id)
            
            if not invoice:
                response = jsonify({"error": "No invoice found for this event"})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 404
            
            response = jsonify(invoice)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        except Exception as e:
            logger.error(f"Error retrieving invoice for event: {e}")
            response = jsonify({"error": str(e)})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    # Function to initialize invoice and payment tables
    @app.route('/api/initialize-invoice-tables', methods=['POST'])
    @jwt_required()
    def initialize_invoice_tables_route():
        conn = None
        try:
            # Log operation start with more details
            logger.info("Starting invoice tables initialization with detailed logging")
            
            # Get a database connection and test it
            try:
                conn = db.get_db_connection()
                logger.info("Successfully connected to database")
            except Exception as conn_error:
                logger.error(f"Database connection error: {conn_error}")
                return jsonify({"error": f"Database connection failed: {str(conn_error)}"}), 500
            
            cursor = conn.cursor()
            logger.info("Database cursor created")
            
            # Create invoices table if not exists
            try:
                logger.info("Attempting to create invoices table")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS invoices (
                        invoice_id SERIAL PRIMARY KEY,
                        events_id INTEGER NOT NULL,
                        invoice_number VARCHAR(50) NOT NULL,
                        invoice_date DATE NOT NULL,
                        total_amount DECIMAL(10, 2) NOT NULL,
                        discount_amount DECIMAL(10, 2) DEFAULT 0.00,
                        final_amount DECIMAL(10, 2) NOT NULL,
                        status VARCHAR(20) NOT NULL DEFAULT 'Unpaid',
                        notes TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
                logger.info("Invoices table created or already exists")
            except Exception as table_error:
                logger.error(f"Error creating invoices table: {table_error}")
                return jsonify({"error": f"Failed to create invoices table: {str(table_error)}"}), 500
            
            # Create payments table if not exists
            try:
                logger.info("Attempting to create payments table")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS payments (
                        payment_id SERIAL PRIMARY KEY,
                        invoice_id INTEGER NOT NULL,
                        amount DECIMAL(10, 2) NOT NULL,
                        payment_method VARCHAR(50) NOT NULL,
                        reference_number VARCHAR(100),
                        payment_date DATE NOT NULL,
                        recorded_by VARCHAR(100) NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
                logger.info("Payments table created or already exists")
            except Exception as table_error:
                logger.error(f"Error creating payments table: {table_error}")
                return jsonify({"error": f"Failed to create payments table: {str(table_error)}"}), 500
            
            # Create indexes - only if tables exist
            try:
                logger.info("Attempting to create index on invoices table")
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_invoices_events_id ON invoices(events_id)
                """)
                conn.commit()
                logger.info("Invoice index created or already exists")
            except Exception as index_error:
                logger.error(f"Error creating invoice index: {index_error}")
                # Non-fatal error, continue
            
            try:
                logger.info("Attempting to create index on payments table")
                cursor.execute("""
                    CREATE INDEX IF NOT EXISTS idx_payments_invoice_id ON payments(invoice_id)
                """)
                conn.commit()
                logger.info("Payment index created or already exists")
            except Exception as index_error:
                logger.error(f"Error creating payment index: {index_error}")
                # Non-fatal error, continue
            
            # Verify tables were created by checking if they exist
            try:
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_schema = 'public' 
                        AND table_name = 'invoices'
                    );
                """)
                invoices_exist = cursor.fetchone()[0]
                
                cursor.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE table_schema = 'public' 
                        AND table_name = 'payments'
                    );
                """)
                payments_exist = cursor.fetchone()[0]
                
                if invoices_exist and payments_exist:
                    logger.info("Successfully verified that both tables exist")
                else:
                    logger.warning(f"Table verification failed: invoices={invoices_exist}, payments={payments_exist}")
            except Exception as verify_error:
                logger.error(f"Error verifying tables: {verify_error}")
            
            return jsonify({
                "message": "Invoice tables initialized successfully",
                "tables_verified": {
                    "invoices": invoices_exist,
                    "payments": payments_exist
                }
            }), 200
            
        except Exception as e:
            logger.error(f"Critical error initializing invoice tables: {e}")
            if conn:
                conn.rollback()
            return jsonify({"error": str(e)}), 500
        finally:
            if conn:
                conn.close()
                logger.info("Database connection closed")

    @app.route('/api/events/<int:event_id>', methods=['GET', 'OPTIONS'])
    @jwt_required(optional=True)  # Make JWT optional to handle OPTIONS requests
    def api_get_event_route(event_id):
        # Handle OPTIONS requests for CORS preflight
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        # This route handles GET requests for event details with CORS support
        try:
            # Only verify JWT for actual data requests
            verify_jwt_in_request()
            
            event_details = get_event_details(event_id)
            
            if not event_details:
                return jsonify({'message': 'Event not found'}), 404
            
            # Get any wishlist package for this event
            if 'wishlist_id' in event_details:
                wishlist_details = get_wishlist_package(event_details['wishlist_id'])
                if wishlist_details:
                    event_details['wishlist_package'] = wishlist_details
            
            # Format time and decimal values for JSON serialization
            if 'start_time' in event_details and event_details['start_time'] is not None:
                event_details['start_time'] = event_details['start_time'].strftime('%H:%M:%S')
                
            if 'end_time' in event_details and event_details['end_time'] is not None:
                event_details['end_time'] = event_details['end_time'].strftime('%H:%M:%S')
                
            if 'total_price' in event_details and event_details['total_price'] is not None:
                event_details['total_price'] = float(event_details['total_price'])
            
            # Make sure all pricing data is properly formatted for the frontend
            if 'suppliers' in event_details and event_details['suppliers']:
                for supplier in event_details['suppliers']:
                    if 'price' in supplier and supplier['price'] is not None:
                        supplier['price'] = float(supplier['price'])
                        
            if 'outfits' in event_details and event_details['outfits']:
                for outfit in event_details['outfits']:
                    if 'price' in outfit and outfit['price'] is not None:
                        outfit['price'] = float(outfit['price'])
                        
            if 'venue' in event_details and event_details['venue']:
                if 'venue_price' in event_details['venue'] and event_details['venue']['venue_price'] is not None:
                    event_details['venue']['venue_price'] = float(event_details['venue']['venue_price'])
            
            response = jsonify(event_details)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        except Exception as e:
            logger.error(f"Error in api_get_event_route: {str(e)}")
            response = jsonify({'message': f'An error occurred while fetching event details: {str(e)}'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/api/invoices/event/<int:event_id>', methods=['GET', 'OPTIONS'])
    @jwt_required(optional=True)  # Make JWT optional to handle OPTIONS requests
    def get_invoice_by_event_route_api(event_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        try:
            # Verify JWT for actual data requests
            verify_jwt_in_request()
            
            invoice = get_invoice_by_event(event_id)
            
            if not invoice:
                response = jsonify({"error": "No invoice found for this event"})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 404
            
            response = jsonify(invoice)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        except Exception as e:
            logger.error(f"Error retrieving invoice for event: {e}")
            response = jsonify({"error": str(e)})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500
    
    # Add a route without the /api prefix for compatibility with frontend
    @app.route('/invoices/event/<int:event_id>', methods=['GET', 'OPTIONS'])
    @jwt_required(optional=True)  # Make JWT optional to handle OPTIONS requests
    def get_invoice_by_event_route_compat_v2(event_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        try:
            # Verify JWT for actual data requests
            verify_jwt_in_request()
            
            invoice = get_invoice_by_event(event_id)
            
            if not invoice:
                response = jsonify({"error": "No invoice found for this event"})
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 404
            
            response = jsonify(invoice)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
        except Exception as e:
            logger.error(f"Error retrieving invoice for event: {e}")
            response = jsonify({"error": str(e)})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    @app.route('/api/users/<int:userid>', methods=['GET', 'OPTIONS'])
    @jwt_required(optional=True)  # Make JWT optional to handle OPTIONS requests
    def get_user_by_id_route(userid):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            return response, 200
            
        try:
            conn = db.get_db_connection()
            cursor = conn.cursor()
            
            # Query to get user details by userid
            query = """
            SELECT userid, firstname, lastname, email, contactnumber, user_type, user_img, address, username
            FROM users
            WHERE userid = %s
            """
            cursor.execute(query, (userid,))
            user_data = cursor.fetchone()
            
            if not user_data:
                return jsonify({"message": "User not found"}), 404
                
            columns = [desc[0] for desc in cursor.description]
            user_dict = dict(zip(columns, user_data))
            
            # Remove password from the result
            if 'password' in user_dict:
                del user_dict['password']
            
            return jsonify(user_dict), 200
            
        except Exception as e:
            logger.error(f"Error fetching user by id: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500
        finally:
            cursor.close()
            conn.close()

    # Discount routes
    @app.route('/api/discounts', methods=['GET'])
    def get_discounts():
        try:
            discounts = get_all_discounts()
            return jsonify({'success': True, 'data': discounts})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500

    @app.route('/api/discounts/active', methods=['GET'])
    def get_active_discounts():
        try:
            discounts = get_active_discounts()
            return jsonify({'success': True, 'data': discounts})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500

    @app.route('/api/discounts', methods=['POST'])
    def create_discount():
        try:
            data = request.json
            required_fields = ['name', 'type', 'value']
            for field in required_fields:
                if field not in data:
                    return jsonify({'success': False, 'error': f'Missing required field: {field}'}), 400

            conn = get_db_connection()
            cur = conn.cursor()
            
            cur.execute("""
                INSERT INTO discounts (name, description, type, value, start_date, end_date, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING discount_id
            """, (
                data['name'],
                data.get('description'),
                data['type'],
                data['value'],
                data.get('start_date'),
                data.get('end_date'),
                data.get('status', 'active')
            ))
            
            discount_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
            conn.close()
            
            return jsonify({'success': True, 'data': {'discount_id': discount_id}})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500

    @app.route('/api/discounts/<int:discount_id>', methods=['PUT'])
    def update_discount(discount_id):
        try:
            data = request.json
            conn = get_db_connection()
            cur = conn.cursor()
            
            update_fields = []
            params = []
            
            for field in ['name', 'description', 'type', 'value', 'start_date', 'end_date', 'status']:
                if field in data:
                    update_fields.append(f"{field} = %s")
                    params.append(data[field])
            
            if not update_fields:
                return jsonify({'success': False, 'error': 'No fields to update'}), 400
            
            params.append(discount_id)
            query = f"""
                UPDATE discounts 
                SET {', '.join(update_fields)}, updated_at = CURRENT_TIMESTAMP
                WHERE discount_id = %s
                RETURNING discount_id
            """
            
            cur.execute(query, params)
            result = cur.fetchone()
            
            if not result:
                return jsonify({'success': False, 'error': 'Discount not found'}), 404
            
            conn.commit()
            cur.close()
            conn.close()
            
            return jsonify({'success': True, 'data': {'discount_id': discount_id}})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500

    @app.route('/api/discounts/<int:discount_id>/status', methods=['PUT'])
    def toggle_discount_status(discount_id):
        try:
            data = request.json
            new_status = data.get('status')
            
            if new_status not in ['active', 'inactive']:
                return jsonify({'success': False, 'error': 'Invalid status'}), 400
            
            conn = get_db_connection()
            cur = conn.cursor()
            
            cur.execute("""
                UPDATE discounts 
                SET status = %s, updated_at = CURRENT_TIMESTAMP
                WHERE discount_id = %s
                RETURNING discount_id
            """, (new_status, discount_id))
            
            result = cur.fetchone()
            
            if not result:
                return jsonify({'success': False, 'error': 'Discount not found'}), 404
            
            conn.commit()
            cur.close()
            conn.close()
            
            return jsonify({'success': True, 'data': {'discount_id': discount_id, 'status': new_status}})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)}), 500

    @app.route('/api/invoices/<int:invoice_id>/discount', methods=['POST'])
    @jwt_required()
    def apply_discount_to_invoice(invoice_id):
        try:
            data = request.get_json()
            required_fields = ['discount_id', 'discount_amount']
            missing_fields = [field for field in required_fields if field not in data]
            
            if missing_fields:
                return jsonify({
                    "error": f"Missing required fields: {', '.join(missing_fields)}"
                }), 400
            
            # Get the current invoice to check if it already has a discount
            current_invoice = get_invoice_by_id(invoice_id)
            if not current_invoice:
                return jsonify({"error": "Invoice not found"}), 404
            
            # If invoice already has a discount set, prevent changing it
            if current_invoice.get('discount_id') is not None:
                return jsonify({
                    "error": "A discount has already been applied to this invoice and cannot be changed"
                }), 400
            
            # Create the update data
            update_data = {
                'discount_id': data['discount_id'],
                'discount_amount': data['discount_amount'],
                # Subtract discount amount from the final amount
                'final_amount': float(current_invoice['total_amount']) - float(data['discount_amount'])
            }
            
            # Update the invoice with the discount information
            updated_invoice = update_invoice(invoice_id, update_data)
            
            if not updated_invoice:
                return jsonify({"error": "Failed to update invoice with discount"}), 500
            
            return jsonify(updated_invoice), 200
            
        except Exception as e:
            logger.error(f"Error applying discount to invoice: {e}")
            return jsonify({"error": str(e)}), 500

    @app.route('/api/invoices/<int:invoice_id>/discount', methods=['DELETE'])
    @jwt_required()
    def remove_discount_from_invoice(invoice_id):
        try:
            # Get the current invoice
            current_invoice = get_invoice_by_id(invoice_id)
            if not current_invoice:
                return jsonify({"error": "Invoice not found"}), 404
            
            # If there's no discount to remove
            if current_invoice.get('discount_id') is None:
                return jsonify({"message": "No discount to remove"}), 200
            
            # Create the update data to remove the discount
            update_data = {
                'discount_id': None,
                'discount_amount': 0,
                # Reset the final amount to the total amount
                'final_amount': current_invoice['total_amount']
            }
            
            # Update the invoice to remove the discount
            updated_invoice = update_invoice(invoice_id, update_data)
            
            if not updated_invoice:
                return jsonify({"error": "Failed to remove discount from invoice"}), 500
            
            return jsonify(updated_invoice), 200
            
        except Exception as e:
            logger.error(f"Error removing discount from invoice: {e}")
            return jsonify({"error": str(e)}), 500

    @app.route('/api/discounts/inactive', methods=['GET'])
    def get_inactive_discounts():
        try:
            from app.db import get_inactive_discounts as fetch_inactive_discounts
            inactive_discounts = fetch_inactive_discounts()
            return jsonify({'success': True, 'data': inactive_discounts})
        except Exception as e:
            logger.error(f"Error fetching inactive discounts: {str(e)}")
            return jsonify({
                'success': False, 
                'error': str(e)
            }), 500

    @app.route('/api/wishlist-venues/<int:wishlist_venue_id>/status', methods=['PUT', 'OPTIONS'])
    @jwt_required()
    @cross_origin(supports_credentials=True)
    def update_wishlist_venue_route(wishlist_venue_id):
        if request.method == 'OPTIONS':
            return jsonify({'success': True}), 200

        try:
            current_user = get_jwt_identity()
            data = request.get_json()
            
            if not data or 'status' not in data:
                return jsonify({'success': False, 'error': 'Status is required'}), 400

            success, message = update_wishlist_venue_status(wishlist_venue_id, data['status'])
            if success:
                return jsonify({'success': True, 'message': message}), 200
            else:
                return jsonify({'success': False, 'error': message}), 400
        except Exception as e:
            print(f"Error updating venue status: {str(e)}")
            return jsonify({'success': False, 'error': str(e)}), 500

    @app.route('/api/wishlist-venues', methods=['POST', 'OPTIONS'])
    @jwt_required()
    def create_wishlist_venue_route():
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'POST,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            data = request.get_json()
            if not data:
                return jsonify({'message': 'No data provided'}), 400

            # Get user ID from token
            email = get_jwt_identity()
            userid = get_user_id_by_email(email)
            
            if userid is None:
                return jsonify({'message': 'User not found'}), 404

            # Create the wishlist venue
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO wishlist_venues (
                        wishlist_id, venue_id, price, remarks, status
                    ) VALUES (
                        %s, %s, %s, %s, %s
                    ) RETURNING wishlist_venue_id
                """, (
                    data.get('wishlist_id'),
                    data.get('venue_id'),
                    data.get('price', 0),
                    data.get('remarks', ''),
                    data.get('status', 'Pending')
                ))
                
                wishlist_venue_id = cursor.fetchone()[0]
                conn.commit()
                
                response = jsonify({
                    'success': True,
                    'message': 'Venue added successfully',
                    'wishlist_venue_id': wishlist_venue_id
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 201
                
            except Exception as e:
                conn.rollback()
                logger.error(f"Error creating wishlist venue: {e}")
                return jsonify({'message': 'Failed to create wishlist venue'}), 500
            finally:
                cursor.close()
                conn.close()
                
        except Exception as e:
            logger.error(f"Error in create_wishlist_venue_route: {e}")
            return jsonify({'message': 'An error occurred while creating wishlist venue'}), 500

    @app.route('/api/wishlist-packages/<int:wishlist_id>/venue', methods=['DELETE', 'OPTIONS'])
    @jwt_required()
    def remove_wishlist_package_venue_route(wishlist_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'DELETE,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # Update the wishlist_package to remove venue reference
            cursor.execute("""
                UPDATE wishlist_packages 
                SET venue_id = NULL, venue_status = NULL
                WHERE wishlist_id = %s
                RETURNING wishlist_id
            """, (wishlist_id,))
            
            result = cursor.fetchone()
            conn.commit()
            
            if result:
                response = jsonify({
                    'success': True,
                    'message': 'Venue reference removed successfully'
                })
                response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
                response.headers.add('Access-Control-Allow-Credentials', 'true')
                return response, 200
            else:
                return jsonify({'message': 'Wishlist package not found'}), 404
                
        except Exception as e:
            logger.error(f"Error removing venue reference: {e}")
            if conn:
                conn.rollback()
            return jsonify({'message': 'An error occurred while removing venue reference'}), 500
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @app.route('/api/wishlist-packages/<int:wishlist_id>', methods=['GET', 'OPTIONS'])
    @jwt_required()
    def get_wishlist_package_route(wishlist_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            # Get wishlist package details
            wishlist_data = get_wishlist_package(wishlist_id)
            
            if not wishlist_data:
                return jsonify({'message': 'Wishlist package not found'}), 404
            
            response = jsonify(wishlist_data)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        except Exception as e:
            logger.error(f"Error getting wishlist package: {e}")
            return jsonify({'message': 'An error occurred while getting wishlist package'}), 500

    @app.route('/api/wishlist-venues/<int:wishlist_id>', methods=['GET', 'OPTIONS'])
    @jwt_required(optional=True)  # Make JWT optional to handle OPTIONS requests
    def get_wishlist_venues_route(wishlist_id):
        if request.method == 'OPTIONS':
            response = jsonify({'message': 'OK'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
            response.headers.add('Access-Control-Allow-Methods', 'GET,OPTIONS')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200

        try:
            # Get wishlist venues
            venues = get_wishlist_venues(wishlist_id)
            
            response = jsonify(venues)
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 200
            
        except Exception as e:
            logger.error(f"Error getting wishlist venues: {e}")
            response = jsonify({'message': 'An error occurred while getting wishlist venues'})
            response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
            response.headers.add('Access-Control-Allow-Credentials', 'true')
            return response, 500

    return app
