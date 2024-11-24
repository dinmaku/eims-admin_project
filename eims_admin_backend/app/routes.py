#routes.py
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies
from .models import check_user,create_user, create_vendor, get_users_by_type, get_vendors_with_users
import logging
import jwt
from functools import wraps
import os

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






