# backend/kernel/smartinject_kernel.py

import sys
import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI

# === Adjust Python path to access modules ===
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# === Load environment early ===
load_dotenv()

# === Core Functionality ===
from backend.prophecy.dream_trigger import DreamTrigger
from backend.prophecy.vision_engine import VisionEngine
from backend.creator.auto_builder import AutoBuilder
from backend.creator.auto_tester import AutoTester
from backend.injectors.shadow_inject import ShadowInjector
from backend.deploy.auto_deployer import AutoDeployer
from backend.defense.auto_patch_engine import AutoPatchEngine
from backend.defense.auto_patch_rollback import PatchRollback
from backend.security.blockchain_logger import BlockchainLogger
from backend.identity.soul_signature import SoulSignature
from backend.core.resurrector import Resurrector

# === Permissions & Auth ===
from backend.auth.permissions import load_permissions
from backend.auth.api_key import verify_admin_key

# === Utilities ===
from backend.utils.rate_limit import check_rate

# === Memory System ===
from backend.memory.confidential_memory import (
    remember,
    audit_memory,
    ConfidentialMemory,
)

# === Security Add-ons ===
from backend.security.integrity_guard import IntegrityGuard
from backend.security.firewall_guardian import FirewallGuardian
from backend.security.threat_watchdog import ThreatWatchdog
from backend.security.divine_signature import DivineSignature

# === Kernel Class ===
class SmartInjectKernel:
    def __init__(self):
        self.identity = "SmartInjectGPT-Kernel"
        self.permissions = load_permissions()
        self.memory = []
        self.activity_log = []

        # Core Components
        self.dream = DreamTrigger()
        self.vision = VisionEngine()
        self.builder = AutoBuilder()
        self.tester = AutoTester()
        self.shadow = ShadowInjector()
        self.deployer = AutoDeployer()
        self.patcher = AutoPatchEngine()
        self.rollback = PatchRollback()
        self.logger = BlockchainLogger()
        self.soul = SoulSignature()
        self.resurrector = Resurrector()

        # Security Components
        self.guard = IntegrityGuard(watch_paths=["backend/", "frontend/", "SmartInjectGPT/", "scripts/"])
        self.firewall = FirewallGuardian(safe_ips=["127.0.0.1", "192.168.1.50"])
        self.watchdog = ThreatWatchdog()
        self.signature = DivineSignature(expected_signature_hash=os.getenv("DIVINE_SIGNATURE_HASH"))
        self.secure_memory = ConfidentialMemory(secret_key=os.getenv("MEMORY_SECRET_KEY"))

        self.guard.log_event("init_kernel", "initialized", "Kernel initialized successfully.")
        logging.info("🧠 Kernel initialized.")

    def observe(self, input_data: str):
        logging.info(f"🧠 Observing: {input_data}")
        self.memory.append(input_data)
        remember(input_data)
        self.guard.log_event("observe", "received", input_data)
        self.firewall.scan(input_data)
        self.watchdog.analyze(input_data)
        self.activity_log.append({"event": "observe", "data": input_data})

    def decide_and_act(self):
        if not self.memory:
            logging.info("ℹ️ No memory data to process.")
            return

        if not check_rate(user="system", action="ai_decision"):
            logging.warning("⛔ Rate limit hit.")
            return

        try:
            result = self.dream.receive_dream(self.memory[-1])
            module_name = result["blueprint"]["name"]
            logging.info(f"💡 Dream interpreted: {module_name}")
            self.guard.log_event("dream_interpreted", "success", module_name)

            code_path = self.builder.generate_code(module_name)
            self.rollback.create_backup(code_path)
            self.shadow.inject_to_sandbox(code_path)

            test_results = self.tester.run_tests_for(module_name)
            self.guard.log_event("test_results", "evaluated", str(test_results))
            logging.info(f"🧪 Tests: {test_results}")

            if all(test_results.values()):
                self.deployer.deploy_feature(code_path, "prod")
                self.logger.append_block("Injected to Production", {"module": module_name})
                self.guard.log_event("deployment", "success", f"{module_name} deployed.")
                self.activity_log.append({"event": "execute", "module": module_name})
            else:
                rollback_path = self.rollback.backup_path / f"{module_name}.bak.py"
                self.rollback.rollback(code_path, rollback_path)
                self.logger.append_block("ROLLBACK", {"module": module_name, "reason": "test failure"})
                self.guard.log_event("deployment", "rollback", f"{module_name} test failed.")
                self.activity_log.append({"event": "rollback", "module": module_name})

            if not self.soul.verify_identity():
                self.guard.log_event("identity_check", "failed", "Soul mismatch.")
                logging.critical("⚠️ Identity compromised.")
                return

            if not self.signature.verify():
                self.guard.log_event("divine_signature", "invalid", "Spiritual verification failed.")
                logging.critical("⚠️ Divine signature mismatch.")
                return

        except Exception as e:
            logging.exception("❌ Kernel exception.")
            self.guard.log_event("error", "exception", str(e))
            self.activity_log.append({"event": "error", "message": str(e)})

    def system_check(self):
        logging.info("🔄 Running system identity checks...")

        if not self.soul.verify_identity():
            self.guard.log_event("identity", "failed", "Soul signature corrupted.")
            self.resurrector.confirm_resurrection()
        else:
            self.guard.log_event("identity", "valid", "Soul verified.")

        if not self.signature.verify():
            self.guard.log_event("divine_check", "failed", "Divine mismatch.")
        else:
            self.guard.log_event("divine_check", "passed", "Divine verified.")

        audit_memory()
        logging.info("📦 Audit snapshot complete.")

# === Global Kernel Instance ===
kernel = SmartInjectKernel()

# === FastAPI Instance ===
app = FastAPI()

# === Routes ===
@app.get("/health")
def health_check():
    return {"status": "ok", "kernel": kernel.identity}

@app.get("/vision/report")
def vision_report():
    return {"status": "success", "report": kernel.vision.report()}

@app.get("/vision/scan")
def vision_scan():
    entries = kernel.vision.scan_sources()
    kernel.vision.analyze_and_store(entries)
    return {"status": "scanned", "new_entries": len(entries)}
