# Rein, A Very Simple Python Web Framework

## Usage
Try: `make runserver`, then access: [`http://localhost:8000`](http://localhost:8000)

## MINIMUM:MEMO
```python
def application(env, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"Hello World"]
```

## Sample apps
To be prepared...

## References
[Webアプリケーションフレームワークの作り方 in Python](https://c-bata.link/webframework-in-python/)