from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_reply():
    user_msg = request.args.get("msg")
    return jsonify(get_bot_response(user_msg))

if __name__ == "__main__":
    app.run(debug=True)
