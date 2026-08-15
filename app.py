from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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

    "cse": "B.Tech Computer Science and Engineering (CSE) is offered at VEMU Institute of Technology. The annual tuition fee is ₹60,000.",
    "ece": "B.Tech Electronics and Communication Engineering (ECE) is offered at VEMU Institute of Technology. The annual tuition fee is ₹60,000.",
    "ai ml": "B.Tech CSE - Artificial Intelligence and Machine Learning (AI & ML) is offered at VEMU Institute of Technology. The annual tuition fee is ₹60,000.",
    "data science": "B.Tech CSE - Data Science is offered at VEMU Institute of Technology. The annual tuition fee is ₹60,000.",
    "eee": "B.Tech Electrical and Electronics Engineering (EEE) is offered at VEMU Institute of Technology. The annual tuition fee is ₹60,000.",
    "mechanical": "B.Tech Mechanical Engineering is offered at VEMU Institute of Technology. The annual tuition fee is ₹60,000."
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower().strip()

    # Greetings
    if user_message in ["hi", "hello", "hey"]:
        return jsonify({
            "reply": "Hello! 👋 Welcome to VEMU Institute of Technology. How can I help you?"
        })

    # B.Tech branches
    if (
        "btech branches" in user_message
        or "b.tech branches" in user_message
        or "branches in btech" in user_message
        or "branches in b.tech" in user_message
        or "btech courses" in user_message
        or "b.tech courses" in user_message
    ):
        return jsonify({
            "reply": """🎓 B.Tech branches at VEMU Institute of Technology:

1. Computer Science and Engineering (CSE)
2. Electronics and Communication Engineering (ECE)
3. CSE - Artificial Intelligence and Machine Learning (AI & ML)
4. CSE - Data Science
5. Electrical and Electronics Engineering (EEE)
6. Mechanical Engineering

💰 Annual B.Tech tuition fee: ₹60,000"""
        })

    # B.Tech fee
    if (
        "btech fee" in user_message
        or "btech fees" in user_message
        or "b.tech fee" in user_message
        or "b.tech fees" in user_message
    ):
        return jsonify({
            "reply": "💰 The annual B.Tech tuition fee is ₹60,000."
        })

    # FAQ keyword matching
    for keyword, answer in faq.items():
        if keyword in user_message:
            return jsonify({
                "reply": answer
            })

    # Thank you
    if "thank" in user_message:
        return jsonify({
            "reply": "You're welcome! 😊 Feel free to ask me anything about VEMU Institute of Technology."
        })

    # Unknown question
    return jsonify({
        "reply": "Sorry, I don't have information about that yet. Please ask about admissions, fees, B.Tech branches, courses, hostel, placements, library, location, or contact details."
    })


if __name__ == "__main__":
    app.run(debug=True)
