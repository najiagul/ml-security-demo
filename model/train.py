import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Simulate "secret" in code (for scanning demo)
API_KEY = "sk-test-1234567890abcdef"  # <-- This will be caught by gitleaks

df = pd.read_csv("data/iris.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
