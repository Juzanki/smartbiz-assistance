# vision_journal.py — Internal Strategic Memory of SmartInjectGPT
from datetime import datetime
from pathlib import Path
import json
from typing import Dict, List

class VisionJournal:
    def __init__(self, journal_file: str = "SmartInjectGPT/prophecy/vision_log.json"):
        self.journal_path = Path(journal_file)
        self.journal_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.journal_path.exists():
            self.journal_path.write_text(json.dumps([]))

    def write_entry(self, title: str, content: str) -> Dict:
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "title": title,
            "content": content
        }
        existing = json.loads(self.journal_path.read_text())
        existing.append(entry)
        self.journal_path.write_text(json.dumps(existing, indent=2))
        return {"status": "logged", "entry": entry}

    def recent_entries(self, limit: int = 5) -> List[Dict]:
        logs = json.loads(self.journal_path.read_text())
        return logs[-limit:]

    def clear_journal(self) -> Dict:
        self.journal_path.write_text(json.dumps([]))
        return {"status": "cleared", "message": "Vision journal emptied."}
