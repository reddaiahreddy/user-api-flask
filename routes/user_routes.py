from flask import Blueprint, jsonify, request

from models import User
from database import db


user_bp = Blueprint(
    "users",
    __name__
)

# GET users
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify(
        [user.to_dict() for user in users]
    )

# POST new user
@user_bp.route('/users', methods=['POST'])
def add_user():
    request_data = request.json

    if not request_data:
        return jsonify({
            "error": "JSON body is required"
        }), 400

    if "name" not in request_data:
        return jsonify({
            "error": "name is required"
        }), 400

    if not request_data["name"].strip():
        return jsonify({
            "error": "name cannot be empty"
        }), 400

    user = User(
        name=request_data["name"]
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(
        user.to_dict()
    ), 201

# UPDATE existing user
@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "error": "user not found"
        }), 404

    request_data = request.json

    if not request_data:
        return jsonify({
            "error": "JSON body is required"
        }), 400

    if "name" not in request_data:
        return jsonify({
            "error": "name is required"
        }), 400

    if not request_data["name"].strip():
        return jsonify({
            "error": "name cannot be empty"
        }), 400

    user.name = request_data["name"]

    db.session.commit()

    return jsonify(
        user.to_dict()
    )

# DELETE existing user
@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "error": "user not found"
        }), 404

    db.session.delete(user)

    db.session.commit()

    return jsonify({
        "message": "user deleted successfully"
    })