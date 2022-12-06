# ここにはurlパターンを実装のこと

from views import okmtyuta, index

url_patterns = [
    ["GET", "/", index],
    ["GET", "/okmtyuta", okmtyuta]
]
