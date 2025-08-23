import subprocess, sys

# Just run Streamlit, let it handle opening the browser
subprocess.run([
    sys.executable, "-m", "streamlit", "run", "summarizer_site.py",
    "--server.headless=false"
])
