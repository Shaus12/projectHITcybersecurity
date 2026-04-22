import pandas as pd
import numpy as np
import os

def generate_pe_dataset(n_samples=1000, output_path='data/pe_malware_dataset.csv'):
    np.random.seed(42)
    
    # Feature 1: VirtualSize (Generally larger for malware)
    virtual_size_benign = np.random.normal(50000, 15000, n_samples // 2)
    virtual_size_malware = np.random.normal(150000, 40000, n_samples // 2)
    
    # Feature 2: Entropy (Generally higher for malware)
    entropy_benign = np.random.uniform(2.0, 5.0, n_samples // 2)
    entropy_malware = np.random.uniform(5.5, 7.9, n_samples // 2)
    
    # Feature 3: NumberOfSections
    sections_benign = np.random.randint(2, 6, n_samples // 2)
    sections_malware = np.random.randint(4, 10, n_samples // 2)
    
    # Feature 4: Characteristics
    chars_benign = np.random.randint(100, 500, n_samples // 2)
    chars_malware = np.random.randint(400, 900, n_samples // 2)
    
    # Combine
    data = {
        'VirtualSize': np.concatenate([virtual_size_benign, virtual_size_malware]),
        'Entropy': np.concatenate([entropy_benign, entropy_malware]),
        'NumberOfSections': np.concatenate([sections_benign, sections_malware]),
        'Characteristics': np.concatenate([chars_benign, chars_malware]),
        'Label': np.concatenate([np.zeros(n_samples // 2), np.ones(n_samples // 2)])
    }
    
    df = pd.DataFrame(data)
    # Shuffle
    df = df.sample(frac=1).reset_index(drop=True)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dataset generated with {n_samples} samples at {output_path}")

if __name__ == "__main__":
    generate_pe_dataset()
