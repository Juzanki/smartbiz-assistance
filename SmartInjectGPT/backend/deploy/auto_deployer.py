# auto_deployer.py — Automatically Deploys Features to Target Environments

import os
from datetime import datetime
from typing import List, Dict


class AutoDeployer:
    def __init__(self):
        self.deploy_log: List[Dict] = []
        self.environments = {
            "dev": "./dev_env/",
            "test": "./test_env/",
            "prod": "./production_env/"
        }

    def deploy_feature(self, feature_path: str, environment: str = "dev") -> Dict:
        if environment not in self.environments:
            return {"status": "error", "message": f"Unknown environment: {environment}"}

        try:
            destination = self.environments[environment]
            filename = os.path.basename(feature_path)

            if not os.path.exists(destination):
                os.makedirs(destination)

            os.system(f"copy {feature_path} {destination}{filename}")

            log_entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "feature": filename,
                "env": environment,
                "path": feature_path
            }
            self.deploy_log.append(log_entry)

            return {
                "status": "✅ Deployed",
                "details": log_entry
            }
        except Exception as e:
            return {
                "status": "❌ Failed",
                "error": str(e)
            }

    def get_deploy_history(self, limit: int = 5) -> List[Dict]:
        return self.deploy_log[-limit:]

    def list_environments(self) -> List[str]:
        return list(self.environments.keys())
