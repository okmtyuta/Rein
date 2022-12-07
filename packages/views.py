# ここにはview関数を実装のこと
import json

from response import Response, JSONResponse, HTMLResponse


def index(request):
    return Response("Welcome To Rein, A Very Simple Python Web Framework")


def get_json(request):
    return JSONResponse({"key": "value"}, charset="utf-8")


def post_json(request):
    return Response(f"You posted: {json.loads(request.body)}")


def get_param(request, name):
    body = f"こんにちは {name}さん。ご用件をお伺いいたします。"
    return Response(body.encode("utf-8"))


def return_html(request):
    return HTMLResponse("test.html")
