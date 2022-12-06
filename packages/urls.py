# ここにはurlパターンを実装のこと

import views


def url(method, path, callback):
    return {"method": method, "path": path, "callback": callback}


url_patterns = [
    url("GET", "^/$", views.index),
    url("GET", "^/okmtyuta$", views.okmtyuta),
    url("POST", "^/user$", views.hello),
    url("GET", "^/user/(?P<name>\w+)$", views.user_detail),
    url("GET", "^/json", views.json),
    url("GET", "^/html", views.html),
]
