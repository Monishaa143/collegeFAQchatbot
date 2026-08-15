from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

faq = {
    "admission": """Admissions start every June.
Please visit the college admission office for details.""",

    "btech courses": """VEMU Institute of Technology offers the following B.Tech branches:

1. Computer Science and Engineering (CSE)
2. Electronics and Communication Engineering (ECE)
3. CSE (Artificial Intelligence & Machine Learning)
4. CSE (Data Science)
5. Electrical and Electronics Engineering (EEE)
6. Mechanical Engineering
7. Civil Engineering""",

    "branches": """B.Tech branches available:

1. CSE
2. ECE
3. CSE (AI & ML)
4. CSE (Data Science)
5. EEE
6. Mechanical Engineering
7. Civil Engineering""",

    "fees": """B.Tech course fees:

CSE – ₹1,50,000 per year
ECE – ₹80,000 per year
CSE (AI & ML) – ₹1,20,000 per year
CSE (Data Science) – ₹1,60,000 per year
EEE – ₹75,000 per year
Mechanical – ₹50,000 per year
Civil – ₹50,000 per year

Hostel Fees – ₹30,000 per year""",

    "course fees": """B.Tech course fees:

CSE – ₹1,50,000 per year
ECE – ₹80,000 per year
CSE (AI & ML) – ₹1,20,000 per year
CSE (Data Science) – ₹1,60,000 per year
EEE – ₹75,000 per year
Mechanical – ₹50,000 per year
Civil – ₹50,000 per year

Hostel Fees – ₹30,000 per year""",

    "hostel": """Hostel facilities are available for boys and girls.

Hostel Fees – ₹30,000 per year""",

    "placement": """Top recruiters include:

1. TCS
2. Infosys
3. Wipro
4. Capgemini
5. Accenture""",

    "library": """Library timings:

Opening Time – 9:00 AM
Closing Time – 6:00 PM""",

    "contact": """College Contact Details:

Phone: +91-6281914053
Phone: 9381231981""",

    "college": """VEMU Institute of Technology

Location:
P. Kothakota,
Chittoor,
Andhra Pradesh.""",

    "location": """VEMU Institute of Technology is located at:

P. Kothakota,
Chittoor,
Andhra Pradesh."""
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"].lower().strip()

    # B.Tech courses
    if any(word in user_message for word in [
        "btech courses",
        "b tech courses",
        "b.tech courses",
        "btech branches",
        "b tech branches",
        "branches",
        "engineering branches"
    ]):
        return jsonify({"reply": faq["btech courses"]})

    # Course fees
    if any(word in user_message for word in [
        "fees",
        "fee",
        "course fees",
        "btech fees",
        "b tech fees",
        "branch fees"
    ]):
        return jsonify({"reply": faq["fees"]})

    # Hostel
    if "hostel" in user_message:
        return jsonify({"reply": faq["hostel"]})

    # Placement
    if any(word in user_message for word in [
        "placement",
        "placements",
        "recruiters",
        "companies"
    ]):
        return jsonify({"reply": faq["placement"]})

    # Library
    if "library" in user_message:
        return jsonify({"reply": faq["library"]})

    # Admission
    if any(word in user_message for word in [
        "admission",
        "admissions",
        "join",
        "joining"
    ]):
        return jsonify({"reply": faq["admission"]})

    # Contact
    if any(word in user_message for word in [
        "contact",
        "phone",
        "mobile",
        "number"
    ]):
        return jsonify({"reply": faq["contact"]})

    # Location
    if any(word in user_message for word in [
        "location",
        "where",
        "address",
        "college location"
    ]):
        return jsonify({"reply": faq["location"]})

    # Greetings
    if any(word in user_message.split() for word in [
        "hi",
        "hello",
        "hey"
    ]):
        return jsonify({
            "reply": """Hello! 👋

Welcome to VEMU Institute of Technology.

You can ask me about:

📘 Admissions
🎓 B.Tech branches
💰 Course fees
🏠 Hostel fees
💼 Placements
📚 Library
📞 Contact details
📍 College location"""
        })

    # Thanks
    if "thank" in user_message:
        return jsonify({
            "reply": """You're welcome! 😊

Feel free to ask me anything about
VEMU Institute of Technology."""
        })

    # Unknown question
    return jsonify({
        "reply": """Sorry, I don't have information about that. 😔

You can ask me about:

🎓 B.Tech branches
💰 Course fees
🏠 Hostel
📘 Admissions
💼 Placements
📚 Library
📞 Contact details
📍 College location"""
    })


if __name__ == "__main__":
    app.run(debug=True)
