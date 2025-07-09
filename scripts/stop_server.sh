#!/bin/bash
if [ -f ../support_tool_server.pid ]; then
  PID=$(cat ../support_tool_server.pid)
  echo "Stopping server with PID $PID"
  kill $PID
  rm ../support_tool_server.pid
else
  echo "No running server found."
fi
