# Support Tool Driver with REST API

A Labgrid-compatible mock driver to upgrade/downgrade software on medical devices via REST API.

## Features

- Python driver mimicking Labgrid structure
- REST-based upgrade/downgrade flow
- Pytest test suite
- CLI + GitHub Actions integration

## Usage

Start the mock HTTP server:

```bash
./scripts/start_server.sh

###############################

day1: # Support Tool Mock HTTP Server

This is a simple HTTP server implementation to simulate a REST-based interface for upgrading and downgrading a medical device using Python's built-in `http.server` module.

## 📦 Features

- ✅ Health check endpoint (`/health`)
- 🔼 Upgrade endpoint (`/upgrade`)
- 🔽 Downgrade endpoint (`/downgrade`)
- 🛑 Shutdown endpoint (`/shutdown`)

## 🚀 Getting Started

### 🧱 Prerequisites

- Python 3.8+
- No external dependencies

### ▶️ Run the Server

```bash
python steps/http_driver.py --port 8080 --host 127.0.0.1
You should see:

nginx
Copy
Edit
HTTP REST server started on 127.0.0.1:8080
🔁 API Usage
✅ Health Check
bash
Copy
Edit
curl http://127.0.0.1:8080/health
Response:

json
Copy
Edit
{
  "status": "ok",
  "message": "Support tool is healthy"
}
🔼 Upgrade Device
bash
Copy
Edit
curl -X POST http://127.0.0.1:8080/upgrade \
  -H "Content-Type: application/json" \
  -d '{"device_id": "MD001", "target_version": "2.1.0", "options": {"force": true}}'
Response:

json
Copy
Edit
{
  "status": "success",
  "action": "upgrade",
  "version": "2.1.0"
}
🔽 Downgrade Device
bash
Copy
Edit
curl -X POST http://127.0.0.1:8080/downgrade \
  -H "Content-Type: application/json" \
  -d '{"device_id": "MD001", "target_version": "1.2.0"}'
Response:

json
Copy
Edit
{
  "status": "success",
  "action": "downgrade",
  "version": "1.2.0"
}
🛑 Shutdown
bash
Copy
Edit
curl -X POST http://127.0.0.1:8080/shutdown
Response:

json
Copy
Edit
{
  "status": "ok",
  "message": "Shutdown complete"
}
📁 File Structure
Copy
Edit
support-tool/
├── steps/
│   └── http_driver.py
├── step_tests/
│   └── test_supporttool_labgrid.py
└── README.md
🧪 Tests
You can run the tests using:

bash
Copy
Edit
pytest step_tests/test_supporttool_labgrid.py
Make sure the server is running before testing.