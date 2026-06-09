from flask import Flask

from routes import api


def create_app():
    """
    Creates and configures the Flask application.
    """

    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def home():
        return {
            "message": "Capstone Backend using OOP Service Layer",
            "endpoints": [
                "/api/health",
                "/api/users",
                "/api/users/active",
                "/api/users/emails",
                "/api/products",
                "/api/products/summary",
                "/api/products/filter?category=education",
                "/api/orders",
                "/api/orders/user/1"
            ]
        }

    return app


if __name__ == "__main__":
    backend_app = create_app()
    backend_app.run(debug=True, host="127.0.0.1", port=5000)