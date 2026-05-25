import os
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", "7000"))
CACHE_HOST = os.environ.get("CACHE_HOST", "cache")
CACHE_PORT = int(os.environ.get("CACHE_PORT", "7001"))
APP_ENV = os.environ.get("APP_ENV", "dev")

def read_url(url):
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read().decode().strip()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/health"):
            body = "web=ok\n"
        else:
            db_url = f"http://{DB_HOST}:{DB_PORT}/get?key=message"
            message = read_url(db_url)
            cache_value = urllib.parse.quote(f"last_request_from_{APP_ENV}")
            cache_url = f"http://{CACHE_HOST}:{CACHE_PORT}/set?key=last_request&value={cache_value}"
            cache_reply = read_url(cache_url)
            body = f"web=ok\nenv={APP_ENV}\ndb_message={message}\ncache={cache_reply}\n"
        data = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        return

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
