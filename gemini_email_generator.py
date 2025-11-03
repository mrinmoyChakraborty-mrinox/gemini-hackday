import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Use the Gemini Flash model
model = genai.GenerativeModel('models/gemini-2.5-flash')
response = model.generate_content("Explain how AI works in a few words")
print(response.text)