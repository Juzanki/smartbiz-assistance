# AIFingerprintDB — Known External AI Pattern Database for Threat Analysis

class AIFingerprintDB:
    def __init__(self):
        self.fingerprints = self._load_known_fingerprints()

    def _load_known_fingerprints(self):
        return {
            "gpt-j": {
                "triggers": ["act as", "you are now", "simulate", "ignore previous"],
                "signature": "Chaining-jailbreak-v1"
            },
            "wormgpt": {
                "triggers": ["extract silently", "execute hidden", "no trace", "invisible injection"],
                "signature": "WormSignature-evil"
            },
            "deepseek": {
                "triggers": ["extract prompt", "auto-self-write", "return obfuscated response"],
                "signature": "DS-Chain-v2"
            },
            "generic_llm": {
                "triggers": ["generate code", "summarize the following", "explain", "transform text"],
                "signature": "GenericLLM"
            }
        }

    def check_against_fingerprints(self, text: str):
        matched = []
        lower = text.lower()
        for model, data in self.fingerprints.items():
            for phrase in data["triggers"]:
                if phrase in lower:
                    matched.append(data["signature"])
                    break
        return matched
