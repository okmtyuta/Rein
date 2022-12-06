# Rein, A Very Simple Python Web Framework

## Usage
Try: `make runserver`, then access: `http://localhost:8000`

## 最小形態
```python
def application(env, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"Hello World"]
```