#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome to gilley's app!</h1>"


@app.route("/<string:username>")
def user(username):
    return f"<h1>Profile for {username}</h1>"

@app.route("/<int:post_id>")
def post(post_id):
    return f"<h1>Post belongs to number{post_id}</h1>"




if __name__ == "__main__":
    app.run(port=5555)