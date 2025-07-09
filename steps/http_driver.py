from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import argparse


class SupportToolHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _send_json(self, data, status=200):
        self._set_headers(status)
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.path == "/health":
            self._send_json({"status": "ok", "message": "Support tool is healthy"})
        else:
            self.send_error(404, "Endpoint not found")

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        raw_data = self.rfile.read(content_length)

        try:
            data = json.loads(raw_data)
        except Exception:
            return self._send_json({"error": "Invalid JSON"}, status=400)

        if self.path == "/upgrade":
            print("Upgrade request received:", data)
            return self._send_json({
                "status": "success",
                "action": "upgrade",
                "version": data.get("target_version", "unknown")
            })

        elif self.path == "/downgrade":
            print("Downgrade request received:", data)
            return self._send_json({
                "status": "success",
                "action": "downgrade",
                "version": data.get("target_version", "unknown")
            })

        elif self.path == "/shutdown":
            print("Shutdown called")
            self._send_json({"status": "ok", "message": "Shutdown complete"})
            # Gracefully stop the server
            def shutdown_server():
                self.server.shutdown()

            import threading
            threading.Thread(target=shutdown_server).start()

        else:
            self.send_error(404, "Invalid endpoint")


def run(host='0.0.0.0', port=5000):
    server_address = (host, port)
    httpd = HTTPServer(server_address, SupportToolHTTPRequestHandler)
    print(f"HTTP REST server started on {host}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Shutting down.")
    finally:
        httpd.server_close()
        print("Server stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='0.0.0.0', help='Bind address')
    parser.add_argument('--port', type=int, default=5000, help='Bind port')
    args = parser.parse_args()

    run(host=args.host, port=args.port)
