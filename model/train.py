import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import hashlib
import os

# Path setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "../data/iris.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
HASH_PATH = os.path.join(BASE_DIR, "model.sha256")

# Simulated secret for secret scan
API_KEY = "sk-test-1234567890abcdef"

# Load data
df = pd.read_csv(DATA_PATH)
X = df.drop("target", axis=1)
y = df["target"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

# Save SHA256 hash
with open(MODEL_PATH, "rb") as f:
    hash_val = hashlib.sha256(f.read()).hexdigest()

with open(HASH_PATH, "w") as f:
    f.write(hash_val)

print(f"✅ Model SHA256: {hash_val}")
