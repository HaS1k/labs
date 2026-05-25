import json, time
from http.server import BaseHTTPRequestHandler, HTTPServer
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        payload = {"status": "ok", "worker": "background-jobs", "last_job": "notification-sync", "timestamp": int(time.time())}
        body = json.dumps(payload, ensure_ascii=False).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
    def log_message(self, *args): return
if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 5555), Handler).serve_forever()
