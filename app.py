from flask import Flask, render_template, request
import os
import google.generativeai as genai
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

@app.route('/')
def home():
    return render_template('home.html', title='Email Generator')

@app.route('/generate', methods=['POST'])
def generate_email():
    purpose = request.form.get('purpose')
    tone = request.form.get('tone')

    # Use the Gemini model
    model = genai.GenerativeModel('gemini-2.5-flash')
    prompt = f"Write a {tone.lower()} email for the following purpose: {purpose}"
    
    response = model.generate_content(prompt)
    return render_template("home.html", title='Email Generator', response_=response.text)

if __name__ == '__main__':
    app.run(debug=True)