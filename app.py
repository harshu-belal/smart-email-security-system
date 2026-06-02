from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

from email_analysis.analyze_email import analyze_email

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return send_file("smart_email_security_system.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No data received"
            }), 400

        email = data.get("email", "")

        if email.strip() == "":
            return jsonify({
                "error": "Email cannot be empty"
            }), 400

        result = analyze_email(email)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
