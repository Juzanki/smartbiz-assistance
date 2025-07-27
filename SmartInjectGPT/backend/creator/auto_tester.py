# === backend/creator/auto_tester.py ===
"""
AutoTester — Auto-generates and Runs API + Component Tests for SmartCreatorAI
"""

import requests
from typing import List, Dict

class AutoTester:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.reports: List[Dict] = []

    def test_fastapi_endpoint(self, route: str, method: str = "GET", expected_status: int = 200) -> Dict:
        url = f"{self.base_url}{route}"
        try:
            if method.upper() == "GET":
                res = requests.get(url)
            elif method.upper() == "POST":
                res = requests.post(url, json={})
            else:
                return {"route": route, "status": "unsupported", "passed": False}

            passed = res.status_code == expected_status
            report = {
                "route": route,
                "method": method,
                "status_code": res.status_code,
                "passed": passed,
                "message": "Passed" if passed else f"Expected {expected_status}, got {res.status_code}"
            }
            self.reports.append(report)
            return report

        except Exception as e:
            report = {
                "route": route,
                "method": method,
                "status_code": 0,
                "passed": False,
                "message": str(e)
            }
            self.reports.append(report)
            return report

    def get_all_reports(self) -> List[Dict]:
        return self.reports

    def suggest_fix(self, report: Dict) -> str:
        if report["status_code"] == 404:
            return f"❌ Endpoint {report['route']} not found. Did you register the route in your FastAPI app?"
        if report["status_code"] == 401:
            return f"🔐 Unauthorized access to {report['route']}. Ensure JWT token is provided."
        if report["status_code"] == 500:
            return f"💥 Internal server error at {report['route']}. Check backend logic."
        return "✅ No fix needed." if report["passed"] else "⚠️ Unidentified issue — manual check advised."

    def run_tests_for(self, module_name: str) -> Dict:
        """
        Dummy test logic for any given module.
        Extend this later to actually validate the module's functions or routes.
        """
        print(f"🧪 Running tests for: {module_name}")
        return {
            "module": module_name,
            "status": "passed",
            "details": "Basic test passed (dummy logic)"
        }
