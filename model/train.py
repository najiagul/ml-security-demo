import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import hashlib


# Simulate "secret" in code (for scanning demo)
API_KEY = "sk-test-1234567890abcdef"  # <-- This will be caught by gitleaks

df = pd.read_csv("data/iris.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Compute and save hash
with open("model.pkl", "rb") as f:
    hash_val = hashlib.sha256(f.read()).hexdigest()

with open("model.sha256", "w") as f:
    f.write(hash_val)

print(f"Model SHA256: {hash_val}")