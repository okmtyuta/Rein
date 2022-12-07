# ここにはurlパターンを実装のこと

import views


def url(method, path, callback):
    return {"method": method, "path": path, "callback": callback}


url_patterns = [
    url("GET", "^/$", views.index),
    url("POST", "^/post-json$", views.post_json),
    url("GET", "^/get/(?P<name>\w+)$", views.get_param),
    url("GET", "^/get-json", views.get_json),
    url("GET", "^/return-html", views.return_html),
]
