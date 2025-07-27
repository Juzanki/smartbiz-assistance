# AISuggester — Intelligent Improvement Proposals for Feature Plans

from typing import List, Dict

class AISuggester:
    def __init__(self):
        self.suggestion_bank = {
            "Loyalty": ["Add Referral Bonus", "Enable Tier Levels", "Auto Rewards on Milestones"],
            "Feedback": ["Enable Anonymous Mode", "Add Sentiment Analysis", "Show Reaction Heatmap"],
            "Live Chat": ["Auto Reply Suggestions", "Admin Typing Monitor", "Language Translation"],
            "Payments": ["Add Mobile Money Option", "Enable Recurring Billing", "Send Payment Reminders"]
        }

    def suggest(self, feature_name: str, existing_sections: List[str]) -> Dict:
        base = feature_name.lower()
        suggestions = []

        for key, ideas in self.suggestion_bank.items():
            if key.lower() in base:
                for idea in ideas:
                    if all(sec.lower() not in idea.lower() for sec in existing_sections):
                        suggestions.append(idea)

        return {
            "feature": feature_name,
            "suggestions": suggestions[:3] if suggestions else ["No suggestions available."]
        }
