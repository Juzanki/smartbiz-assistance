# FeatureParser — Converts Owner Prompt into Structured Feature Plan

import re
from typing import Dict, List

class FeatureParser:
    def __init__(self):
        self.required_keywords = {
            "schema": ["table", "database", "save", "record", "store"],
            "ui": ["form", "component", "view", "button", "input", "modal"],
            "api": ["route", "endpoint", "submit", "fetch", "update"]
        }

    def parse_prompt(self, text: str) -> Dict:
        # Step 1: Extract feature title
        title_match = re.search(r"(kipengele|feature)\s+cha?\s+(.*?)\s+(ndani|chenye|kiwe|kionyeshe|ambacho|kinacho)?", text, re.IGNORECASE)
        feature_name = title_match.group(2).strip().title() if title_match else "Unnamed Feature"

        # Step 2: Extract sections/components
        sections_match = re.findall(r"[AaBbCcDdEe]\.\s*([^\n,]+)", text)
        sections = [s.strip().title() for s in sections_match] if sections_match else []

        # Step 3: Detect requirements
        requirements = []
        text_lower = text.lower()
        for req, triggers in self.required_keywords.items():
            if any(k in text_lower for k in triggers):
                requirements.append(req)

        if not requirements:
            requirements = ["schema", "ui", "api"]  # default fallback

        return {
            "feature_name": feature_name,
            "sections": sections,
            "requires": requirements,
            "priority": "normal"
        }
