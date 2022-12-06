# Rein, A Very Simple Python Web Framework

## Usage


## 最小形態
```python
def application(env, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"Hello World"]
```