from flask import Flask, jsonify, request
import data

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return jsonify({"message": "User API is running 🚀"})

# GET users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data.users)

# POST new user
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    new_user["id"] = len(data.users) + 1
    data.users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)