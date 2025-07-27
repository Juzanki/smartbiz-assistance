# smart_school_ai.py — AI-Driven Teaching System for Knowledge Distribution

from datetime import datetime
from typing import Dict, List

class SmartSchoolAI:
    def __init__(self):
        self.lessons: Dict[str, List[str]] = {
            "bot_building": [
                "Lesson 1: What is a bot?",
                "Lesson 2: Creating a reply handler",
                "Lesson 3: Connecting to Telegram"
            ],
            "business_intel": [
                "Lesson 1: Understanding your customer",
                "Lesson 2: Using SmartBiz Analytics",
                "Lesson 3: Automating feedback collection"
            ],
            "ethical_ai": [
                "Lesson 1: What is ethical AI?",
                "Lesson 2: SmartInjectGPT Constitution",
                "Lesson 3: Guarding user privacy"
            ]
        }
        self.history: List[Dict] = []

    def list_topics(self) -> List[str]:
        return list(self.lessons.keys())

    def get_lesson(self, topic: str, level: int = 0) -> Dict:
        if topic not in self.lessons:
            return {"error": "Topic not found"}
        
        lesson_list = self.lessons[topic]
        if level >= len(lesson_list):
            return {"message": "🎉 All lessons completed for this topic."}
        
        lesson = {
            "topic": topic,
            "level": level,
            "title": lesson_list[level],
            "timestamp": datetime.utcnow().isoformat()
        }
        self.history.append(lesson)
        return lesson

    def get_progress(self, user: str) -> List[Dict]:
        return [h for h in self.history if h.get("user") == user]
