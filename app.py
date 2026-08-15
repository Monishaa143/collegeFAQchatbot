import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

faq = {
    "admission": "Admissions start every June. Please visit the college admission office for details.",
    "fees": "The annual tuition fee is ₹60,000.",
    "courses": "We offer B.Tech, MBA, MCA, Diploma, and Degree programs.",
    "hostel": "Hostel facilities are available for both boys and girls.",
    "placement": "Top recruiters include TCS, Infosys, Wipro, Capgemini, and Accenture.",
    "library": "The library is open from 9 AM to 6 PM.",
    "contact": "You can contact the college at +91-6281914053 or 9381231981.",
    "college": "VEMU Institute of Technology is located in P. Kothakota, Chittoor, Andhra Pradesh.",
    "location": "VEMU Institute of Technology is located in P. Kothakota, Chittoor, Andhra Pradesh.",
    "courses offered": "We offer B.Tech, MBA, MCA, Diploma, and Degree programs.",
    "fee": "The annual tuition fee is ₹60,000."
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].strip()
    message_lower = user_message.lower()

    # First check your college FAQ
    for keyword, answer in faq.items():
        if keyword in message_lower:
            return jsonify({"reply": answer})

    # Greetings
    if any(word in message_lower.split() for word in ["hi", "hello", "hey"]):
        return jsonify({
            "reply": "Hello! 👋 Welcome to VEMU Institute of Technology. How can I help you?"
        })

    # Thanks
    if "thank" in message_lower:
        return jsonify({
            "reply": "You're welcome! 😊 Feel free to ask me anything."
        })

    # If FAQ doesn't contain the answer, ask OpenAI
    try:

        response = client.responses.create(
            model="gpt-5.6",
            instructions="""
            You are a helpful college assistant for VEMU Institute of Technology.

            Answer questions clearly and simply.

            Use these college details when relevant:
            - College: VEMU Institute of Technology
            - Location: P. Kothakota, Chittoor, Andhra Pradesh
            - Courses: B.Tech, MBA, MCA, Diploma and Degree programs
            - Annual tuition fee: ₹60,000
            - Hostel: Available for boys and girls
            - Library: 9 AM to 6 PM
            - Contact: +91-6281914053 or 9381231981

            If the question is unrelated to VEMU, politely answer if you can,
            but do not invent college-specific information.
            """,
            input=user_message
        )

        return jsonify({
            "reply": response.output_text
        })

    except Exception as e:

        print("OPENAI ERROR:", e)

        return jsonify({
            "reply": "Sorry, I couldn't connect to the AI service right now."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
