# MindSpace - Mental Health Web App

**Hackathon Submission:** Techs Sparking Challenge 

MindSpace is a volunteer initiative designed to address mental health challenges faced by teens and young adults. It provides an interactive web platform to help users express their emotions, engage in self-care, and access motivational content.

---

## Problem Statement

Many teens and young adults face depression and anxiety but have no accessible way to express their emotions or seek guidance. Loneliness and lack of emotional support can lead to severe mental health issues, including risk of suicide.  

**Statistics:**  
- According to WHO, ~10-20% of adolescents experience mental health conditions globally.  
- Studies show that simply talking about emotions and practicing self-care can reduce symptoms of anxiety and depression by 30-40%.

---

## Proposed Solution

MindSpace provides:

1. **AI-Powered Chatbot:** Converses with users based on their current mood.  
2. **Self-Care Checklist:** Users track self-care activities; progress is visualized with animated progress bars and confetti for encouragement.  
3. **Interactive Exercises:** Engage in psychology-based exercises to improve emotional intelligence and resilience.  
4. **Motivational Quotes:** Infinite AI-generated quotes to inspire and uplift users.


---

## Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML, CSS, JavaScript  
- **AI:** OpenAI API (GPT-4o-mini for chatbot, text-davinci-003 for quotes)  

---

## Flowchart (Backend Workflow)

1. User selects mood → `moodtracker.html`  
2. Mood sent to Flask backend → AI Chatbot response generated → displayed in `chat.html`  
3. User completes self-care activities → progress bar updates → confetti animation triggers  
4. Motivational quotes fetched dynamically from OpenAI API → displayed in `quotes.html`

---

## Contributing

This is a volunteer project to raise **mental health awareness** and provide emotional support. Contributions are welcome.

---

## Deployment

1. Clone this repository  
2. Install requirements: `pip install -r requirements.txt`  
3. Set your OpenAI API key in `app.py`  
4. Run locally: `python app.py`  
5. Deploy on Render or Replit to get a live URL for public access.

---

## License

MIT License
