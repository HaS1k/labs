import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

DB_URL = os.environ.get("DB_URL", "http://db:5432")
CACHE_URL = os.environ.get("CACHE_URL", "http://cache:6379")
APP_ENV = os.environ.get("APP_ENV", "local")
VERSION = os.environ.get("APP_VERSION", "dev")


def get_text(url, timeout=5):
    with urllib.request.urlopen(url, timeout=timeout) as response:
        return response.read().decode("utf-8").strip()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            payload = {"status": "ok", "environment": APP_ENV, "version": VERSION}
        else:
            db_status = get_text(DB_URL + "/data")
            cache_status = get_text(CACHE_URL + "/cache")
            payload = {
                "message": "Complex CI/CD demo application",
                "environment": APP_ENV,
                "version": VERSION,
                "db": db_status,
                "cache": cache_status,
            }
        body = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
