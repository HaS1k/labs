import json, os
from http.server import BaseHTTPRequestHandler, HTTPServer
DATA_DIR = os.environ.get("DATA_DIR", "/data")
DATA_FILE = os.path.join(DATA_DIR, "records.json")
os.makedirs(DATA_DIR, exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"records": ["order-1001", "order-1002"], "storage": "named volume"}, f)
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open(DATA_FILE, encoding="utf-8") as f:
            payload = json.load(f)
        payload["status"] = "ok"
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self, *args): return
if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5432), Handler).serve_forever()
