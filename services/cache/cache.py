import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

STORE = {}
PORT = 7001

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed.query)
        if parsed.path == "/health":
            body = "cache=ok\n"
        elif parsed.path == "/get":
            key = query.get("key", [""])[0]
            body = STORE.get(key, "") + "\n"
        elif parsed.path == "/set":
            key = query.get("key", [""])[0]
            value = query.get("value", [""])[0]
            STORE[key] = value
            body = "stored_in_cache\n"
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
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
