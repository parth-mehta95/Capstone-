from flask import Blueprint, jsonify, request

from models import ApiResponse, Order, Product, User
from services import OrderService, ProductService, UserService
from validators import DataValidator, OrderValidator, ProductValidator, UserValidator

api = Blueprint("api", __name__)

user_validator = UserValidator()
product_validator = ProductValidator()
order_validator = OrderValidator()
data_validator = DataValidator()

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


def validation_error_response(result):
    response = ApiResponse(
        False,
        "Validation failed",
        result.to_dict(),
    )
    return jsonify(response.to_dict()), 400


@api.route("/health", methods=["GET"])
def health_check():
    response = ApiResponse(
        True,
        "Backend service is running",
        {"status": "ok"},
    )
    return jsonify(response.to_dict()), 200


@api.route("/users", methods=["GET"])
def get_users():
    response = ApiResponse(
        True,
        "Users fetched successfully",
        user_service.get_all(),
    )
    return jsonify(response.to_dict()), 200


@api.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json() or {}

    result = user_validator.validate(payload)
    if not result.is_valid:
        return validation_error_response(result)

    new_user = User(
        len(user_service.get_all()) + 1,
        payload["name"],
        payload["email"],
        payload.get("active", True),
    )

    response = ApiResponse(
        True,
        "User created successfully",
        user_service.add_item(new_user),
    )
    return jsonify(response.to_dict()), 201


@api.route("/users/active", methods=["GET"])
def get_active_users():
    response = ApiResponse(
        True,
        "Active users fetched successfully",
        user_service.get_active_users(),
    )
    return jsonify(response.to_dict()), 200


@api.route("/products", methods=["GET"])
def get_products():
    response = ApiResponse(
        True,
        "Products fetched successfully",
        product_service.get_all(),
    )
    return jsonify(response.to_dict()), 200


@api.route("/products", methods=["POST"])
def create_product():
    payload = request.get_json() or {}

    result = product_validator.validate(payload)
    if not result.is_valid:
        return validation_error_response(result)

    new_product = Product(
        len(product_service.get_all()) + 1,
        payload["name"],
        payload["category"],
        payload["price"],
        payload.get("in_stock", True),
    )

    response = ApiResponse(
        True,
        "Product created successfully",
        product_service.add_item(new_product),
    )
    return jsonify(response.to_dict()), 201


@api.route("/products/filter", methods=["GET"])
def filter_products():
    result = data_validator.validate(request.args)
    if not result.is_valid:
        return validation_error_response(result)

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
        order_service.get_all(),
    )
    return jsonify(response.to_dict()), 200


@api.route("/orders", methods=["POST"])
def create_order():
    payload = request.get_json() or {}

    result = order_validator.validate(payload)
    if not result.is_valid:
        return validation_error_response(result)

    new_order = Order(
        len(order_service.get_all()) + 1,
        payload["user_id"],
        payload["product_ids"],
        payload["status"],
    )

    response = ApiResponse(
        True,
        "Order created successfully",
        order_service.add_item(new_order),
    )
    return jsonify(response.to_dict()), 201