import streamlit as st
import pandas as pd
import joblib
import numpy as np
import datetime
import os

# Page Config
st.set_page_config(page_title="MalwareGuard MVP", page_icon="🛡️")

# Load model (auto-bootstrap data + model on a fresh clone)
@st.cache_resource
def load_model():
    import subprocess, sys
    model_path = 'models/malware_classifier.pkl'
    if not os.path.exists(model_path):
        if not os.path.exists('data/pe_malware_dataset.csv'):
            subprocess.run([sys.executable, 'scripts/generate_data.py'], check=True)
        subprocess.run([sys.executable, 'scripts/train_model.py'], check=True)
    return joblib.load(model_path)

model = load_model()

# Logging function
def log_prediction(features, prediction):
    log_file = 'traffic_logs.log'
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label = "MALWARE" if prediction == 1 else "BENIGN"
    log_entry = f"[{timestamp}] Features: {features} | Prediction: {label}\n"
    with open(log_file, 'a') as f:
        f.write(log_entry)

st.title("🛡️ MalwareGuard: PE Analysis MVP")
st.markdown("""
This prototype classifies files as **Malware** or **Benign** based on their PE (Portable Executable) header features.
Enter the file characteristics below to run the analysis.
""")

col1, col2 = st.columns(2)

with col1:
    virtual_size = st.number_input("Virtual Size", min_value=0, value=100000)
    entropy = st.slider("Entropy", min_value=0.0, max_value=8.0, value=4.5)

with col2:
    sections = st.number_input("Number of Sections", min_value=1, max_value=20, value=5)
    chars = st.number_input("Characteristics", min_value=0, value=500)

if st.button("Analyze File"):
    feature_names = ['VirtualSize', 'Entropy', 'NumberOfSections', 'Characteristics']
    features = pd.DataFrame([[virtual_size, entropy, sections, chars]], columns=feature_names)
    prediction = int(model.predict(features)[0])
    proba = model.predict_proba(features)[0]
    
    log_prediction(features.iloc[0].tolist(), prediction)
    
    if prediction == 1:
        st.error(f"🚨 **Malware Detected!** (Confidence: {proba[1]:.2%})")
    else:
        st.success(f"✅ **File appears Benign.** (Confidence: {proba[0]:.2%})")
    
    st.info("The event has been logged in `traffic_logs.log` for auditing.")

st.sidebar.header("About")
st.sidebar.info("This is an AI-based defense prototype for detecting malicious executables using structural analysis.")
