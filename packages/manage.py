import argparse
from wsgiref.simple_server import make_server

from app import App
from urls import url_patterns


def main(args):
    # 開発用サーバー起動用
    if args.action == "runserver":
        app = App()

        for url_pattern in url_patterns:
            app.router.add(
                url_pattern["method"], url_pattern["path"], url_pattern["callback"]
            )

        httpd = make_server("", int(args.port), app)
        print(f"Server started on http://localhost:{args.port}")
        httpd.serve_forever()

    else:
        print("YOU CAN SELECT ONLY RUNSERVER")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rein管理プログラム")
    parser.add_argument("--action", default="runserver", help="manage.pyのアクション指定")
    parser.add_argument("--port", default=8000, help="開発用サーバーを起動するためのポート指定")

    args = parser.parse_args()

    main(args)
