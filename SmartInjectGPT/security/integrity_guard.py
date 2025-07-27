# backend/security/integrity_guard.py
import os
from dotenv import load_dotenv

load_dotenv()  # Hii isomwe kabla ya kuitwa mahali popote
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class IntegrityGuard:
    def __init__(self, silent: bool = False):
        log_path = os.getenv("INTEGRITY_LOG_PATH")
        if not log_path:
            raise ValueError("INTEGRITY_LOG_PATH not set in .env")
        self._log_file = Path(log_path)
        self.silent = silent
        if not self.silent:
            print("🛡 Using log file path:", self._log_file)
        self._init_log()

    def _init_log(self):
        try:
            self._log_file.parent.mkdir(parents=True, exist_ok=True)
            if not self._log_file.exists():
                self._log_file.write_text(json.dumps([], indent=2), encoding="utf-8")
                self.log_event("init_guard", "initialized", "IntegrityGuard system started successfully.")
        except Exception as e:
            self._print_error(f"Failed during _init_log: {e}")

    def log_event(self, event: str, status: str, details: str = "", file: str = "", ip: str = ""):
        try:
            try:
                logs = json.loads(self._log_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, FileNotFoundError):
                logs = []

            logs.append({
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "event": event,
                "status": status,
                "details": details,
                "file": file,
                "ip": ip
            })

            self._log_file.write_text(json.dumps(logs, indent=2), encoding="utf-8")
            if not self.silent:
                print(f"✅ Logged: {event} → {status}")
        except Exception as e:
            self._print_error(f"Failed to write log: {e}")

    def _print_error(self, msg):
        if not self.silent:
            print(f"[IntegrityGuard ERROR] {msg}")
