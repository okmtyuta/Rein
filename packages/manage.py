import argparse
from wsgiref.simple_server import make_server

from app import App


def main(args):
    if args.action == "runserver":
        app = App()

        @app.route("^/$", "GET")
        def hello(request, start_response):
            start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
            return [b"Hello World"]

        @app.route("^/user/$", "POST")
        def create_user(request, start_response):
            start_response(
                "201 Created", [("Content-type", "text/plain; charset=utf-8")]
            )
            return [b"User Created"]

        @app.route("^/user/(?P<name>\w+)/$", "GET")
        def user_detail(request, start_response, name):
            start_response("200 OK", [("Content-type", "text/plain; charset=utf-8")])
            body = "Hello {name}".format(name=name)
            return [body.encode("utf-8")]

        @app.route("^/user/(?P<name>\w+)/follow/$", "POST")
        def create_user(request, start_response, name):
            start_response(
                "201 Created", [("Content-type", "text/plain; charset=utf-8")]
            )
            body = "Followed {name}".format(name=name)
            return [body.encode("utf-8")]

        httpd = make_server("", 8000, app)
        
        print("Server started on http://localhost:8000")
        httpd.serve_forever()


    else:
        print("YOU CAN SELECT ONLY RUNSERVER")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--action", help="")

    args = parser.parse_args()

    app = main(args)
