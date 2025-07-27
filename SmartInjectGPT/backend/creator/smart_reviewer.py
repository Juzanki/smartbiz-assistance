# SmartReviewer — Code Quality & Ethical Validator for SmartCreatorAI Output

import re
from pathlib import Path
from typing import Dict

class SmartReviewer:
    def __init__(self):
        self.quality_keywords = [
            "def ", "class ", "return", "async ", "await", "try:", "except", "@router", "BaseModel"
        ]
        self.risk_signals = [
            "eval(", "exec(", "os.system", "subprocess", "hardcoded secrets", "open(", "write(", "import os"
        ]

    def review_file(self, file_path: str) -> Dict:
        path = Path(file_path)
        if not path.exists():
            return {"file": file_path, "score": 0, "status": "❌ File not found"}

        code = path.read_text()
        lines = code.splitlines()
        score = self._score_quality(code)
        risks = self._detect_risks(code)

        return {
            "file": str(path.name),
            "lines": len(lines),
            "quality_score": round(score * 100),
            "risks_detected": risks,
            "status": "✅ Reviewed"
        }

    def _score_quality(self, code: str) -> float:
        matches = sum(code.count(k) for k in self.quality_keywords)
        lines = code.count("\n") + 1
        return min(1.0, matches / max(lines, 10))

    def _detect_risks(self, code: str):
        return [r for r in self.risk_signals if r in code]

    def summarize_report(self, report: Dict) -> str:
        if report["quality_score"] >= 85 and not report["risks_detected"]:
            return f"✅ {report['file']} is high-quality and clean."
        if report["risks_detected"]:
            return f"⚠️ {report['file']} contains risky logic: {', '.join(report['risks_detected'])}"
        if report["quality_score"] < 50:
            return f"🛠️ {report['file']} may require major refactoring."
        return f"ℹ️ {report['file']} is acceptable, but can be improved."
