from flask import Blueprint, request, jsonify
from models import tasks, create_task

task_routes = Blueprint('tasks', __name__)

@task_routes.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@task_routes.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = create_task(data["title"])
    return jsonify(task), 201

@task_routes.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"})

@task_routes.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.json
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["done"] = data.get("done", task["done"])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404