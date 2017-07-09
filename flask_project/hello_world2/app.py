# encoding: utf-8

import sys, os, logging, json
from flask import Flask, render_template, request, current_app, g
app = Flask(__name__)

# comment...
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/get/<id>", methods=["GET"])
def api_get(id):
    print "request.args:", request.args
    print "request.get_data()", request.get_data()
    print dir(request)
    data = {"id": id, "name":"中文"}
    return json.dumps(data)

@app.route("/api/post", methods=["POST"])
def api_post():
    print "request.get_data()", request.get_data()
    print "request.get_json()", request.get_json()
    print "request.data", request.data
    print "request.form", request.form
    data = json.loads(request.data)
    print "dict:", data, data["data"][0]
    return '''{"message": "hello"}'''

# ...
if __name__ == "__main__":
    app.run()


