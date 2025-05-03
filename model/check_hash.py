import hashlib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
HASH_PATH = os.path.join(BASE_DIR, "model.sha256")

with open(MODEL_PATH, "rb") as f:
    actual_hash = hashlib.sha256(f.read()).hexdigest()

with open(HASH_PATH, "r") as f:
    expected_hash = f.read().strip()

if actual_hash != expected_hash:
    print(f"❌ Hash mismatch! Expected: {expected_hash}, Found: {actual_hash}")
    exit(1)
else:
    print(f"✅ Model hash matches: {actual_hash}")
