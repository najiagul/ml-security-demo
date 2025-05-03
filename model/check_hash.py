import hashlib

with open("model.pkl", "rb") as f:
    actual_hash = hashlib.sha256(f.read()).hexdigest()

with open("model.sha256", "r") as f:
    expected_hash = f.read().strip()

if actual_hash != expected_hash:
    print(f"❌ Hash mismatch! Expected: {expected_hash}, Found: {actual_hash}")
    exit(1)
else:
    print(f"✅ Model hash matches: {actual_hash}")
