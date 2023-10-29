from flask import Flask, render_template, request, jsonify
from process import ChatBot

app = Flask(__name__)
chatbot = ChatBot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    msg = request.form["msg"]
    if msg:
        response = chatbot.generate_response(msg)
    else:
        response = "Saya tidak mengerti itu"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)