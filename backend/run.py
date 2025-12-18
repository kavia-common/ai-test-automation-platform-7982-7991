import os
import socket
import sys
from contextlib import closing
from app import app

def _is_port_in_use(host: str, port: int) -> bool:
    """
    Check whether a TCP port is already in use on the given host.

    Returns True if a connection can be established (port is occupied),
    otherwise False.
    """
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(0.5)
        try:
            return sock.connect_ex((host, port)) == 0
        except OSError:
            # If we cannot attempt to connect, assume not in use for our purposes
            return False

def _resolve_port() -> int:
    """
    Decide the port to use with priority:
    1) REACT_APP_PORT
    2) PORT
    3) default 3001
    """
    port_str = os.getenv("REACT_APP_PORT") or os.getenv("PORT") or "3001"
    try:
        return int(port_str)
    except (TypeError, ValueError):
        # Fallback to default if invalid
        return 3001

def _log(msg: str) -> None:
    """Lightweight logger to stdout."""
    print(f"[backend] {msg}", flush=True)

if __name__ == "__main__":
    host = "0.0.0.0"  # Bind to all interfaces (container-friendly)
    requested_port = _resolve_port()

    # Check port usage on localhost and 0.0.0.0 to be conservative
    in_use_localhost = _is_port_in_use("127.0.0.1", requested_port)
    in_use_all = _is_port_in_use("0.0.0.0", requested_port)
    port_in_use = in_use_localhost or in_use_all

    # If the requested port is 3001 and appears in use, assume preview orchestrator is serving it
    if port_in_use and requested_port == 3001:
        _log(
            "Detected that port 3001 is already in use. "
            "This environment's preview orchestrator likely already runs the backend. "
            "Exiting to avoid a conflict. If you need a manual instance, set PORT to a different value."
        )
        _log("Hint: try `PORT=3010 python -m flask run` or `PORT=3010 python backend/run.py`")
        sys.exit(0)

    # If a different env-specified port is in use, exit with a clear message
    if port_in_use and requested_port != 3001:
        _log(
            f"Requested PORT={requested_port} is already in use. "
            "Please choose another port (e.g., set PORT to a free value). Exiting."
        )
        sys.exit(1)

    _log(f"Starting Flask app on {host}:{requested_port}")
    # Bind to 0.0.0.0 for containerized environments; ensure threaded server for dev convenience
    app.run(host=host, port=requested_port, threaded=True)
