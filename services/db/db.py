import json
import os
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

DB_FILE = os.environ.get("DB_FILE", "/data/storage.json")
DEFAULT_MESSAGE = os.environ.get("DB_MESSAGE", "Hello from local database service")
PORT = int(os.environ.get("DB_PORT", "7000"))

def load_data():
    if not os.path.exists(DB_FILE):
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        save_data({"message": DEFAULT_MESSAGE})
    with open(DB_FILE, "r", encoding="utf-8") as fh:
        return json.load(fh)

def save_data(data):
    os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
    with open(DB_FILE, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        data = load_data()
        if parsed.path == "/health":
            body = "db=ok\n"
        elif parsed.path == "/get":
            key = query.get("key", ["message"])[0]
            body = str(data.get(key, "")) + "\n"
        elif parsed.path == "/set":
            key = query.get("key", ["message"])[0]
            value = query.get("value", [""])[0]
            data[key] = value
            save_data(data)
            body = "stored\n"
        else:
            self.send_response(404)
            self.end_headers()
            return
        encoded = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, fmt, *args):
        return

if __name__ == "__main__":
    load_data()
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
