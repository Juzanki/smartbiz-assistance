# auto_builder.py — Self-Building AI Feature Constructor

from SmartInjectGPT.creator.feature_parser import FeatureParser
from SmartInjectGPT.creator.component_builder import ComponentBuilder
from SmartInjectGPT.creator.auto_tester import AutoTester
from SmartInjectGPT.creator.smart_reviewer import SmartReviewer
from datetime import datetime
from typing import Dict

class AutoBuilder:
    def __init__(self, api_base_url="http://localhost:8000"):
        self.parser = FeatureParser()
        self.builder = ComponentBuilder()
        self.tester = AutoTester(base_url=api_base_url)
        self.reviewer = SmartReviewer()
        self.build_log = []

    def build_full_feature(self, raw_prompt: str) -> Dict:
        parsed = self.parser.parse_prompt(raw_prompt)
        feature = parsed.get("feature_name")

        # Build all components
        result = self.builder.build_feature(parsed)

        # Run tests if backend exists
        test_results = {}
        if "route" in result["output"]:
            test_results = self.tester.test_fastapi_endpoint(
                f"/{feature.lower().replace(' ', '-')}"
            )

        # Review if route exists
        review_results = {}
        if "route" in result["output"]:
            review_results = self.reviewer.review_file(result["output"]["route"])

        # Save log
        log_entry = {
            "feature": feature,
            "timestamp": datetime.utcnow().isoformat(),
            "outputs": result["output"],
            "test": test_results,
            "review": review_results
        }

        self.build_log.append(log_entry)
        return log_entry

    def get_build_history(self, limit=5):
        return self.build_log[-limit:]
