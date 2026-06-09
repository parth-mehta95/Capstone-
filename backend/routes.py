from flask import Blueprint, jsonify, request

from data_utils import (
    create_product_summary,
    filter_products_by_category,
    filter_products_by_price,
    find_product_by_id,
)
from models import ApiResponse, Order, Product, User

api = Blueprint("api", __name__)

products = [
    Product(1, "React Native Course", "education", 49.99, True).to_dict(),
    Product(2, "Mobile UI Kit", "design", 29.99, True).to_dict(),
    Product(3, "Backend API Template", "development", 59.99, False).to_dict(),
    Product(4, "JavaScript Handbook", "education", 19.99, True).to_dict(),
]

users = [
    User(1, "Parth Mehta", "parth@example.com", ["education", "development"]).to_dict(),
    User(2, "John Doe", "john@example.com", ["design"]).to_dict(),
]

orders = [
    Order(1, 1, [1, 3], "processing").to_dict(),
    Order(2, 2, [2], "completed").to_dict(),
]


@api.route("/health", methods=["GET"])
def health_check():
    response = ApiResponse(
        success=True,
        message="Backend API is running",
        data={"status": "ok"},
    )
    return jsonify(response.to_dict()), 200


@api.route("/products", methods=["GET"])
def get_products():
    response = ApiResponse(
        success=True,
        message="Products fetched successfully",
        data=products,
    )
    return jsonify(response.to_dict()), 200


@api.route("/products/summary", methods=["GET"])
def get_product_summary():
    summary = create_product_summary(products)

    response = ApiResponse(
        success=True,
        message="Product summary generated successfully",
        data=summary,
    )
    return jsonify(response.to_dict()), 200


@api.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = find_product_by_id(products, product_id)

    if not product:
        response = ApiResponse(
            success=False,
            message="Product not found",
        )
        return jsonify(response.to_dict()), 404

    response = ApiResponse(
        success=True,
        message="Product fetched successfully",
        data=product,
    )
    return jsonify(response.to_dict()), 200


@api.route("/products/filter", methods=["GET"])
def filter_products():
    category = request.args.get("category")
    max_price = request.args.get("max_price", type=float)

    filtered_products = products

    if category:
        filtered_products = filter_products_by_category(
            filtered_products,
            category,
        )

    if max_price is not None:
        filtered_products = filter_products_by_price(
            filtered_products,
            max_price,
        )

    response = ApiResponse(
        success=True,
        message="Products filtered successfully",
        data=filtered_products,
    )
    return jsonify(response.to_dict()), 200


@api.route("/users", methods=["GET"])
def get_users():
    response = ApiResponse(
        success=True,
        message="Users fetched successfully",
        data=users,
    )
    return jsonify(response.to_dict()), 200


@api.route("/orders", methods=["GET"])
def get_orders():
    response = ApiResponse(
        success=True,
        message="Orders fetched successfully",
        data=orders,
    )
    return jsonify(response.to_dict()), 200