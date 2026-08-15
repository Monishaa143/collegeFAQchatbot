import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# OpenAI API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# =========================
# VEMU COLLEGE INFORMATION
# =========================

college_info = """
VEMU Institute of Technology
Location: P. Kothakota, Chittoor, Andhra Pradesh

B.Tech Courses:

1. Computer Science and Engineering (CSE)
2. Electronics and Communication Engineering (ECE)
3. Computer Science and Engineering - Artificial Intelligence and Machine Learning (CSE - AI & ML)
4. Computer Science and Engineering - Data Science (CSE - Data Science)
5. Electrical and Electronics Engineering (EEE)
6. Mechanical Engineering

Annual B.Tech Tuition Fee:
₹60,000 per year

Hostel:
Hostel facilities are available for boys and girls.

Library:
Library timings are 9 AM to 6 PM.

Placements:
Top recruiters mentioned include TCS, Infosys, Wipro, Capgemini and Accenture.

Contact:
+91-6281914053
+91-9381231981

Admissions:
Admissions generally start every June.
Students should contact the college for current admission information.
"""


# =========================
# HOME PAGE
# =========================

@app.route("/")
def home():
    return render_template("index.html")


# =========================
# CHAT
# =========================

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].strip()

    if not user_message:
        return jsonify({
            "reply": "Please enter a question."
        })


    # =========================
    # DIRECT FAQ ANSWERS
    # =========================

    message = user_message.lower()


    # Greetings
    if any(word in message.split() for word in ["hi", "hello", "hey"]):

        return jsonify({
            "reply": "Hello! 👋 Welcome to VEMU Institute of Technology. How can I help you?"
        })


    # Thanks
    if "thank" in message:

        return jsonify({
            "reply": "You're welcome! 😊 Feel free to ask me anything about VEMU Institute of Technology."
        })


    # B.Tech branches
    if (
        "btech branches" in message
        or "b.tech branches" in message
        or "branches in btech" in message
        or "branches are available" in message
        or "engineering branches" in message
    ):

        return jsonify({
            "reply": """
🎓 B.Tech branches available at VEMU Institute of Technology:

1. Computer Science and Engineering (CSE)
2. Electronics and Communication Engineering (ECE)
3. CSE - Artificial Intelligence and Machine Learning (AI & ML)
4. CSE - Data Science
5. Electrical and Electronics Engineering (EEE)
6. Mechanical Engineering

💰 Annual B.Tech tuition fee: ₹60,000
"""
        })


    # B.Tech fees
    if (
        "btech fee" in message
        or "btech fees" in message
        or "b.tech fee" in message
        or "b.tech fees" in message
        or "engineering fee" in message
        or "engineering fees" in message
    ):

        return jsonify({
            "reply": "💰 The annual B.Tech tuition fee is ₹60,000."
        })


    # CSE
    if "cse" in message and "fee" in message:

        return jsonify({
            "reply": "💻 B.Tech Computer Science and Engineering (CSE) annual tuition fee is ₹60,000."
        })


    # ECE
    if "ece" in message and "fee" in message:

        return jsonify({
            "reply": "📡 B.Tech Electronics and Communication Engineering (ECE) annual tuition fee is ₹60,000."
        })


    # AI & ML
    if (
        ("ai" in message and "ml" in message)
        or "artificial intelligence" in message
    ) and "fee" in message:

        return jsonify({
            "reply": "🤖 B.Tech CSE - Artificial Intelligence and Machine Learning annual tuition fee is ₹60,000."
        })


    # Data Science
    if "data science" in message and "fee" in message:

        return jsonify({
            "reply": "📊 B.Tech CSE - Data Science annual tuition fee is ₹60,000."
        })


    # EEE
    if "eee" in message and "fee" in message:

        return jsonify({
            "reply": "⚡ B.Tech Electrical and Electronics Engineering (EEE) annual tuition fee is ₹60,000."
        })


    # Mechanical
    if "mechanical" in message and "fee" in message:

        return jsonify({
            "reply": "⚙️ B.Tech Mechanical Engineering annual tuition fee is ₹60,000."
        })


    # =========================
    # OPENAI
    # =========================

    try:

        response = client.responses.create(

            model="gpt-5.6",

            instructions=f"""
You are the official AI College Assistant for VEMU Institute of Technology.

Answer questions clearly, naturally and simply.

Use ONLY the following college information for college-specific facts:

{college_info}

Important:

- Understand different ways of asking the same question.
- If someone asks "What branches are there in B.Tech?",
  provide the B.Tech branch list.
- If someone asks about B.Tech fees,
  tell them the annual tuition fee is ₹60,000.
- If someone asks about a particular B.Tech branch,
  explain that branch using the information provided.
- Do not invent college-specific information.
- If information is unavailable, clearly say that the information
  is not available and advise the student to contact the college.
- You can answer general educational questions using your general knowledge.
""",

            input=user_message
        )


        return jsonify({
            "reply": response.output_text
        })


    except Exception as e:

        print("OPENAI ERROR:", e)

        return jsonify({
            "reply": "Sorry, I couldn't connect to the AI service right now. Please try again later."
        }), 500


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)
