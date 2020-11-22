from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', method=['GET'])
def hello_world():
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
