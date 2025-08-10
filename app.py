from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['GET'])
def get_user():
    return jsonify(users), 200

@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = str(len(users + 1))
    users[user_id] = {
        "name": data.get("name"),
        "email": data.get("email"),
    }
    return jsonify({"message": "User added", "user": users[user_id]}), 201

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])
    return jsonify({"messsage": "User update", "user": users[user_id]}), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user":deleted_user}), 200

if __name__ == '__main__':
    app.run(debug=True)