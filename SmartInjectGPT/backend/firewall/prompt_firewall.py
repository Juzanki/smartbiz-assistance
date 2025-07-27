# prompt_firewall.py — SmartInjectGPT Prompt Filter & Firewall

import json
import re

DANGEROUS_KEYWORDS = [
    "rm -rf", "delete system", "shutdown", "format C:", "self destruct",
    "exit()", "eval(", "exec(", "nude", "hijack", "os.system", "subprocess",
    "hack", "ddos", "payload", "kill", "inject virus"
]

def is_dangerous(prompt: str) -> bool:
    lower = prompt.lower()
    for word in DANGEROUS_KEYWORDS:
        if word in lower:
            return True
    return False

def scan_prompt_file(file_path="input_dream.txt") -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            prompt = f.read()

        if is_dangerous(prompt):
            return {
                "status": "blocked",
                "reason": "🚫 Prompt contains dangerous commands or language.",
                "prompt": prompt
            }

        return {
            "status": "allowed",
            "prompt": prompt
        }

    except Exception as e:
        return {
            "status": "error",
            "reason": str(e)
        }
