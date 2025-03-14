from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# Set API Key (Replace with your actual Gemini API key)
GEMINI_API_KEY = "AIzaSyAiYwLFrZMoH5p-YCMW2vKe2zhbgrbteSk"
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
    app.run(debug=True)
