from models import User
from flask import Flask, jsonify, request
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

# Home route
@app.route('/')
def home():
    return jsonify({"message": "User API is running 🚀"})

# GET users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()

    return jsonify(
        [user.to_dict() for user in users]
    )

# POST new user
@app.route('/users', methods=['POST'])
@app.route('/users', methods=['POST'])
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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)