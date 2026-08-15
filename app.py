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
    "courses offered": "We offer B.Tech, MBA, MCA, Diploma, and Degree programs.",
    "fee": "The annual tuition fee is ₹60,000.",
    "placement": "Top recruiters include TCS, Infosys, Wipro, Capgemini, and Accenture."
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower().strip()

    # Find matching FAQ keyword
    for keyword, answer in faq.items():
        if keyword in user_message:
            return jsonify({"reply": answer})

    # Common greetings
    if any(word in user_message for word in ["hi", "hello", "hey"]):
        return jsonify({
            "reply": "Hello! 👋 Welcome to VEMU Institute of Technology. How can I help you?"
        })

    if "thank" in user_message:
        return jsonify({
            "reply": "You're welcome! 😊 Feel free to ask me anything about VEMU Institute of Technology."
        })

    # If no matching question is found
    return jsonify({
        "reply": "Sorry, I don't have information about that. Please ask about admissions, fees, courses, hostel, placements, library, or contact details."
    })


if __name__ == "__main__":
    app.run(debug=True)