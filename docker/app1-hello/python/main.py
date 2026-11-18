from flask import Flask, jsonify
import os, socket

app = Flask(__name__)

ENV = os.getenv("ENV_VALUE", "No env set")
DB_PASSWORD = os.getenv('DB_PASSWORD')
MESSAGE = os.getenv('APP_MESSAGE')
HOSTNAME = socket.gethostname()
APP_SECRET = os.getenv('APP_SECRET')

@app.get("/")
def hello():
    return jsonify({
        "message": MESSAGE,
        "env": ENV,
        "container": HOSTNAME,
        "secret": APP_SECRET
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
