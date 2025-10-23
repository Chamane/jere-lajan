from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.models import Expense, db

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/add", methods=["POST"])
def create_expense():
    """
    Create a new expense
    ---
    security:
        - Bearer: []
    tags:
      - Expenses
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - title
            - amount
            - description
            - user_id
          properties:
            title:
              type: string
              example: "Groceries"
            amount:
              type: number
              format: float
              example: 150.75
            description:
              type: string
              example: "Weekly grocery shopping"
            user_id:
              type: integer
              example: 1
    responses:
      201:
        description: Expense created successfully
      400:
        description: Missing or invalid data
    """
    data = request.get_json()

    title = data.get("title")
    amount = data.get("amount")
    description = data.get("description")
    user_id = data.get("user_id")

    if not title or not amount or not description or not user_id:
        return jsonify({"error": "Title, amount, description, and user_id are required."}), 400

    new_expense = Expense(
        title=title,
        amount=amount,
        description=description,
        user_id=user_id
    )

    db.session.add(new_expense)
    db.session.commit()

    return jsonify({"message": "Expense created successfully."}), 201
