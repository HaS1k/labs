import json
from http.server import BaseHTTPRequestHandler, HTTPServer
CACHE = {"status": "ok", "backend": "cache", "keys": ["session", "homepage", "metrics"]}
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps(CACHE, ensure_ascii=False).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self, *args): return
if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 6379), Handler).serve_forever()
