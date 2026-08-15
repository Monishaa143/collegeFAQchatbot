import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            instructions=(
                "You are a helpful college assistant for "
                "VEMU Institute of Technology. "
                "Answer clearly and simply."
            ),
            input=user_message
        )

        return jsonify({
            "reply": response.output_text
        })

    except Exception as e:
        return jsonify({
            "reply": "Sorry, I am unable to answer right now."
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
