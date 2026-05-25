import os
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

WEB_HOST = os.environ.get("WEB_HOST", "web")
WEB_PORT = int(os.environ.get("WEB_PORT", "5000"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        target = f"http://{WEB_HOST}:{WEB_PORT}{self.path}"
        try:
            with urllib.request.urlopen(target, timeout=5) as response:
                data = response.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception as exc:
            data = f"proxy_error={exc}\n".encode()
            self.send_response(502)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

    def log_message(self, fmt, *args):
        return

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
