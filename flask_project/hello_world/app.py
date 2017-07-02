from flask import Flask, request, current_app, g 
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello"

if __name__ == "__main__":
    app.run()


