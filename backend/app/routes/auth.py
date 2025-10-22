from flask import Blueprint, request, jsonify

from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token

from app.models import User

from app.extensions import db

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    Register a new user
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - username
            - password
          properties:
            username:
              type: string
              example: testuser
            password:
              type: string
              example: "1234"
    responses:
      201:
        description: User registered successfully
      400:
        description: Missing or invalid data
    """
    data = request.get_json()
    
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400
    
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists."}), 409
    
    hashed_password = generate_password_hash(password)

    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": f"User {username} registered successfully."}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
  """
  User login
  ---
  tags:
    - Authentication
  parameters:
    - in: body
      name: body
      schema:
        type: object
        required:
          - username
          - password
        properties:
          username:
            type: string  
            example: testuser
          password:
            type: string
            example: "1234"
  responses:
    200:
      description: Login successful
      schema:
        type: object
        properties:
          access_token:
            type: string
    401:
      description: Invalid credentials
  """
  data = request.get_json()
  
  username = data.get("username")
  password = data.get("password")

  user = User.query.filter_by(username=username).first()
  
  if not user or not check_password_hash(user.password, password):
    return jsonify({"error": "Invalid credentials"}), 401

  access_token = create_access_token(identity=user.id)
  
  return jsonify({"access_token": access_token}), 200


