import os
from datetime import datetime, timezone
from flask.views import MethodView
from flask_smorest import Blueprint

# Create blueprint for health-related endpoints
health_blp = Blueprint(
    "Health",
    "health",
    url_prefix="/",
    description="Health check endpoints"
)

# PUBLIC_INTERFACE
@health_blp.route("/", methods=["GET"])
class RootHealth(MethodView):
    """
    Root health endpoint.
    Returns a minimal JSON payload to indicate service readiness.
    """
    def get(self):
        return {
            "status": "ok",
            "message": "Service is healthy",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "service": "backend",
            "details": {
                "env": {
                    "REACT_APP_NODE_ENV": os.getenv("REACT_APP_NODE_ENV", "development"),
                }
            }
        }, 200

# PUBLIC_INTERFACE
@health_blp.route("/health", methods=["GET"])
class Health(MethodView):
    """
    Detailed health endpoint.
    Provides status plus selected configuration values for diagnostics.
    """
    def get(self):
        return {
            "status": "ok",
            "uptime_hint": "N/A",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "service": "backend",
            "config": {
                "allowed_origins": (os.getenv("REACT_APP_FRONTEND_URL") or os.getenv("REACT_APP_BACKEND_URL") or "http://localhost:3000"),
                "port": int(os.getenv("REACT_APP_PORT") or os.getenv("PORT") or 3001),
                "health_path": os.getenv("REACT_APP_HEALTHCHECK_PATH", "/health"),
                "log_level": os.getenv("REACT_APP_LOG_LEVEL", "info"),
                "node_env": os.getenv("REACT_APP_NODE_ENV", "development"),
                "ws_url": os.getenv("REACT_APP_WS_URL", ""),
            }
        }, 200
