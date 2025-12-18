import os
from app import app

if __name__ == "__main__":
    # Read port from environment variables, default 3001
    port_str = os.getenv("REACT_APP_PORT") or os.getenv("PORT") or "3001"
    try:
        port = int(port_str)
    except ValueError:
        port = 3001

    # Bind to 0.0.0.0 for containerized environments
    app.run(host="0.0.0.0", port=port)
