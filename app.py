from flask import Flask, request, abort
from werkzeug.utils import secure_filename
import os
from pathlib import Path
import json


DATA_DIR = os.environ.get("DATA_DIR", "./data")

app = Flask(__name__)


@app.get("/get/<fname>")
def get(fname):
    fname = secure_filename(fname)
    fname = os.path.join(Path(DATA_DIR), fname)
    try:
        data = Path(fname).read_text()
        return json.loads(data)
    except IOError:
        abort(404)


@app.put("/put/<fname>")
def put(fname):
    fname = secure_filename(fname)
    fname = os.path.join(Path(DATA_DIR), fname)
    Path(fname).write_text(json.dumps(request.get_json(force=True)))
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
