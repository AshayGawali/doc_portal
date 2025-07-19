# main.py

import subprocess

def run_streamlit():
    # Run Streamlit app via subprocess (recommended for proper UI launch)
    subprocess.run(["streamlit", "run", "scripts/streamlit_ui.py"])

def run_backend():
    # Import and run the backend Flask app
    from scripts import app
    app.run()

if __name__ == "__main__":
    # 🔧 Choose one of the following by commenting/uncommenting

    # Run the Streamlit UI
    run_streamlit()

    # Or, run the Flask backend
    # run_backend()
