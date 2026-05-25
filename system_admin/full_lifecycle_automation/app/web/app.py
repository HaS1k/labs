import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

DB_URL = os.environ.get("DB_URL", "http://db:5432")
CACHE_URL = os.environ.get("CACHE_URL", "http://cache:6379")
WORKER_URL = os.environ.get("WORKER_URL", "http://worker:5555")
APP_ENV = os.environ.get("APP_ENV", "local")
APP_VERSION = os.environ.get("APP_VERSION", "dev")

def fetch(url):
    with urllib.request.urlopen(url, timeout=5) as r:
        return json.loads(r.read().decode("utf-8"))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            payload = {"status": "ok", "environment": APP_ENV, "version": APP_VERSION}
        else:
            payload = {
                "message": "Full lifecycle automation demo",
                "environment": APP_ENV,
                "version": APP_VERSION,
                "db": fetch(DB_URL + "/data"),
                "cache": fetch(CACHE_URL + "/cache"),
                "worker": fetch(WORKER_URL + "/job"),
            }
        body = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, *args):
        return

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
