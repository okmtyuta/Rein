# ここにはurlパターンを実装のこと

from views import okmtyuta, index

def url(method, path, callback):
    return {
        "method": method,
        "path": path,
        "callback": callback
    }

url_patterns = [
    url("GET", "^/$", index),
    url("GET", "^/okmtyuta$", okmtyuta)
]
