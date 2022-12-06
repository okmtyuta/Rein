# ここにはview関数を実装のこと

def index(request):
    return [b"THIS PAGE IS indeX"]

def okmtyuta(request):
    return [b"Hello okmtyuta"]

def hello(request):
    print(request.body.decode('utf-8'))
    return [b'User is created']

def user_detail(request, name):
    print(name)
    body = 'Hello {name}'.format(name=name)
    return [body.encode('utf-8')]