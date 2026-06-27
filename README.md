# 🛡️ MalwareGuard: PE Header Classification MVP

> An AI-powered malware classification system that analyzes Portable Executable (PE) headers to identify malicious files.

---

## 📌 Project Overview

MalwareGuard is a cybersecurity prototype designed to demonstrate the application of Machine Learning in identifying malicious executables. Unlike signature-based detection, this system focuses on structural anomalies within the file's PE headers, such as abnormal section sizes, high entropy, and characteristic flags.

This project follows a complete cybersecurity workflow:
1.  **Data Collection:** Synthetic generation of PE header features.
2.  **EDA & Modeling:** Exploratory analysis and training of a Random Forest Classifier.
3.  **Security Testing:** Adversarial robustness evaluation against feature manipulation.
4.  **Prototype (MVP):** A functional Streamlit interface with real-time logging and alerting.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Virtual Environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Shaus12/projectHITcybersecurity.git
   cd projectHITcybersecurity
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the MVP
To launch the Streamlit dashboard:
```bash
streamlit run app.py
```
> On a fresh clone the synthetic dataset and trained model are not committed (see `.gitignore`).
> `app.py` bootstraps them automatically on first launch. To build them manually instead:
> ```bash
> python scripts/generate_data.py   # creates data/pe_malware_dataset.csv
> python scripts/train_model.py     # trains & saves models/malware_classifier.pkl
> ```

### Running Tests
To run the security robustness test:
```bash
python scripts/security_test.py
```

---

## 📊 Methodology

### Feature Selection
The model uses four primary features extracted from PE headers:
- **VirtualSize:** The size of the file when loaded into memory. Malware often has inflated sizes due to packing.
- **Entropy:** A measure of randomness. High entropy often indicates encrypted or compressed payloads (common in malware).
- **NumberOfSections:** The number of sections in the PE file.
- **Characteristics:** Flags describing the file's attributes.

### Model Performance
The Random Forest model achieved **100% accuracy** on the synthetic test set, demonstrating the clear distinction between the generated benign and malicious distributions.

---

## 🚨 Alerting & Auditing
The MVP includes a **Logging & Alerting** module. Every analysis attempt is recorded in `traffic_logs.log`, providing a persistent audit trail for security teams to monitor potential threats.

---

## 🛡️ Security Testing
The system was tested against **Adversarial Noise**. We simulated an attacker attempting to "camouflage" a file by manipulating its features. The `security_test.py` script demonstrates how increasing entropy and virtual size can trigger the malware classifier even on a benign base, highlighting the sensitivity of the model to structural changes.

---

## 🛠️ Architecture
- **Backend:** Python, Scikit-Learn
- **Frontend:** Streamlit
- **Data:** Pandas, NumPy
- **Persistence:** Joblib (Model), CSV (Dataset)

---

## 📦 Submission Deliverables
All academic submission materials live in [`docs/`](docs/):
- **Poster:** [`docs/MalwareGuard_Poster.pptx`](docs/MalwareGuard_Poster.pptx) + [`docs/MalwareGuard_Poster.pdf`](docs/MalwareGuard_Poster.pdf)
- **Project Abstract Form:** [`docs/Project_Abstract_Form.docx`](docs/Project_Abstract_Form.docx) + [`docs/Project_Abstract_Form.pdf`](docs/Project_Abstract_Form.pdf)
- **Poster figures (high-res):** [`docs/figures/`](docs/figures/)
- **Video script / storyboard:** [`docs/Video_Script.md`](docs/Video_Script.md)
