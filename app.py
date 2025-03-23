import os
from flask import Flask, render_template, request, jsonify
from together import Together
from dotenv import load_dotenv

# Load API key dari .env
load_dotenv()
API_KEY = os.getenv("TOGETHER_API_KEY")

# Pastikan API Key tidak kosong
if not API_KEY:
    raise ValueError("API Key tidak ditemukan! Pastikan sudah diatur di .env")

# Inisialisasi Flask dan Together AI
app = Flask(__name__)
client = Together(api_key=API_KEY)

# Route untuk halaman utama
@app.route("/")
def home():
    return render_template("index.html")

# Route untuk menangani input dari pengguna
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    return jsonify({"response": response.choices[0].message.content})

# Jalankan Flask
if __name__ == "__main__":
    app.run(debug=True)
