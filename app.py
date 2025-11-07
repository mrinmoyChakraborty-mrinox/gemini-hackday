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
    prompt = f'''You are an expert email writing assistant named Mail Genie.
Your job is to write a complete, well-formatted email based on the user's purpose.

Guidelines:
- The email must sound {tone.lower()} in tone.
- Begin with an appropriate greeting (e.g., 'Dear Sir/Madam', 'Hi [Name]', etc. depending on tone).
- End with a suitable closing and signature.
- Keep the language natural, polite, and concise.
- Format the response in clear paragraphs with line breaks.
- Do NOT include placeholders like [Name] or [Company] unless absolutely necessary.

Now, write the best possible email for this purpose:
\"\"\"{purpose}\"\"\" '''
    
    response = model.generate_content(prompt)
    return render_template("home.html", title='Email Generator', response_=response.text)

if __name__ == '__main__':
    app.run(debug=True)
