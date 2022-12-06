# Rein, A Very Simple Python Web Framework

## Usage
Try: `make runserver`, then access: [`http://localhost:8000`](http://localhost:8000)

### Add Routing
If you want to add routing, you edit `url_patterns` in `urls.py`. For instance, if you want to make routing: "user", you add a url_pattern as following,
```python
url_patterns = [
    ...,
    ["GET", "/user", user]
]
```
where `user` is a function defined as:
```python
def user(request, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"Hello user"]
```
In this situation, you can get "Hello user" on `http://localhost:8000`

## MINIMUM:MEMO
```python
def application(env, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"Hello World"]
```

## Sample apps
To be prepared...

## Future
完成目標はfuture.mdを参照のこと。

## References
[Webアプリケーションフレームワークの作り方 in Python](https://c-bata.link/webframework-in-python/)