import streamlit as st
import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Page Config
st.set_page_config(
    page_title="StudySaathi – AI Study Companion",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A5F;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #5A6A7A;
        margin-bottom: 1.5rem;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3rem;
        font-weight: 600;
    }
    .flashcard {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        min-height: 120px;
    }
    .quiz-question {
        background: #f0f4ff;
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #4F46E5;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/student-center.png", width=80)
    st.title("StudySaathi")
    st.markdown("**AI Study Companion**")
    st.markdown("---")
    
    language = st.selectbox(
        "Language / भाषा",
        ["English", "Hindi (हिंदी)", "Hinglish"]
    )
    
    st.markdown("---")
    st.markdown("### How to use")
    st.markdown("""
    1. Paste any topic or notes
    2. Choose what you need
    3. Click Generate
    4. Learn smarter!
    """)
    st.markdown("---")
    st.caption("Built for Horizon Hackathon 2026")
    st.caption("Theme: AI with Education")

# Header
st.markdown('<p class="main-title">📚 StudySaathi</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Your AI-powered study companion — Explain • Summarize • Flashcards • Quiz</p>', unsafe_allow_html=True)

# API Key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    api_key = st.sidebar.text_input("Enter Groq API Key", type="password", help="Get free key from https://console.groq.com")

if not api_key:
    st.warning("⚠️ Please enter your Groq API Key in the sidebar to continue. Get a free key at [console.groq.com](https://console.groq.com)")
    st.stop()

client = Groq(api_key=api_key)

# Language instruction
lang_map = {
    "English": "Respond only in clear, simple English.",
    "Hindi (हिंदी)": "Respond only in simple Hindi (Devanagari script).",
    "Hinglish": "Respond in natural Hinglish (Hindi + English mix), easy for Indian students."
}
lang_instruction = lang_map[language]

# Input
st.markdown("### 📝 Enter Topic or Notes")
user_input = st.text_area(
    "Paste any topic, paragraph, or your notes here...",
    height=180,
    placeholder="Example: Photosynthesis is the process by which green plants make their own food using sunlight..."
)

# Feature selection
col1, col2, col3, col4 = st.columns(4)
with col1:
    btn_explain = st.button("📖 Explain Simply", use_container_width=True)
with col2:
    btn_summary = st.button("✂️ Summarize", use_container_width=True)
with col3:
    btn_flash = st.button("🃏 Flashcards", use_container_width=True)
with col4:
    btn_quiz = st.button("❓ Generate Quiz", use_container_width=True)

def call_ai(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": f"You are StudySaathi, a friendly and patient AI tutor for school and college students. {lang_instruction} Keep answers clear, structured, and encouraging. Use simple words."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2048
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Explain
if btn_explain:
    if not user_input.strip():
        st.error("Please enter some text first!")
    else:
        with st.spinner("Explaining in simple words..."):
            prompt = f"""Explain the following topic in very simple language that a student can easily understand.
Use short paragraphs, bullet points, and real-life examples where helpful.
Break down difficult terms.

Topic/Notes:
{user_input}"""
            result = call_ai(prompt)
            st.markdown("### 📖 Simple Explanation")
            st.markdown(result)

# Summary
if btn_summary:
    if not user_input.strip():
        st.error("Please enter some text first!")
    else:
        with st.spinner("Creating summary..."):
            prompt = f"""Create a clear and concise summary of the following text.
- Capture all key points
- Use bullet points
- Keep it short but complete (max 150-200 words)

Text:
{user_input}"""
            result = call_ai(prompt)
            st.markdown("### ✂️ Summary")
            st.markdown(result)

# Flashcards
if btn_flash:
    if not user_input.strip():
        st.error("Please enter some text first!")
    else:
        with st.spinner("Generating flashcards..."):
            prompt = f"""Create 5-6 study flashcards from the following text.
Return ONLY a valid JSON array. Each item must have "front" and "back" keys.
Example format:
[
  {{"front": "Question or term", "back": "Answer or definition"}},
  {{"front": "...", "back": "..."}}
]

Text:
{user_input}"""
            result = call_ai(prompt)
            st.markdown("### 🃏 Flashcards")
            try:
                # Clean markdown code blocks if present
                clean = result.strip()
                if clean.startswith("```"):
                    clean = clean.split("```")[1]
                    if clean.startswith("json"):
                        clean = clean[4:]
                cards = json.loads(clean)
                for i, card in enumerate(cards, 1):
                    with st.expander(f"🃏 Card {i}: {card.get('front', '')[:60]}..."):
                        st.markdown(f"**Front:** {card.get('front', '')}")
                        st.markdown(f"**Back:** {card.get('back', '')}")
            except Exception:
                st.markdown(result)

# Quiz
if btn_quiz:
    if not user_input.strip():
        st.error("Please enter some text first!")
    else:
        with st.spinner("Generating quiz..."):
            prompt = f"""Create a quiz of exactly 5 multiple-choice questions based on the following text.
Return ONLY a valid JSON array. Each item must have:
- "question": the question text
- "options": list of 4 options (A, B, C, D)
- "answer": the correct option letter (A/B/C/D)
- "explanation": short explanation of why it is correct

Example:
[
  {{
    "question": "What is ...?",
    "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
    "answer": "B",
    "explanation": "Because ..."
  }}
]

Text:
{user_input}"""
            result = call_ai(prompt)
            st.markdown("### ❓ Quiz Time")
            try:
                clean = result.strip()
                if clean.startswith("```"):
                    clean = clean.split("```")[1]
                    if clean.startswith("json"):
                        clean = clean[4:]
                questions = json.loads(clean)
                
                if "quiz_answers" not in st.session_state:
                    st.session_state.quiz_answers = {}
                if "quiz_submitted" not in st.session_state:
                    st.session_state.quiz_submitted = False
                
                for i, q in enumerate(questions):
                    st.markdown(f'<div class="quiz-question"><b>Q{i+1}. {q["question"]}</b></div>', unsafe_allow_html=True)
                    options = q.get("options", [])
                    selected = st.radio(
                        f"Select answer for Q{i+1}",
                        options,
                        key=f"q_{i}",
                        label_visibility="collapsed"
                    )
                    st.session_state.quiz_answers[i] = {
                        "selected": selected,
                        "correct": q.get("answer", ""),
                        "explanation": q.get("explanation", ""),
                        "options": options
                    }
                
                if st.button("Submit Quiz", type="primary"):
                    st.session_state.quiz_submitted = True
                
                if st.session_state.quiz_submitted:
                    score = 0
                    st.markdown("---")
                    st.markdown("### 📊 Results")
                    for i, data in st.session_state.quiz_answers.items():
                        selected = data["selected"]
                        # Extract letter from selected option
                        selected_letter = selected[0] if selected else ""
                        correct_letter = data["correct"]
                        is_correct = selected_letter.upper() == correct_letter.upper()
                        if is_correct:
                            score += 1
                            st.success(f"Q{i+1}: Correct ✅")
                        else:
                            st.error(f"Q{i+1}: Wrong ❌ — Correct answer: {correct_letter}")
                        st.caption(f"Explanation: {data['explanation']}")
                    st.markdown(f"### Your Score: **{score}/5**")
                    if score == 5:
                        st.balloons()
                        st.success("Perfect score! Excellent work! 🎉")
                    elif score >= 3:
                        st.info("Good job! Keep practicing.")
                    else:
                        st.warning("Review the topic once more. You can do better!")
            except Exception:
                st.markdown(result)

# Footer
st.markdown("---")
st.caption("StudySaathi • Built for Horizon Hackathon 2026 (AI with Education) • Powered by Groq + Llama")
