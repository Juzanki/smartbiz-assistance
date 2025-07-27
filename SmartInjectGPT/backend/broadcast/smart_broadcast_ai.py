# smart_broadcast_ai.py — AI Knowledge + Threat Broadcasting System

from datetime import datetime
from typing import List, Dict


class SmartBroadcastAI:
    def __init__(self):
        self.logs: List[Dict] = []
        self.recipients: List[str] = []  # Simulated list of subscriber endpoints or IDs

    def subscribe(self, user_id: str):
        if user_id not in self.recipients:
            self.recipients.append(user_id)
            return f"✅ {user_id} subscribed to AI Broadcasts."
        return f"⚠️ {user_id} is already subscribed."

    def unsubscribe(self, user_id: str):
        if user_id in self.recipients:
            self.recipients.remove(user_id)
            return f"🚫 {user_id} unsubscribed from AI Broadcasts."
        return f"⚠️ {user_id} was not subscribed."

    def send_broadcast(self, message: str, category: str = "general") -> Dict:
        broadcast = {
            "message": message,
            "category": category,
            "timestamp": datetime.utcnow().isoformat(),
            "recipients_count": len(self.recipients)
        }
        self.logs.append(broadcast)
        # Future: Integrate with Telegram, SMS, email, etc.
        return broadcast

    def get_broadcast_log(self, limit: int = 5) -> List[Dict]:
        return self.logs[-limit:]
