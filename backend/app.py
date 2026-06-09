from flask import Flask

from routes import api


def create_app():
    """Creates and configures the Flask app."""

    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def home():
        return {
            "message": "React Native Capstone Python Backend API",
            "endpoints": [
                "/api/health",
                "/api/products",
                "/api/products/summary",
                "/api/products/1",
                "/api/products/filter?category=education",
                "/api/users",
                "/api/orders",
            ],
        }

    return app


if __name__ == "__main__":
    backend_app = create_app()
    backend_app.run(debug=True, host="127.0.0.1", port=5000)