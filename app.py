"""
AI Love Compatibility Bot - Flask Application
This app uses Gemini AI to generate fun compatibility reports between two people.
"""

import os
from flask import Flask, render_template, request
from google import genai

# Initialize Flask app
app = Flask(__name__)

# Configure secret key for sessions (using Replit environment variable)
app.secret_key = os.getenv('SESSION_SECRET', 'dev-secret-key-change-in-production')

# Configure Gemini API
# IMPORTANT: The GOOGLE_API_KEY should already be set in Replit's "Secrets" tab
# Get your API key from: https://aistudio.google.com/app/apikey
api_key = os.getenv('GOOGLE_API_KEY')
if api_key:
    client = genai.Client(api_key=api_key)
else:
    client = None
    print("⚠️ WARNING: GOOGLE_API_KEY not found! Please add it in Replit Secrets.")


@app.route('/')
def index():
    """
    Homepage - displays the form where users enter their information
    """
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    """
    Process the form submission and generate compatibility report using Gemini AI
    """
    # Check if API key is configured
    if not client:
        error_message = "Gemini API key is not configured. Please add GOOGLE_API_KEY to your Replit Secrets."
        return render_template('result.html', report=error_message, error=True)
    
    # Get form data from the submitted form
    person1_name = request.form.get('person1_name', 'Person 1')
    person1_age = request.form.get('person1_age', 'Unknown')
    person1_bio = request.form.get('person1_bio', '')
    person1_zodiac = request.form.get('person1_zodiac', 'Unknown')
    
    person2_name = request.form.get('person2_name', 'Person 2')
    person2_age = request.form.get('person2_age', 'Unknown')
    person2_bio = request.form.get('person2_bio', '')
    person2_zodiac = request.form.get('person2_zodiac', 'Unknown')
    
    # Create the prompt for Gemini AI
    prompt = f"""Compare the compatibility between these two people based on their information:

Person 1: {person1_name}, Age: {person1_age}, Bio: {person1_bio}, Zodiac: {person1_zodiac}
Person 2: {person2_name}, Age: {person2_age}, Bio: {person2_bio}, Zodiac: {person2_zodiac}

Make it humorous, romantic, and creative. 

Include:
- A love score out of 100 ❤️
- A zodiac commentary 🔮
- A funny 'Love Aura Name' 💫
- A short poetic summary 💌

Use emojis generously and make it entertaining!"""
    
    try:
        # Send the prompt to Gemini AI and get the response
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        compatibility_report = response.text if response.text else "No response generated"
        
        # Render the result page with the AI-generated report
        return render_template('result.html', 
                             report=compatibility_report,
                             person1=person1_name,
                             person2=person2_name,
                             error=False)
    
    except Exception as e:
        # Handle any errors that occur during API call
        error_message = f"Oops! Something went wrong: {str(e)}"
        return render_template('result.html', report=error_message, error=True)


# Run the Flask app
if __name__ == '__main__':
    # Run on 0.0.0.0:5000 so it's accessible in Replit
    app.run(host='0.0.0.0', port=5000, debug=True)
