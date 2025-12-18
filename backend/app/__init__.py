import os
from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from .routes.health import health_blp

def _get_allowed_origins_from_env() -> list[str]:
    """
    Resolve allowed CORS origins from environment variables.
    Priority:
    1) REACT_APP_FRONTEND_URL
    2) REACT_APP_BACKEND_URL (rarely needed for CORS but included as fallback)
    Default: http://localhost:3000
    Multiple origins can be comma-separated.
    """
    origins_raw = os.getenv("REACT_APP_FRONTEND_URL") or os.getenv("REACT_APP_BACKEND_URL") or "http://localhost:3000"
    # Split comma-separated values and trim
    return [o.strip() for o in origins_raw.split(",") if o.strip()]

# Initialize app
app = Flask(__name__)
app.url_map.strict_slashes = False

# Configure CORS using env with sensible defaults
allowed_origins = _get_allowed_origins_from_env()
CORS(
    app,
    resources={r"/*": {"origins": allowed_origins}},
    supports_credentials=True,
)

# OpenAPI/Swagger configuration
app.config["API_TITLE"] = "AI Test Automation Platform API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
# Keep Swagger UI at /docs
app.config["OPENAPI_URL_PREFIX"] = "/docs"
app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Initialize API and register blueprints
api = Api(app)
api.register_blueprint(health_blp)
