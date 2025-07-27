# dream_memory_log.py — Logs all incoming prompts as prophetic memory

from datetime import datetime

def log_dream(prompt, log_file="dream_logs.txt"):
    now = datetime.utcnow().isoformat()
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {prompt.strip()}\n")
