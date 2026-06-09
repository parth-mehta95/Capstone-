from flask import Blueprint, jsonify, request

from models import ApiResponse, Order, Product, User
from services import OrderService, ProductService, UserService

api = Blueprint("api", __name__)

user_service = UserService([
    User(1, "Parth Mehta", "parth@example.com", True),
    User(2, "John Doe", "john@example.com", False),
    User(3, "Jane Smith", "jane@example.com", True),
])

product_service = ProductService([
    Product(1, "React Native Course", "education", 49.99, True),
    Product(2, "Mobile UI Kit", "design", 29.99, True),
    Product(3, "Backend Template", "development", 59.99, False),
])

order_service = OrderService([
    Order(1, 1, [1, 3], "processing"),
    Order(2, 3, [2], "completed"),
])


@api.route("/health", methods=["GET"])
def health_check():
    response = ApiResponse(
        True,
        "Backend service is running",
        {"status": "ok"}
    )
    return jsonify(response.to_dict()), 200


@api.route("/users", methods=["GET"])
def get_users():
    response = ApiResponse(
        True,
        "Users fetched successfully",
        user_service.get_all()
    )
    return jsonify(response.to_dict()), 200


@api.route("/users/active", methods=["GET"])
def get_active_users():
    response = ApiResponse(
        True,
        "Active users fetched successfully",
        user_service.get_active_users()
    )
    return jsonify(response.to_dict()), 200


@api.route("/users/emails", methods=["GET"])
def get_user_emails():
    response = ApiResponse(
        True,
        "Active user emails fetched successfully",
        user_service.get_user_emails()
    )
    return jsonify(response.to_dict()), 200


@api.route("/products", methods=["GET"])
def get_products():
    response = ApiResponse(
        True,
        "Products fetched successfully",
        product_service.get_all()
    )
    return jsonify(response.to_dict()), 200


@api.route("/products/summary", methods=["GET"])
def get_product_summary():
    response = ApiResponse(
        True,
        "Product summary fetched successfully",
        product_service.get_product_summary()
    )
    return jsonify(response.to_dict()), 200


@api.route("/products/filter", methods=["GET"])
def filter_products():
    category = request.args.get("category")
    max_price = request.args.get("max_price", type=float)

    if category:
        data = product_service.filter_by_category(category)
        message = "Products filtered by category"
    elif max_price is not None:
        data = product_service.filter_by_price(max_price)
        message = "Products filtered by price"
    else:
        data = product_service.get_all()
        message = "All products returned"

    response = ApiResponse(True, message, data)
    return jsonify(response.to_dict()), 200


@api.route("/orders", methods=["GET"])
def get_orders():
    response = ApiResponse(
        True,
        "Orders fetched successfully",
        order_service.get_all()
    )
    return jsonify(response.to_dict()), 200


@api.route("/orders/user/<int:user_id>", methods=["GET"])
def get_orders_by_user(user_id):
    response = ApiResponse(
        True,
        "User orders fetched successfully",
        order_service.get_orders_by_user(user_id)
    )
    return jsonify(response.to_dict()), 200