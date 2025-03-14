from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Securely get API Key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  
if not GEMINI_API_KEY:
    raise ValueError("⚠️ ERROR: GEMINI_API_KEY is not set in environment variables!")

genai.configure(api_key=GEMINI_API_KEY)

@app.route("/", methods=["GET"])
def home():
    return "Flask Summarizer API is running!"

@app.route("/summarize", methods=["POST"])
def summarize_text():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(f"Summarize the following text:\n\n{text}")
    
    summary = response.text if response and response.text else "Error generating summary."
    return jsonify({"summary": summary})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render’s assigned port or default to 5000
    app.run(host="0.0.0.0", port=port, debug=True)
