# backend/memory/confidential_memory.py

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict, Union
from cryptography.fernet import Fernet

# === Simple In-Memory Store ===
memory_store: List[str] = []

def remember(data: str) -> None:
    """
    Store temporary memory used by SmartInjectGPT kernel.
    """
    memory_store.append(data)
    logging.info(f"[MEMORY] 🧠 Remembered: {data}")

def audit_memory() -> List[str]:
    """
    Audit all temporary memory data for review or debugging.
    """
    logging.info(f"[MEMORY] 📋 Auditing memory store — {len(memory_store)} entries.")
    return memory_store

# === Secure Encrypted Vault for Persistent Memory ===
class ConfidentialMemory:
    def __init__(self, secret_key: str, storage_file="SmartInjectGPT/secure/confidential_data.json.enc"):
        self.cipher = Fernet(secret_key)
        self.storage_path = Path(storage_file)
        self.data: List[Dict[str, Union[str, datetime]]] = []
        self._load()

    def _load(self) -> None:
        if self.storage_path.exists():
            try:
                encrypted = self.storage_path.read_bytes()
                decrypted = self.cipher.decrypt(encrypted)
                self.data = json.loads(decrypted.decode("utf-8"))
                logging.info(f"[CONFIDENTIAL] 🔐 Loaded {len(self.data)} secure records.")
            except Exception as e:
                logging.warning(f"[CONFIDENTIAL] ⚠️ Decryption failed: {e}")
                self.data = []
        else:
            self.data = []

    def _save(self) -> None:
        try:
            encrypted = self.cipher.encrypt(json.dumps(self.data, indent=2).encode("utf-8"))
            self.storage_path.parent.mkdir(parents=True, exist_ok=True)
            self.storage_path.write_bytes(encrypted)
            logging.info("[CONFIDENTIAL] ✅ Memory encrypted and saved.")
        except Exception as e:
            logging.error(f"[CONFIDENTIAL] ❌ Failed to save: {e}")

    def store_secret(self, label: str, content: str, level: str = "private") -> dict:
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "label": label,
            "level": level,
            "content": content
        }
        self.data.append(entry)
        self._save()
        logging.info(f"[CONFIDENTIAL] 🔒 Stored: {label}")
        return entry

    def retrieve_by_label(self, label: str) -> Optional[dict]:
        for item in reversed(self.data):
            if item["label"] == label:
                logging.info(f"[CONFIDENTIAL] 🔍 Retrieved: {label}")
                return item
        logging.warning(f"[CONFIDENTIAL] ❌ Not found: {label}")
        return None

    def clear_all(self) -> None:
        self.data = []
        self._save()
        logging.warning("[CONFIDENTIAL] ⚠️ All secrets cleared.")

    def list_secrets(self) -> List[Dict[str, str]]:
        return [{"label": d["label"], "timestamp": d["timestamp"], "level": d["level"]} for d in self.data]
