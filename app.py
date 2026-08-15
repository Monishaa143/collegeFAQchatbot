from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# =========================
# COLLEGE INFORMATION
# =========================

faq = {

    "admission": "Admissions start every June. Please visit the college admission office for details.",

    "college": "VEMU Institute of Technology is located in P. Kothakota, Chittoor, Andhra Pradesh.",

    "location": "VEMU Institute of Technology is located in P. Kothakota, Chittoor, Andhra Pradesh.",

    "hostel": "Hostel facilities are available for both boys and girls. Hostel fee is ₹30,000 per year.",

    "hostel fee": "The hostel fee is ₹30,000 per year.",

    "library": "The library is open from 9 AM to 6 PM.",

    "contact": "You can contact the college at +91-6281914053 or 9381231981.",

    "placement": "Top recruiters include TCS, Infosys, Wipro, Capgemini, and Accenture.",

    "courses": """VEMU Institute of Technology offers the following B.Tech branches:

1. Computer Science and Engineering (CSE)
2. Electronics and Communication Engineering (ECE)
3. CSE - Artificial Intelligence and Machine Learning (AI & ML)
4. CSE - Data Science
5. Electrical and Electronics Engineering (EEE)
6. Mechanical Engineering
7. Civil Engineering
""",

    "cse": "B.Tech Computer Science and Engineering (CSE) fee is ₹1,50,000 per year.",

    "ece": "B.Tech Electronics and Communication Engineering (ECE) fee is ₹80,000 per year.",

    "ai ml": "B.Tech CSE - Artificial Intelligence and Machine Learning (AI & ML) fee is ₹1,20,000 per year.",

    "data science": "B.Tech CSE - Data Science fee is ₹1,60,000 per year.",

    "eee": "B.Tech Electrical and Electronics Engineering (EEE) fee is ₹75,000 per year.",

    "mechanical": "B.Tech Mechanical Engineering fee is ₹50,000 per year.",

    "civil": "B.Tech Civil Engineering fee is ₹50,000 per year."
}


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

    user_message = request.json.get("message", "").lower().strip()

    if not user_message:
        return jsonify({
            "reply": "Please enter a question."
        })


    # =========================
    # GREETINGS
    # =========================

    if user_message in ["hi", "hello", "hey", "hii", "hiii"]:

        return jsonify({
            "reply": "Hello! 👋 Welcome to VEMU Institute of Technology. How can I help you?"
        })


    # =========================
    # THANK YOU
    # =========================

    if "thank" in user_message:

        return jsonify({
            "reply": "You're welcome! 😊 Feel free to ask me anything about VEMU Institute of Technology."
        })


    # =========================
    # ALL B.TECH BRANCHES
    # =========================

    if (
        "btech branches" in user_message
        or "b.tech branches" in user_message
        or "branches in btech" in user_message
        or "branches in b.tech" in user_message
        or "what branches" in user_message
        or "which branches" in user_message
    ):

        return jsonify({
            "reply": """🎓 B.Tech branches at VEMU Institute of Technology:

1. Computer Science and Engineering (CSE)
   💰 Fee: ₹1,50,000/year

2. Electronics and Communication Engineering (ECE)
   💰 Fee: ₹80,000/year

3. CSE - Artificial Intelligence and Machine Learning (AI & ML)
   💰 Fee: ₹1,20,000/year

4. CSE - Data Science
   💰 Fee: ₹1,60,000/year

5. Electrical and Electronics Engineering (EEE)
   💰 Fee: ₹75,000/year

6. Mechanical Engineering
   💰 Fee: ₹50,000/year

7. Civil Engineering
   💰 Fee: ₹50,000/year
"""
        })


    # =========================
    # HOSTEL FEE
    # =========================

    if (
        "hostel fee" in user_message
        or "hostel fees" in user_message
        or "fee for hostel" in user_message
        or "hostel cost" in user_message
    ):

        return jsonify({
            "reply": "🏠 The hostel fee is ₹30,000 per year for boys and girls."
        })


    # =========================
    # COURSE-SPECIFIC FEES
    # =========================

    # CSE
    if (
        ("cse" in user_message)
        and ("fee" in user_message or "fees" in user_message)
    ):

        return jsonify({
            "reply": "💻 B.Tech Computer Science and Engineering (CSE) fee is ₹1,50,000 per year."
        })


    # ECE
    if (
        ("ece" in user_message)
        and ("fee" in user_message or "fees" in user_message)
    ):

        return jsonify({
            "reply": "📡 B.Tech Electronics and Communication Engineering (ECE) fee is ₹80,000 per year."
        })


    # AI & ML
    if (
        (
            ("ai" in user_message and "ml" in user_message)
            or "artificial intelligence" in user_message
        )
        and ("fee" in user_message or "fees" in user_message)
    ):

        return jsonify({
            "reply": "🤖 B.Tech CSE - Artificial Intelligence and Machine Learning (AI & ML) fee is ₹1,20,000 per year."
        })


    # Data Science
    if (
        "data science" in user_message
        and ("fee" in user_message or "fees" in user_message)
    ):

        return jsonify({
            "reply": "📊 B.Tech CSE - Data Science fee is ₹1,60,000 per year."
        })


    # EEE
    if (
        "eee" in user_message
        and ("fee" in user_message or "fees" in user_message)
    ):

        return jsonify({
            "reply": "⚡ B.Tech Electrical and Electronics Engineering (EEE) fee is ₹75,000 per year."
        })


    # Mechanical
    if (
        "mechanical" in user_message
        and ("fee" in user_message or "fees" in user_message)
    ):

        return jsonify({
            "reply": "⚙️ B.Tech Mechanical Engineering fee is ₹50,000 per year."
        })


    # Civil
    if (
        "civil" in user_message
        and ("fee" in user_message or "fees" in user_message)
    ):

        return jsonify({
            "reply": "🏗️ B.Tech Civil Engineering fee is ₹50,000 per year."
        })


    # =========================
    # GENERAL FAQ MATCHING
    # =========================

    for keyword, answer in faq.items():

        if keyword in user_message:

            return jsonify({
                "reply": answer
            })


    # =========================
    # UNKNOWN QUESTION
    # =========================

    return jsonify({
        "reply": """Sorry, I don't have information about that yet. 🤖

You can ask me about:

🎓 B.Tech branches
💰 Course fees
🏠 Hostel fees
📚 Courses
📝 Admissions
💼 Placements
📖 Library
📍 College location
📞 Contact details"""
    })


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)
