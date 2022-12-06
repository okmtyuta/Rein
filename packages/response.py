from http.client import responses as http_responses
import json
import os
from wsgiref.headers import Headers

from setting import _TEMPLATE_DIRS


class Response:
    default_status = 200
    default_charset = "utf-8"
    default_content_type = "text/html; charset=UTF-8"

    def __init__(self, body="", status=None, headers=None, charset=None):
        self._body = body
        self.status = status or self.default_status
        self.headers = Headers()
        self.charset = charset or self.default_charset

        if headers:
            for name, value in headers.items():
                self.headers.add_header(name, value)

    @property
    def status_code(self):
        return "%d %s" % (self.status, http_responses[self.status])

    @property
    def header_list(self):
        if "Content-Type" not in self.headers:
            self.headers.add_header("Content-Type", self.default_content_type)
        return self.headers.items()

    @property
    def body(self):
        if isinstance(self._body, str):
            return [self._body.encode(self.charset)]
        return [self._body]


class JSONResponse(Response):
    default_content_type = "text/json; charset=UTF-8"

    def __init__(self, dic, status=200, headers=None, charset=None, **dump_args):
        self.dic = dic
        self.json_dump_args = dump_args
        super().__init__("", status=status, headers=headers, charset=charset)

    @property
    def body(self):
        return [
            json.dumps(self.dic, **self.json_dump_args, ensure_ascii=False).encode(
                self.charset
            )
        ]


class HTMLResponse(Response):
    def __init__(self, filename, status=200, headers=None, charset="utf-8"):
        self.filepath = self.get_template_path(filename)
        super().__init__(body="", status=status, headers=headers, charset=charset)

    def read_html(self, path, encoding="utf-8"):
        try:
            with open(path, encoding=encoding) as f:
                html = f.read()
        except:
            html = ""

        return html

    def get_template_path(self, filename):
        for template_dir in _TEMPLATE_DIRS:
            if os.path.exists(os.path.join(template_dir, filename)):
                return os.path.join(template_dir, filename)
            else:
                continue

        return None

    @property
    def body(self):
        html = self.read_html(self.filepath)
        return [html.encode()]
