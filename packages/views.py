# ここにはview関数を実装のこと

def index(request, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"THIS PAGE IS INDEX"]

def okmtyuta(request, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"Hello okmtyuta"]