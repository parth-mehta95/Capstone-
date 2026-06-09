from flask import Blueprint, jsonify, request

try:
    from .models import ApiResponse, TaskItem, UserProfile
except ImportError:
    from models import ApiResponse, TaskItem, UserProfile


api = Blueprint("api", __name__)

users = [
    UserProfile(1, "John Doe", "john@example.com"),
    UserProfile(2, "Jane Smith", "jane@example.com"),
]

tasks = [
    TaskItem(1, "Complete React Native setup", True),
    TaskItem(2, "Connect backend service", False),
]


@api.route("/health", methods=["GET"])
def health_check():
    response = ApiResponse(
        success=True,
        message="Backend service is running",
        data={"status": "ok"},
    )
    return jsonify(response.to_dict()), 200


@api.route("/users", methods=["GET"])
def get_users():
    data = [user.to_dict() for user in users]

    response = ApiResponse(
        success=True,
        message="Users fetched successfully",
        data=data,
    )
    return jsonify(response.to_dict()), 200


@api.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json()

    if not payload or "name" not in payload or "email" not in payload:
        response = ApiResponse(
            success=False,
            message="Name and email are required",
        )
        return jsonify(response.to_dict()), 400

    new_user = UserProfile(
        id=len(users) + 1,
        name=payload["name"],
        email=payload["email"],
    )

    users.append(new_user)

    response = ApiResponse(
        success=True,
        message="User created successfully",
        data=new_user.to_dict(),
    )
    return jsonify(response.to_dict()), 201


@api.route("/tasks", methods=["GET"])
def get_tasks():
    data = [task.to_dict() for task in tasks]

    response = ApiResponse(
        success=True,
        message="Tasks fetched successfully",
        data=data,
    )
    return jsonify(response.to_dict()), 200


@api.route("/tasks", methods=["POST"])
def create_task():
    payload = request.get_json()

    if not payload or "title" not in payload:
        response = ApiResponse(
            success=False,
            message="Task title is required",
        )
        return jsonify(response.to_dict()), 400

    new_task = TaskItem(
        id=len(tasks) + 1,
        title=payload["title"],
        completed=payload.get("completed", False),
    )

    tasks.append(new_task)

    response = ApiResponse(
        success=True,
        message="Task created successfully",
        data=new_task.to_dict(),
    )
    return jsonify(response.to_dict()), 201