# AI Test Automation Backend (Flask)

This backend provides API endpoints for the AI Test Automation platform and a simple health endpoint used by the React frontend Navbar.

## Quick Start
1. Create a virtual environment and install dependencies (instructions depend on actual project setup).
2. Configure environment:
   - Copy `.env.example` to `.env`.
   - Ensure:
     - `PORT=3001`
     - `CORS_ORIGINS=http://localhost:3000`
3. Run the server:
   - Start the Flask app so it listens on port 3001.

## Health Endpoint
- The frontend calls the configured health path (default `/`) on `http://localhost:3001`.
- Return either JSON (e.g., `{ "status": "OK" }`) or plain text (`OK`).
- A 200 OK response results in the frontend showing "Backend: Healthy".
- If the endpoint is unreachable or returns an error, the frontend shows "Backend: Unreachable".

## Verify End-to-End
1. Start the backend on port 3001 with CORS allowing `http://localhost:3000`.
2. Start the React frontend at `http://localhost:3000` with `REACT_APP_API_BASE=http://localhost:3001` and optional `REACT_APP_HEALTHCHECK_PATH=/`.
3. Visit the frontend in a browser:
   - The Navbar badge should display: "Backend: Healthy".
   - If not healthy, check:
     - Backend is running and accessible on port 3001.
     - CORS headers allow origin `http://localhost:3000`.
     - Health endpoint path matches `REACT_APP_HEALTHCHECK_PATH` (default `/`).
