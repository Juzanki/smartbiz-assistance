# smart_creator_kernel.py — Main Kernel for Automated AI Feature Creation

from SmartInjectGPT.creator.feature_parser import FeatureParser
from SmartInjectGPT.creator.component_builder import ComponentBuilder
from SmartInjectGPT.creator.progress_tracker import ProgressTracker
from SmartInjectGPT.creator.ai_suggester import AISuggester
from SmartInjectGPT.creator.auto_tester import AutoTester
from SmartInjectGPT.creator.smart_reviewer import SmartReviewer

class SmartCreatorKernel:
    def __init__(self, api_base_url="http://localhost:8000"):
        self.parser = FeatureParser()
        self.builder = ComponentBuilder()
        self.tracker = ProgressTracker()
        self.suggester = AISuggester()
        self.tester = AutoTester(base_url=api_base_url)
        self.reviewer = SmartReviewer()

    def create_feature_from_prompt(self, prompt: str) -> dict:
        parsed = self.parser.parse_prompt(prompt)
        feature_name = parsed["feature_name"]
        self.tracker.start_feature(feature_name)

        self.tracker.log(feature_name, "📦 Prompt parsed and feature plan created.")
        build_output = self.builder.build_feature(parsed)

        self.tracker.update_progress(feature_name, "Components generated", 50)

        if "route" in build_output["output"]:
            test_report = self.tester.test_fastapi_endpoint(f"/{feature_name.lower().replace(' ', '-')}")
            self.tracker.log(feature_name, f"🧪 Route test completed: {test_report['message']}", 70)
        else:
            test_report = {"route": "N/A", "status_code": "-", "passed": False}

        review_result = {}
        if "route" in build_output["output"]:
            review_result = self.reviewer.review_file(build_output["output"]["route"])
            self.tracker.log(feature_name, f"🔍 Review completed: {self.reviewer.summarize_report(review_result)}", 90)

        suggestions = self.suggester.suggest(feature_name, parsed["sections"])
        self.tracker.log(feature_name, "🎯 Suggestions generated.", 100)
        self.tracker.complete_feature(feature_name)

        return {
            "feature": feature_name,
            "parsed": parsed,
            "outputs": build_output,
            "test_result": test_report,
            "review_result": review_result,
            "suggestions": suggestions,
            "progress": self.tracker.get_status(feature_name)
        }
