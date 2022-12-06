# ここにはview関数を実装のこと

from response import Response, JSONResponse, HTMLResponse


def index(request):
    return Response("THIS PAGE IS indeX")


def json(request):
    return JSONResponse({"name": "okmtyuta", "greet": "こんにちは"}, charset="utf-8")


def okmtyuta(request):
    return Response("Hello okmtyuta")


def hello(request):
    return Response("User is created")


def user_detail(request, name):
    print(name)
    body = f"こんにちは {name}さん。ご用件をお伺いいたします。"
    return Response(body.encode("utf-8"))


def html(request):
    return HTMLResponse("test.html")
