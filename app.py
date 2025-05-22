import os

from flask import Flask, jsonify, send_file, abort

app = Flask(__name__)


@app.route("/<filename>")
def serve_txt_file(filename):
    if not filename.endswith(".txt"):
        abort(404)

    txt_file_path = os.path.join("static", filename)

    if os.path.exists(txt_file_path) and os.path.isfile(txt_file_path):
        return send_file(txt_file_path, mimetype="text/plain")
    else:
        abort(404)


@app.route("/")
def index():
    return jsonify({"message": "use /<filename> to see your files."})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
