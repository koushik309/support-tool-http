#!/bin/bash
echo "Starting support tool HTTP server..."
python3 ../http_driver.py --port 5000 &
echo $! > ../support_tool_server.pid
echo "Server started on port 5000"
