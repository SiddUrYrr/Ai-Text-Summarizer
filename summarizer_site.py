import streamlit as st
from transformers import pipeline
import torch
import time

# -------------------------------
# Load Model (Cached for Speed)
# -------------------------------
@st.cache_resource
def load_summarizer():
    device = 0 if torch.cuda.is_available() else -1  # Use GPU if available
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=device)

summarizer = load_summarizer()

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(
    page_title="AI Summarizer",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for Animations
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to right, #141E30, #243B55);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    h1 {
        text-align: center;
        color: #FFD700;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #FFD700; }
        to { text-shadow: 0 0 20px #FF8C00; }
    }
    textarea, .stTextInput>div>div>input {
        background: #1c1c1c !important;
        color: white !important;
        border-radius: 10px;
    }
    .stButton>button {
        background: #FFD700;
        color: black;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #FF8C00;
        color: white;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🤖 AI Text Summarizer")
st.markdown("### Summarize any text instantly, even offline! 🚀")

# -------------------------------
# Input Fields
# -------------------------------
query = st.text_input("🔍 Focus on (optional):", "")
text = st.text_area("📜 Enter your text here:", height=200)

# -------------------------------
# Summarization Logic
# -------------------------------
if st.button("✨ Summarize"):
    if text.strip():
        with st.spinner("⚡ Summarizing... Please wait..."):
            start_time = time.time()
            short_text = text[:3000]  # Limit input size
            summary = summarizer(short_text, max_length=180, min_length=60, do_sample=False)
            elapsed = time.time() - start_time

        st.success(f"✅ Summary generated in {elapsed:.2f}s")
        st.markdown(f"### 🔹 Summary (focus on **{query or 'main points'}**):")
        st.markdown(f"> {summary[0]['summary_text']}")
    else:
        st.error("⚠️ Please enter some text first.")

st.markdown("---")
st.markdown("💻 *Runs fully offline after the first download.*")