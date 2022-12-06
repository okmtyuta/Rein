import argparse
from wsgiref.simple_server import make_server

from app import App
from urls import url_patterns


def main(args):
    if args.action == "runserver":
        app = App()

        for url_pattern in url_patterns:
            app.router.add(url_pattern[0], url_pattern[1], url_pattern[2])

        httpd = make_server("", 8000, app)

        print(f"Server started on http://localhost:{args.port}")
        httpd.serve_forever()


    else:
        print("YOU CAN SELECT ONLY RUNSERVER")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--action", default="runserver", help="")
    parser.add_argument("--port", default=8000, help="")

    args = parser.parse_args()

    app = main(args)
