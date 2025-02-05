from flask import Flask, request, jsonify
app = Flask(__name__)
FILE_NAME = "students.json"

# Функції роботи з файлом
def load_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)

@app.route("/students", methods=["GET", "POST"])
def students():
    students = load_students()
    if request.method == "POST":
        students.append(request.json)
        save_students(students)
        return jsonify({"message": "✅ Студента додано!"}), 201
    return jsonify(students)

@app.route("/students/<int:index>", methods=["DELETE"])
def delete_student(index):
    students = load_students()
    if 0 <= index < len(students):
        removed = students.pop(index)
        save_students(students)
    return jsonify({"message": f"✅ Студента {removed.get("Імя", "Невідомо")} {removed.get("Прізвище", "Невідомо")} видалено!"})


if name == "__main__":
    app.run(debug=True)