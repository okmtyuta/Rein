# Rein, A Very Simple Python Web Framework

## Getting Started
ルートディレクトリで`make runserver`を実行すると開発用サーバーが起動します。
この状態で[`http://localhost:8000`](http://localhost:8000)にアクセスしてみてください。

## ルーティングを追加する。
ルーティングを追加したい場合は，`urls.py`の`url_patterns`に追加してください。例えば，メソッドを`GET`，パスを`/user`，コールバック関数を`user`とするルーティングを追加したい場合は，以下のように記述します。
```python
url_patterns = [
    ...,
    url("GET", "^/user$", user)
]
```
ここで，コールバック関数`user`は以下のような形式である必要があります。
```python
def user(request):
    return Response("Hello user")
```
以上の設定のもとで開発用サーバーを起動し，[`http://localhost:8000/user`](http://localhost:8000/user)にアクセスしてください。

## HTMLを返す
レスポンスとしてHTMLファイルを返却したい場合，`HTMLResponse`を使用してください。具体的にはコールバックを次のように作成します。
```python
def html(request):
  return HTMLResponse(".../path/to/html")
```
`.../path/to/html`を相対パスで扱いたい場合，あらかじめ`setting.py`で`_TEMPLATE_DIRS`を設定しておく必要があります。例えば，`setting.py`で以下のような設定を行ったとします。
```
_TEMPLATE_DIRS = [
    "", ".../packages/template"
  ]
```
このとき，`packages/template`内のHTMLファイルは相対パスで読み込めます。すなわち`packages/template/test.html`は以下のように読み込むことが可能です。
```python
def html(request):
  return HTMLResponse("test.html")
```

## HTMLのテンプレートエンジンを使用する
To be prepared

---

## Memo to be arranged

### WSGI compliant minimum configuration
```python
def application(env, start_response):
    start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
    return [b"Hello World"]
```

### Sample Application
To be prepared...

### Design
To be prepared

### References
[Webアプリケーションフレームワークの作り方 in Python](https://c-bata.link/webframework-in-python/)

### Makefile
To be prepared