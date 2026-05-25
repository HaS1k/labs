import json
import sys
import urllib.request

url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:18081/health"
with urllib.request.urlopen(url, timeout=10) as response:
    payload = json.loads(response.read().decode("utf-8"))
print(json.dumps(payload, ensure_ascii=False, indent=2))
assert payload["status"] == "ok"
