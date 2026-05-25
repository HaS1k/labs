import json, sys, urllib.request
url = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:19080/health"
with urllib.request.urlopen(url, timeout=10) as r:
    payload = json.loads(r.read().decode())
print(json.dumps(payload, ensure_ascii=False, indent=2))
assert payload["status"] == "ok"
