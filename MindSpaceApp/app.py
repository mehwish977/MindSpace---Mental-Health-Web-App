from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os
from dotenv import load_dotenv
import openai

# -------------------- Load environment variables --------------------
load_dotenv()  # loads variables from .env

# -------------------- Flask App --------------------
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # Must be set in .env

# -------------------- OpenAI Setup --------------------
openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

# -------------------- Routes --------------------
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/moodtracker', methods=['GET', 'POST'])
def moodtracker():
    if request.method == 'POST':
        selected_emotion = request.form.get('emotion')
        session['current_mood'] = selected_emotion
        return redirect(url_for('chat', mood=selected_emotion))
    return render_template('moodtracker.html')

@app.route('/chat/<mood>', methods=['GET', 'POST'])
def chat(mood):
    user_message = None
    bot_response = None

    if request.method == 'POST':
        user_message = request.form.get('message')
        bot_response = get_chat_response(user_message, mood)

    return render_template('chat.html', mood=mood, user_message=user_message, bot_response=bot_response)

@app.route('/selfcare')
def selfcare():
    return render_template('selfcare.html')

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')

# -------------------- AI Functions --------------------
def get_chat_response(user_message, mood):
    system_prompt = f"""
    You are a {mood} chatbot for MindSpace App. 
    Only talk about this emotion. If the user talks about a different emotion, 
    politely ask them to select the correct emotion from Mood Tracker.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    
    return response.choices[0].message.content

@app.route('/get_quote')
def get_quote():
    prompt = "Give me a single inspiring motivational quote in one sentence."
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an inspiring quotes generator."},
                {"role": "user", "content": prompt}
            ]
        )
        quote = response.choices[0].message.content.strip()
        return jsonify({"quote": quote})
    except Exception as e:
        print("Quote API error:", e)
        return jsonify({"quote": "Failed to load quote."})

# -------------------- Run App --------------------
if __name__ == "__main__":
    app.run(debug=True)
