<p align="center">
  <img src="static/images/mail_genie_logo.png" alt="Mail Genie Logo" width="120"/>
</p>
# 📧 MailGenie - Smart Email Writer (Flask Version)

MailGenie is a beginner-friendly web app built with Flask and Google’s Gemini API.
It helps users instantly generate professional, friendly, or academic emails by describing the purpose and tone — perfect for students, professionals, and beginners exploring AI-powered text generation.

---

## ✨ Features

- 🪄 Generate emails based on user input (e.g., apology, job application, inquiry)
- 🎭 Choose tone: Formal, Friendly, Apology, or Academic
- 🌐 Clean Flask web interface for easy use
- ⚙️ Powered by Gemini API for human-like, polished writing
- 🧠 Beginner-friendly and easy to extend

---

## 🚀 How to Run

1️⃣ Clone the repository

git clone https://github.com/yourusername/mailgenie.git
cd mailgenie

2️⃣ Create a virtual environment (recommended)

python -m venv venv
source venv/bin/activate  # for Linux/macOS
venv\Scripts\activate     # for Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Get your Gemini API key

Visit "https://aistudio.google.com/app/apikey" (https://aistudio.google.com/app/apikey)
and copy your API key.

5️⃣ Run the Flask server

python app.py

6️⃣ Open in browser

Go to 👉 "http://127.0.0.1:5000" (http://127.0.0.1:5000)

---

## 🧠 Concepts Learned

- Integrating Gemini API with Flask
- Creating a web interface using HTML + CSS + Flask templates
- Handling user input and displaying AI-generated responses
- Using environment variables to store API keys securely

---

## 📸 Example Workflow

1. Enter the purpose of your email (e.g., “Apology for missing deadline”).
2. Select a tone (Formal / Friendly / Apology / Academic).
3. Click Generate Email.
4. Instantly see your AI-written email with subject and body ready to copy.

---

## 🎨 Future Enhancements

- 🕶️ Add Dark Mode toggle
- 📋 Add “Copy Email” button
- 📂 Save generated emails to database
- 📧 Gmail API integration to send emails directly
- 🗣️ Add speech-to-text for hands-free generation

---

## 🧩 Hacktoberfest 2025 (If Applicable)

- [ ] This PR is for Hacktoberfest 2025
- [ ] My code follows the repository’s guidelines
- [ ] I have commented and formatted the code
- [ ] I have tested the app locally and it works correctly

---

## 🤝 Contributing

Contributions are welcome!
You can help by improving:

- UI design or styling
- Prompt quality and tone options
- API key security handling
- Adding a Flask blueprint for modular structure
