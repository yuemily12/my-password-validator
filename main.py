from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from my Password Validator!"


@app.route("/checkPassword", methods=["POST"])
def check_password():
    data = request.get_json() or {}
    pw = data.get("password", "")

    # FIXME: To be implemented
    return jsonify({"valid": False, "reason": "Not implemented"}), 501
