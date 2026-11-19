from flask import Flask, request, jsonify

app = Flask(__name__)

habits = []
next_id = 1

@app.route("/habits", methods=["POST"])
def create_habit():
    data = request.get_json()

    # basic validation: required fields
    required_fields = ["name", "date", "completed"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    global next_id

    new_habit = {
        "id": next_id,
        "name": data["name"],
        "date": data["date"],
        "completed": data["completed"],
        "notes": data.get("notes", "")
    }

    habits.append(new_habit)
    next_id += 1

    return jsonify(new_habit), 201

@app.route("/habits/<int:habit_id>", methods=["GET"])
def get_habit(habit_id):
    for habit in habits:
        if habit["id"] == habit_id:
            return jsonify(habit), 200

    # not found
    return jsonify({"error": "Habit not found"}), 404

@app.route("/habits", methods=["GET"])
def list_habits():
    return jsonify(habits), 200

@app.route("/habits/<int:habit_id>", methods=["PUT"])
def update_habit(habit_id):
    data = request.get_json()

    # validate required fields
    required_fields = ["name", "date", "completed"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # find exisitng habit
    for habit in habits:
        if habit["id"] == habit_id:
            habit["name"] = data["name"]
            habit["date"] = data["date"]
            habit["completed"] = data["completed"]
            habit["notes"] = data.get("notes", habit.get("notes", ""))
            return jsonify(habit), 200

    # not found
    return jsonify({"error": "Habit not found"}), 404

@app.route("/habits/<int:habit_id>", methods=["DELETE"])
def delete_habit(habit_id):
    for index, habit in enumerate(habits):
        if habit["id"] == habit_id:
            del habits[index]
            return "", 204

    return jsonify({"error": "Habit not found"}), 404