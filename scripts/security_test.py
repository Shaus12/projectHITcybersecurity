import joblib
import numpy as np
import pandas as pd

def run_security_test():
    print("--- Security Testing: Adversarial Robustness ---")
    model = joblib.load('models/malware_classifier.pkl')
    feature_names = ['VirtualSize', 'Entropy', 'NumberOfSections', 'Characteristics']
    
    # Baseline Benign Sample (High confidence benign)
    # VirtualSize=50000, Entropy=3.0, Sections=3, Characteristics=200
    benign_sample = pd.DataFrame([[50000, 3.0, 3, 200]], columns=feature_names)
    prediction = int(model.predict(benign_sample)[0])
    proba = model.predict_proba(benign_sample)[0]
    print(f"Original Benign Sample Prediction: {'MALWARE' if prediction == 1 else 'BENIGN'} (Confidence: {proba[prediction]:.2%})")
    
    # Adversarial Manipulation: Gradually increasing features to mimic malware
    print("\nAttempting to mimic malware features on a benign base:")
    for noise_level in [0.5, 1.0, 1.5, 2.0]:
        adv_sample = benign_sample.copy()
        adv_sample.iloc[0, 1] += noise_level * 2  # Increasing Entropy
        adv_sample.iloc[0, 0] += noise_level * 50000 # Increasing VirtualSize
        
        adv_pred = int(model.predict(adv_sample)[0])
        adv_proba = model.predict_proba(adv_sample)[0]
        
        status = "BYPASS (Detected as Malware)" if adv_pred == 1 else "STILL BENIGN"
        print(f"Noise Level {noise_level}: Prediction={'MALWARE' if adv_pred == 1 else 'BENIGN'}, Confidence={adv_proba[adv_pred]:.2%} -> {status}")

if __name__ == "__main__":
    run_security_test()
