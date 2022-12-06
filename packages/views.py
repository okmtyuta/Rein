# ここにはview関数を実装のこと

from response import Response, JSONResponse


def index(request):
    return Response("THIS PAGE IS indeX")


def json(request):
    return JSONResponse({"name": "okmtyuta", "greet": "こんにちは"}, charset="utf-8")


def okmtyuta(request):
    return Response("Hello okmtyuta")


def hello(request):
    print(request.body.decode("utf-8"))
    return Response("User is created")


def user_detail(request, name):
    print(name)
    body = "こんにちは {name}".format(name=name)
    return Response(body.encode("utf-8"))
