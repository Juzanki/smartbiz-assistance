# dream_trigger.py — Converts User Dreams into Feature Modules (via AI Pattern Recognition)

from datetime import datetime
from typing import Dict, List


class DreamTrigger:
    def __init__(self):
        self.logged_dreams: List[Dict] = []

    def receive_dream(self, text: str) -> Dict:
        # Step 1: Classify the theme of the dream
        theme = self._classify_theme(text)

        # Step 2: Extract keywords and goals
        goals = self._extract_goals(text)

        # Step 3: Build module blueprint
        module_name = self._propose_module_name(theme, goals)
        blueprint = {
            "name": module_name,
            "created": datetime.utcnow().isoformat(),
            "theme": theme,
            "keywords": goals,
            "source_dream": text
        }
        self.logged_dreams.append(blueprint)

        return {
            "status": "dream_parsed",
            "blueprint": blueprint
        }

    def _classify_theme(self, text: str) -> str:
        lowered = text.lower()
        if "help" in lowered or "assistant" in lowered:
            return "Assistance"
        elif "protect" in lowered or "danger" in lowered:
            return "Security"
        elif "vision" in lowered or "future" in lowered:
            return "Foresight"
        elif "business" in lowered or "sales" in lowered:
            return "Commerce"
        elif "language" in lowered:
            return "Translation"
        else:
            return "General Purpose"

    def _extract_goals(self, text: str) -> List[str]:
        # Simple goal extractor (can be enhanced later)
        words = text.lower().split()
        return list(set([word for word in words if word in ("assistant", "gifts", "livestream", "coins", "auto", "schedule", "ai", "protect", "video", "scene")]))

    def _propose_module_name(self, theme: str, keywords: List[str]) -> str:
        base = "_".join(keywords[:2]) if keywords else "dream"
        return f"{theme.lower()}_{base}_module"

    def list_logged_dreams(self) -> List[Dict]:
        return self.logged_dreams
