#routes.py
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from .models import check_user,create_user, create_vendor, get_users_by_type, get_vendors_with_users, delete_user, update_staff, get_packages, create_package, update_package, delete_package, get_all_booked_wishlist, update_event, get_packages_wedding
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
            data = request.json
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
            data = request.json
            app.logger.info(f"Received data: {data}")

            required_fields = [
                'firstName', 'lastName', 'email', 'contactNumber', 
                'country', 'city', 'street', 'password', 'user_type'
            ]
            
            for field in required_fields:
                if field not in data or not data[field]:
                    app.logger.error(f"Missing field: {field}")
                    return jsonify({"message": f"Missing required field: {field}"}), 400

            if data['user_type'] == 'vendor':
                vendor_fields = ['service', 'minPrice', 'maxPrice']
                for field in vendor_fields:
                    if field not in data or not data[field]:
                        app.logger.error(f"Missing vendor-specific field: {field}")
                        return jsonify({"message": f"Missing vendor-specific field: {field}"}), 400

            # Insert the user into the database
            user_created, user_id = create_user(
                first_name=data['firstName'],
                last_name=data['lastName'],
                email=data['email'],
                contact_number=data['contactNumber'],
                password=data['password'],
                user_type=data['user_type'],
                country=data['country'],
                city=data['city'],
                street=data['street']
            )

            if user_created:
                if data['user_type'] == 'vendor':
                    # Insert the vendor entry after the user is created
                    vendor_created = create_vendor(
                        userid=user_id,
                        service=data['service'],
                        min_price=data['minPrice'],
                        max_price=data['maxPrice']
                    )
                    if vendor_created:
                        app.logger.info("Vendor data inserted successfully")
                    else:
                        app.logger.error("Failed to create vendor")
                        return jsonify({"message": "Failed to create vendor"}), 500
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



    @app.route('/vendors', methods=['GET'])
    @jwt_required()
    def get_vendors_route():
        try:
            # Fetch vendors with their associated user details
            vendors = get_vendors_with_users()
            return jsonify(vendors), 200
        except Exception as e:
            app.logger.error(f"Error fetching vendors: {e}")
            return jsonify({'message': 'An error occurred while fetching vendors'}), 500



    @app.route('/created-users/<int:userid>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def edit_staff(userid):
        try:
            if not userid:
                return jsonify({"message": "Invalid user ID"}), 400

            data = request.json
            firstname = data.get('firstname')
            lastname = data.get('lastname')
            email = data.get('email')
            contact = data.get('contactnumber')  # Changed from 'contactnumber' to 'contact'
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

        # Extract fields from the incoming data
        package_name = data.get('package_name')
        package_type = data.get('package_type')
        venue = data.get('venue')
        price = data.get('price')
        capacity = data.get('capacity')
        description = data.get('description')

        # Check if all required fields are provided
        if not all([package_name, package_type, venue, price, capacity, description]):
            return jsonify({"error": "All fields are required"}), 400

        try:
            # Convert price and capacity to correct types
            price = Decimal(price)  # Convert price to Decimal for precise handling
            capacity = int(capacity)  # Convert capacity to integer
        except ValueError:
            return jsonify({"error": "Price must be a decimal and capacity must be an integer"}), 400

        try:
            # Call the function to create the package in the database
            if create_package(package_name, package_type, venue, price, capacity, description):
                return jsonify({"status": "success", "message": "Package created successfully"}), 201
            else:
                return jsonify({"status": "error", "message": "Failed to create package"}), 500
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
        

    @app.route('/created-package/<int:package_id>', methods=['PUT'])
    @jwt_required()  # Authentication required
    def edit_package(package_id):
        try:
            if not package_id:
                return jsonify({"message": "Invalid package ID"}), 400

            data = request.json
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
        



    @app.route('/created-package/<int:package_id>', methods=['DELETE'])
    @jwt_required()
    def delete_package_route(package_id):
        """
        Deletes a package based on the package ID.
        """
        try:
            result = delete_package(package_id)
            if result:
                return jsonify({"message": "Package deleted successfully"}), 200
            else:
                return jsonify({"message": "Failed to delete package. Package not found."}), 404
        except Exception as e:
            app.logger.error(f"Error in delete_package_route: {e}")
            return jsonify({"message": "An error occurred while deleting the package"}), 500

        

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

            data = request.json
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
