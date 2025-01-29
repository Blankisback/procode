from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')  # Example of how to get a token

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        # You can add additional logic here to validate the token (e.g., JWT)

        return f(*args, **kwargs)  # If the token is valid, call the route function

    return decorated_function
