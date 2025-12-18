# ai-test-automation-platform-7982-7991

This workspace hosts the Flask backend for the AI Test Automation platform.

- Expected port: 3001 (env `PORT=3001`)
- CORS must allow the frontend origin: `CORS_ORIGINS=http://localhost:3000`
- Health endpoint: `/` (or update the frontend `REACT_APP_HEALTHCHECK_PATH` accordingly)

End-to-end verification:
- With backend running at http://localhost:3001 and frontend at http://localhost:3000
- The frontend Navbar should show: "Backend: Healthy"
