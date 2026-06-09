from flask import Flask

try:
    from .routes import api
except ImportError:
    from routes import api


def create_app():
    """
    Creates and configures the Flask backend app.
    """

    app = Flask(__name__)

    app.register_blueprint(api, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def home():
        return {
            "message": "React Native Capstone Backend Service",
            "available_routes": [
                "/api/health",
                "/api/users",
                "/api/tasks",
            ],
        }

    return app


if __name__ == "__main__":
    backend_app = create_app()
    backend_app.run(debug=True, host="127.0.0.1", port=5000)