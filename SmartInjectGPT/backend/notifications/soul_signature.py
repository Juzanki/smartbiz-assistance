# soul_signature.py — Identity Guardian for SmartInjectGPT

import json

def verify_identity(file_path="backend/identity/soul_signature.json") -> bool:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if (
            data.get("identity") == "SmartInjectGPT" and
            data.get("prophetic_code") == "777-KEY" and
            data.get("sanctified") is True
        ):
            return True

        print("⚠️ AI Identity Integrity Broken.")
        return False

    except Exception as e:
        print("❌ Soul Signature Check Failed:", str(e))
        return False
