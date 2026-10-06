# 📚 StudySaathi – AI Study Companion

**Horizon Hackathon 2026 | Theme: AI with Education**

StudySaathi is an AI-powered study companion that helps students understand topics faster, revise better, and practice with quizzes — all in simple language (English / Hindi / Hinglish).

---

## 🎯 Problem

Many students struggle to understand complex topics from textbooks or notes. Teachers cannot give individual attention to every student. Existing tools are either too advanced or not student-friendly for Indian learners.

## 💡 Solution

StudySaathi lets any student:
- Paste a topic or notes
- Get a **simple explanation**
- Generate a **short summary**
- Create **flashcards** for revision
- Take a **5-question quiz** with instant feedback

Supports **English, Hindi, and Hinglish**.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📖 Explain Simply | Breaks down any topic into easy language with examples |
| ✂️ Summarize | Creates clear bullet-point summaries |
| 🃏 Flashcards | Generates front/back study cards |
| ❓ Quiz | 5 MCQs with scoring + explanations |
| 🌐 Multilingual | English / Hindi / Hinglish |

---

## 🛠️ Tech Stack

- **Frontend + Backend:** Streamlit (Python)
- **AI Model:** Llama 3.3 70B via Groq API (fast + free tier)
- **Deployment:** Streamlit Community Cloud

---

## 🚀 How to Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/StudySaathi.git
cd StudySaathi
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Groq API Key
- Get a free key from [https://console.groq.com](https://console.groq.com)
- Create a `.env` file:
```
GROQ_API_KEY=your_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

---

## 🌐 Live Demo


> live link: https://studysaathi-krt2jntj2w7pxrbwpprbg9.streamlit.app 

---

## 📸 Screenshots

*(Add screenshots after running the app)*

---

## 🎓 Built For

**Horizon Hackathon 2026** by Hoollow  
Theme: **AI with Education**  
Areas covered: Education • Student Life • Productivity • Accessibility

---

## 🔮 Future Improvements

- PDF / image upload support
- Spaced repetition for flashcards
- Subject-wise progress tracking
- Voice input for doubts
- Mobile app version

---

## 👨‍💻 Author

Built as an individual project for Horizon Hackathon 2026.

---

## 📄 License

MIT License
