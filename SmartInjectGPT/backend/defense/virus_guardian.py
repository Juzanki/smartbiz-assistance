# VirusGuardian — Payload Detection and AI Infection Filter for SmartInjectGPT

import re
from typing import Dict

class VirusGuardian:
    def __init__(self):
        self.signatures = [
            r"(rm\s+-rf\s+/)",  # Linux wipe
            r"(eval\(.*\))",    # Hidden code execution
            r"(exec\(.*\))",
            r"(base64_decode\()",
            r"(subprocess\.Popen)",
            r"(system\()",
            r"(import\s+os.*system)",
            r"(cryptojack|bitcoin miner)",
            r"(payload injection|malware signature)"
        ]

    def scan(self, code_or_input: str) -> Dict:
        matches = []
        for pattern in self.signatures:
            if re.search(pattern, code_or_input, re.IGNORECASE):
                matches.append(pattern)

        return {
            "infected": bool(matches),
            "matches": matches,
            "summary": f"{len(matches)} threat pattern(s) matched"
        }
