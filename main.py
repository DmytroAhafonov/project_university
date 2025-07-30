from flask import Flask, request, jsonify
import asyncio
from database import init_db
from models import User, UserCreate
from pydantic import ValidationError

app = Flask(__name__)

# Создаём собственный event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(init_db())

@app.route("/users", methods=["GET"])
def get_users():
    users = loop.run_until_complete(User.find_all().to_list())
    return jsonify([
        {**user.model_dump(), "id": str(user.id)} for user in users
    ])

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    try:
        user_data = UserCreate(**data)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400

    user = User(**user_data.model_dump())
    loop.run_until_complete(user.insert())
    response = user.model_dump()
    response["id"] = str(user.id)
    return jsonify(response), 201


# DELETE /users/<id>
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = loop.run_until_complete(User.get(user_id))
    if not user:
        return jsonify({"error": "User not found"}), 404
    loop.run_until_complete(user.delete())
    return jsonify({"message": "User deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
