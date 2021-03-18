from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def server_status():
    return "The server is on!"

@app.route("/info", methods=["GET"])
def information():
    output = "This server will allow users to request blood analysis"
    return output

if __name__ == "__main__":
    app.run()