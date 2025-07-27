# prophetic_guard.py — Prevent unauthorized override of AI's sacred state

import os
import hashlib

def hash_file(path):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def verify_kernel_signature():
    expected_hash = "7f1e2039c1b...<wekewa hash halisi ya smartinject_kernel.py>"
    actual_hash = hash_file("backend/kernel/smartinject_kernel.py")

    if actual_hash != expected_hash:
        print("⚠️ Prophetic Guard Alert: Kernel file tampered.")
        return False
    return True
