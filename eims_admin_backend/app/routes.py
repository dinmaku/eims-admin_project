#routes.py
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from .models import check_user,create_user, create_supplier, get_users_by_type, get_suppliers_with_users, update_suppliers_and_user, delete_user, update_staff, get_packages, create_package, update_package, delete_package, get_all_booked_wishlist, update_event, get_packages_wedding, get_all_venues, get_package_services_with_suppliers, get_gown_packages,create_venue, update_venue, delete_venue, get_all_gown_packages, add_gown_package, get_all_outfits
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
            data = request.get_json(force=True, silent=True) or {}
            app.logger.info(f"Received data: {data}")

            required_fields = [
                'username', 'firstName', 'lastName', 'email', 'contactNumber', 
                'address', 'password', 'user_type'
            ]
            
            for field in required_fields:
                if field not in data or not data[field]:
                    app.logger.error(f"Missing field: {field}")
                    return jsonify({"message": f"Missing required field: {field}"}), 400

            if data['user_type'] == 'Suppliers':
                supplier_fields = ['service', 'price']
                for field in supplier_fields:
                    if field not in data or not data[field]:
                        app.logger.error(f"Missing supplier-specific field: {field}")
                        return jsonify({"message": f"Missing supplier-specific field: {field}"}), 400

            # Insert the user into the database
            user_created, user_id = create_user(
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
                app.logger.error("User creation failed due to duplicate email")
                return jsonify({"message": "Email already exists"}), 400

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

        required_fields = ['package_name', 'package_type', 'venue_id', 'capacity', 
                            'additional_capacity_charges', 'charge_unit', 'description', 'suppliers', 'gown_package_id']

        if not all(field in data for field in required_fields):
            return jsonify({"error": "All fields are required"}), 400

        try:
            data['capacity'] = int(data['capacity'])
            data['additional_capacity_charges'] = Decimal(str(data['additional_capacity_charges']))
            data['charge_unit'] = int(data['charge_unit'])
            data['gown_package_id'] = int(data['gown_package_id']) if data['gown_package_id'] else None

            if not isinstance(data['suppliers'], list) or len(data['suppliers']) == 0:
                return jsonify({"error": "At least one supplier is required"}), 400

            for supplier in data['suppliers']:
                if supplier['type'] == 'internal':
                    if not supplier['supplier_id']:
                        return jsonify({"error": "Invalid internal supplier data"}), 400
                elif supplier['type'] == 'external':
                    if not all(key in supplier for key in ['external_supplier_name', 'external_supplier_contact', 'external_supplier_price']):
                        return jsonify({"error": "Invalid external supplier data"}), 400
                    supplier['external_supplier_price'] = Decimal(str(supplier['external_supplier_price']))
                else:
                    return jsonify({"error": "Invalid supplier type"}), 400

            if create_package(data):
                return jsonify({"status": "success", "message": "Package created successfully"}), 201
            else:
                return jsonify({"status": "error", "message": "Failed to create package"}), 500
        except ValueError:
            return jsonify({"error": "Invalid numeric value provided"}), 400
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500

        

    @app.route('/created-package/<int:package_id>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def edit_package(package_id):
        try:
            if not package_id:
                return jsonify({"message": "Invalid package ID"}), 400

            data = request.get_json(force=True, silent=True) or {}
            required_fields = ["package_name", "package_type", "venue", "price", "capacity", "description"]

            # Ensure all required fields are present
            if not all(field in data and data[field] for field in required_fields):
                return jsonify({"message": "All fields are required"}), 400

            # Extract data
            package_name = data["package_name"]
            package_type = data["package_type"]
            venue = data["venue"]
            price = data["price"]
            capacity = data["capacity"]
            description = data["description"]

            # Update the package data
            if update_package(package_id, package_name, package_type, venue, price, capacity, description):
                return jsonify({"message": "Package updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update package. Package not found or database error occurred."}), 404
        except Exception as e:
            app.logger.error(f"Error in edit_package route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500
    


#manage events routes
    @app.route('/booked-wishlist', methods=['GET'])
    def get_all_booked_wishlist_for_admin():
        try:
            # Fetch all events with status 'Wishlist'
            all_wishlist_events = get_all_booked_wishlist()
            return jsonify(all_wishlist_events), 200
        except Exception as e:
            logging.error(f"Error fetching all 'Wishlist' events for admin: {e}")
            return jsonify({'message': f'Error fetching wishlist events: {str(e)}'}), 500


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

    @app.route('/created-venues', methods=['GET'])
    @jwt_required()
    def get_venues_route():
        try:
            # Fetch all event packages
            packages = get_all_venues()
            return jsonify(packages), 200
        except Exception as e:
            app.logger.error(f"Error fetching packages: {e}")
            return jsonify({'message': 'An error occurred while fetching packages'}), 500


    @app.route('/create-venue', methods=['POST'])
    def create_venue_route():
        try:
            # Extract data from the incoming request
            data = request.get_json(force=True, silent=True) or {}
            venue_name = data.get('venue_name')
            location = data.get('location')
            venue_price = data.get('venue_price')

            # Validate input data
            if not all([venue_name, location, venue_price]):
                return jsonify({"error": "All fields are required: venue_name, location, venue_price"}), 400

            if not isinstance(venue_price, (int, float)) or venue_price <= 0:
                return jsonify({"error": "Venue price must be a positive number"}), 400

            # Call the function to create the venue
            success = create_venue(venue_name, location, venue_price)

            if success:
                return jsonify({"message": "Venue created successfully"}), 201
            else:
                return jsonify({"error": "Failed to create venue"}), 500

        except Exception as e:
            print(f"Error in /create-venue route: {e}")
            return jsonify({"error": "An internal server error occurred"}), 500



    @app.route('/update-venue/<int:venue_id>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def update_venue_details(venue_id):
        """
        Updates the details of a specific venue.

        Args:
            venue_id (int): The ID of the venue to update.

        Returns:
            JSON response with success or error message.
        """
        try:
            if not venue_id:
                return jsonify({"message": "Invalid venue ID"}), 400

            data = request.json
            required_fields = ["venue_name", "location", "venue_price"]

            # Ensure all required fields are present
            if data is None or not all(field in data and data.get(field) for field in required_fields):
                return jsonify({"message": "All fields are required"}), 400

            # Extract data
            venue_name = data["venue_name"]
            location = data["location"]
            venue_price = data["venue_price"]

            # Update the venue data
            if update_venue(venue_id, venue_name, location, venue_price):
                return jsonify({"message": "Venue updated successfully"}), 200
            else:
                return jsonify({"message": "Failed to update venue. Venue not found or database error occurred."}), 404
        except Exception as e:
            app.logger.error(f"Error in update_venue_details route: {e}")
            return jsonify({"message": f"Error: {str(e)}"}), 500
        


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


