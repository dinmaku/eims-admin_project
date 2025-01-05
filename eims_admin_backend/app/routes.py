#routes.py
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from .models import check_user, create_user, create_supplier, get_users_by_type, get_suppliers_with_users, update_suppliers_and_user, delete_user, update_staff, get_packages, create_package, update_package, delete_package, get_all_booked_wishlist, update_event, get_packages_wedding, get_all_venues, get_package_services_with_suppliers, get_gown_packages,create_venue, update_venue, delete_venue, get_all_gown_packages, add_gown_package, get_all_outfits, get_all_additional_services, create_additional_service, update_additional_service, get_event_types, initialize_event_types, create_event_type, get_admin_users, create_outfit, add_event_item, get_available_suppliers, get_available_venues, get_available_gown_packages, get_all_additional_services, get_event_types, get_package_details_by_id, get_user_id_by_email
import logging
import jwt
from functools import wraps
import os
from decimal import Decimal

logging.basicConfig(level=logging.DEBUG)
SECRET_KEY = os.getenv('eims', 'fallback_jwt_secret')

def init_routes(app):
    
    @app.route('/login', methods=['POST'])
    def login():
        try:
            # Get the login data
            data = request.get_json(force=True, silent=True) or {}
            email = data.get('email')
            password = data.get('password')

            # Check if email and password are provided
            if not email or not password:
                print("Missing email or password")
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
                print("Invalid credentials or unauthorized user type")
                return jsonify({'message': '* Invalid email, password, or unauthorized access.'}), 401

        except Exception as e:
            print(f"Error during login: {e}")
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
                        app.logger.info("Supplier data inserted successfully")
                    else:
                        app.logger.error("Failed to create supplier")
                        return jsonify({"message": "Failed to create supplier"}), 500
                app.logger.info("User data validated and inserted into the database successfully")
                return jsonify({"message": "User registered successfully"}), 201
            else:
                app.logger.error(f"User creation failed: {error_message}")
                return jsonify({"message": error_message}), 400

        except Exception as e:
            app.logger.error(f"Error processing request: {str(e)}")
            return jsonify({"message": "Internal server error"}), 500



        

    @app.route('/created-users', methods=['GET'])
    @jwt_required()
    def get_users_by_type_route():
        try:
            # Fetch users with user_type 'assistant' or 'staff'
            users = get_users_by_type()
            return jsonify(users), 200
        except Exception as e:
            app.logger.error(f"Error fetching users: {e}")
            return jsonify({'message': 'An error occurred while fetching users'}), 500


    @app.route('/get_admin', methods=['GET'])
    @jwt_required()
    def get_admin_list():
        try:
            # Fetch users with user_type 'Admin'
            users = get_admin_users()
            return jsonify(users), 200
        except Exception as e:
            app.logger.error(f"Error fetching admin users: {e}")
            return jsonify({'message': 'An error occurred while fetching admin users'}), 500



    @app.route('/suppliers', methods=['GET'])
    @jwt_required()
    def get_suppliers_route():
        try:
            # Fetch suppliers with their associated user details
            suppliers = get_suppliers_with_users()
            return jsonify(suppliers), 200
        except Exception as e:
            app.logger.error(f"Error fetching suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching suppliers'}), 500

    @app.route('/package-service-suppliers', methods=['GET'])
    @jwt_required()
    def get_event_service_suppliers_route():
        try:
            # Fetch suppliers with their associated user details
            suppliers = get_package_services_with_suppliers()
            return jsonify(suppliers), 200
        except Exception as e:
            app.logger.error(f"Error fetching suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching suppliers'}), 500
        

    @app.route('/gown-packages', methods=['GET'])
    @jwt_required()
    def get_gown_packages_route():
        try:
            gown_packages = get_gown_packages()
            return jsonify(gown_packages), 200
        except Exception as e:
            app.logger.error(f"Error fetching gown packages: {e}")
            return jsonify({'message': 'An error occurred while fetching gown packages'}), 500
        

    @app.route('/edit-supplier/<int:supplier_id>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def edit_supplier(supplier_id):
        try:
            data = request.get_json(force=True, silent=True) or {}
            app.logger.info(f"Received data: {data}")  # Log incoming data
            print(data)

            # Extract and validate supplier-specific fields
            service = data.get('service')
            price = data.get('price')
            if not all([service, price]):
                return jsonify({"message": "Supplier-specific fields 'service' and 'price' are required"}), 400

            # Extract and validate user-specific fields
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            email = data.get('email')
            username = data.get('username')
            contactnumber = data.get('contactnumber')
            password = data.get('password')
            userid = data.get('userid')  # Make sure you extract userid from the request

            if not all([firstname, lastname, username, email, contactnumber, password, userid]):
                return jsonify({"message": "All user fields are required"}), 400

            # Log the fields to check if they match expectations
            app.logger.info(f"Fields: firstname={firstname}, lastname={lastname}, username={username}, email={email}, contactnumber={contactnumber}, password={password}, userid={userid}")

            # Assuming `update_suppliers_and_user` is a valid function
            if update_suppliers_and_user(
                supplier_id=supplier_id, service=service, price=price,
                firstname=firstname, lastname=lastname, email=email,
                contactnumber=contactnumber, username=username, password=password, userid=userid
            ):
                return jsonify({"message": "Supplier and user details updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update supplier or user. Record not found or database error occurred."}), 404

        except Exception as e:
            app.logger.error(f"Error in edit_supplier route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500








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
            app.logger.error(f"Error in edit_staff route: {e}")
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
            app.logger.error(f"Error in delete_users route: {e}")
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
            app.logger.error(f"Error fetching packages: {e}")
            return jsonify({'message': 'An error occurred while fetching packages'}), 500

    @app.route('/create-package', methods=['POST'])
    @jwt_required()
    def create_package_route():
        data = request.get_json()
        print("Received data:", data)

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
            app.logger.error(f"Error in create_package_route: {e}")
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
            app.logger.error(f"Error in edit_package route: {e}")
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
            app.logger.error(f"Error deleting package: {e}")
            return jsonify({"message": "An error occurred while deleting the package"}), 500

            
    


#manage events routes
    @app.route('/booked-wishlist', methods=['GET'])
    @jwt_required()
    def get_booked_wishlist_route():
        try:
            # Fetch booked wishlist with additional services
            wishlist_with_services = get_all_booked_wishlist()
            return jsonify(wishlist_with_services), 200
        except Exception as e:
            app.logger.error(f"Error fetching booked wishlist with services: {e}")
            return jsonify({'message': 'An error occurred while fetching booked wishlist'}), 500


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
            app.logger.error(f"Error in update_booked_wishlist route: {e}")
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
            app.logger.error(f"Error fetching packages: {e}")
            return jsonify({'message': 'An error occurred while fetching packages'}), 500




#venues routes

    @app.route('/venues', methods=['POST'])
    @jwt_required()
    def add_venue():
        data = request.get_json()
        venue_name = data.get('venue_name')
        location = data.get('location')
        venue_price = data.get('venue_price')
        venue_capacity = data.get('venue_capacity')
        description = data.get('description')

        if not all([venue_name, location, venue_price, venue_capacity]):
            return jsonify({'message': 'Missing required fields'}), 400

        try:
            create_venue(venue_name, location, venue_price, venue_capacity, description)
            return jsonify({'message': 'Venue added successfully'}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500

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
            app.logger.error(f"Error fetching packages: {e}")
            return jsonify({'message': 'An error occurred while fetching packages'}), 500


#routes for outfit packages

    @app.route('/gown-packages', methods=['GET'])
    @jwt_required()
    def get_all_gown_packages_route():
        try:
            # Fetch all gown packages
            packages = get_all_gown_packages()
            return jsonify(packages), 200
        except Exception as e:
            app.logger.error(f"Error fetching gown packages: {e}")
            return jsonify({'message': 'An error occurred while fetching gown packages'}), 500
        
        
    @app.route('/outfits', methods=['GET'])
    @jwt_required()
    def get_outfits_route():
        try:
            # Fetch all outfits
            outfits = get_all_outfits()
            return jsonify(outfits), 200
        except Exception as e:
            app.logger.error(f"Error fetching outfits: {e}")
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
            logging.error(f"Error in create_new_outfit: {str(e)}")
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
            app.logger.error(f"Error adding gown package: {e}")
            return jsonify({'message': 'An error occurred while adding the gown package'}), 500


#additional services routes

    @app.route('/additional-services', methods=['GET'])
    @jwt_required()
    def get_additional_services_route():
        try:
            services = get_all_additional_services()
            return jsonify(services), 200
        except Exception as e:
            app.logger.error(f"Error fetching additional services: {str(e)}")
            return jsonify({'message': 'An error occurred while fetching additional services'}), 500

    @app.route('/created-services', methods=['GET'])
    @jwt_required()
    def get_services_route():
        try:
            services = get_all_additional_services()
            return jsonify(services), 200
        except Exception as e:
            app.logger.error(f"Error fetching services: {e}")
            return jsonify({'message': 'An error occurred while fetching services'}), 500

    @app.route('/create-service', methods=['POST'])
    @jwt_required()
    def create_service_route():
        try:
            data = request.get_json(force=True, silent=True) or {}
            add_service_name = data.get('add_service_name')
            add_service_description = data.get('add_service_description')
            add_service_price = data.get('add_service_price')

            if not all([add_service_name, add_service_description, add_service_price]):
                return jsonify({"error": "All fields are required: add_service_name, add_service_description, add_service_price"}), 400

            if not isinstance(add_service_price, (int, float)) or add_service_price <= 0:
                return jsonify({"error": "Service price must be a positive number"}), 400

            success = create_additional_service(add_service_name, add_service_description, add_service_price)

            if success:
                return jsonify({"message": "Service created successfully"}), 201
            else:
                return jsonify({"error": "Failed to create service"}), 500
        except Exception as e:
            app.logger.error(f"Error in /create-service route: {e}")
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
            app.logger.error(f"Error in update_service_details route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500

    @app.route('/event-types', methods=['GET'])
    def get_event_types_route():
        try:
            event_types = get_event_types()
            return jsonify(event_types), 200
        except Exception as e:
            app.logger.error(f"Error fetching event types: {e}")
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




    @app.route('/wishlist', methods=['POST'])
    @jwt_required()
    def add_wishlist():
        email = get_jwt_identity()
        userid = get_user_id_by_email(email)

        if userid is None:
            return jsonify({'message': 'Failed to retrieve user ID'}), 400

        data = request.json

        # Validate required fields
        required_fields = [
            'event_name', 'event_type', 'event_theme', 'event_color', 
            'package_id', 'suppliers', 'venues',
            'onsite_firstname', 'onsite_lastname', 'onsite_contact', 'onsite_address'
        ]
        if not all(field in data for field in required_fields):
            return jsonify({'message': 'Missing required fields'}), 400

        try:
            events_id = add_event_item(
                userid=userid,
                event_name=data['event_name'],
                event_type=data['event_type'],
                event_theme=data['event_theme'],
                event_color=data['event_color'],
                package_id=data['package_id'],
                suppliers=data['suppliers'],
                venues=data['venues'],
                schedule=data.get('schedule'),
                start_time=data.get('start_time'),
                end_time=data.get('end_time'),
                status=data.get('status', 'Wishlist'),
                onsite_firstname=data['onsite_firstname'],
                onsite_lastname=data['onsite_lastname'],
                onsite_contact=data['onsite_contact'],
                onsite_address=data['onsite_address']
            )

            return jsonify({
                'message': 'Event added successfully', 
                'events_id': events_id
            }), 201

        except Exception as e:
            app.logger.error(f"Error adding wishlist: {str(e)}")
            return jsonify({
                'message': f'Failed to add event: {str(e)}'
            }), 500

    @app.route('/available-suppliers', methods=['GET'])
    @jwt_required()
    def get_available_suppliers_route():
        try:
            suppliers = get_available_suppliers()
            return jsonify(suppliers), 200
        except Exception as e:
            app.logger.error(f"Error fetching available suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching available suppliers'}), 500

    @app.route('/available-venues', methods=['GET'])
    @jwt_required()
    def get_available_venues_route():
        try:
            venues = get_available_venues()
            return jsonify(venues), 200
        except Exception as e:
            app.logger.error(f"Error fetching available venues: {e}")
            return jsonify({'message': 'An error occurred while fetching available venues'}), 500

    @app.route('/available-gown-packages', methods=['GET'])
    @jwt_required()
    def get_available_gown_packages_route():
        try:
            gown_packages = get_available_gown_packages()
            return jsonify(gown_packages), 200
        except Exception as e:
            app.logger.error(f"Error fetching available gown packages: {e}")
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
            app.logger.error(f"Error fetching package details: {e}")
            return jsonify({'message': 'An error occurred while fetching package details'}), 500


    @app.route('/created-venues', methods=['GET'])
    @jwt_required()
    def get_created_venues():
        try:
            venues = get_all_venues()
            return jsonify(venues), 200
        except Exception as e:
            app.logger.error(f"Error fetching venues: {e}")
            return jsonify({'message': 'An error occurred while fetching venues'}), 500

    @app.route('/created-suppliers', methods=['GET'])
    @jwt_required()
    def get_created_suppliers():
        try:
            suppliers = get_suppliers_with_users()
            return jsonify(suppliers), 200
        except Exception as e:
            app.logger.error(f"Error fetching suppliers: {e}")
            return jsonify({'message': 'An error occurred while fetching suppliers'}), 500

    @app.route('/created-gown-packages', methods=['GET'])
    @jwt_required()
    def get_created_gown_packages():
        try:
            packages = get_all_gown_packages()
            return jsonify(packages), 200
        except Exception as e:
            app.logger.error(f"Error fetching gown packages: {e}")
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
            app.logger.error(f"Error fetching booked wishlist: {str(e)}")
            return jsonify({'message': f'Error fetching wishlist: {str(e)}'}), 500
