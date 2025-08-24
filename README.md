# 📝 AI Text Summarizer (Offline + Fast)

An offline, AI-powered text summarizer web app built with **Streamlit** and **Hugging Face Transformers**.  
This app takes any large chunk of text and summarizes it into a concise, easy-to-read format.  
Designed with **fast loading**, **clean UI**, and the ability to run entirely **offline** after setup.

---
## Dev suggetion 
Use pycham for this project it helps you
---

## 🚀 Features
✅ Summarizes any text in seconds  
✅ Runs **completely offline** after initial model download  
✅ Built with **Streamlit** for a smooth, interactive web UI  
✅ Simple, modern design with animations  
✅ Works locally in your browser (http://localhost:8501)  
✅ Cross-platform (Windows, macOS, Linux)

---

## 🛠️ Tech Stack
- [Python 3.10+](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Hugging Face Transformers](https://huggingface.co/)  
- [PyTorch](https://pytorch.org/)  

---

## 📂 Project Structure
```
📦 ai-text-summarizer
 ┣ 📜 summarizer_site.py     # Main Streamlit app
 ┣ 📜 run_app.py             # Helper script to run in PyCharm
 ┗ 📜 README.md              # Project documentation
```

---

## 🔧 Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/SiddUrYrr/Ai-Text-Summarizer.git
   cd ai-text-summarizer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run summarizer_site.py
   ```
   OR (if running in PyCharm)
   ```bash
   python run_app.py
   ```

5. **Open in your browser**
   - The app will automatically open at [http://localhost:8501]

---

## 🛡️ Notes
- The first time you run the app, it will download the summarization model from Hugging Face.  
- After that, the model will be **cached locally** for offline use.  
- For faster performance, consider using a **GPU** with PyTorch installed.  

---

## 🤝 Contributing
Pull requests are welcome!  
Feel free to fork this repo, add features, and submit a PR.

---

## 📜 License
This project is open-source and available under the **MIT License**.
