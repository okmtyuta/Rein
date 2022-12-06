# ここにはurlパターンを実装のこと

from views import okmtyuta, index, hello, user_detail, json


def url(method, path, callback):
    return {"method": method, "path": path, "callback": callback}


url_patterns = [
    url("GET", "^/$", index),
    url("GET", "^/okmtyuta$", okmtyuta),
    url("POST", "^/user$", hello),
    url("GET", "^/user/(?P<name>\w+)$", user_detail),
    url("GET", "^/json", json),
]
