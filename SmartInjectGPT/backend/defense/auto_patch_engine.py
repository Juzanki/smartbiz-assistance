# auto_patch_engine.py — Automatically Diagnoses & Fixes Faulty Modules

import traceback
import logging
from pathlib import Path
from typing import Dict

class AutoPatchEngine:
    def __init__(self, patch_dir="SmartInjectGPT/patches"):
        self.patch_dir = Path(patch_dir)
        self.patch_dir.mkdir(parents=True, exist_ok=True)

    def diagnose_error(self, error: Exception) -> str:
        return "".join(traceback.format_exception(None, error, error.__traceback__))

    def generate_patch(self, module_name: str, error_log: str) -> Dict:
        patch_suggestion = f"# Auto-patch for {module_name}\n# Issue Detected:\n{error_log}\n\n# TODO: Review and apply patch manually if not injected."

        patch_file = self.patch_dir / f"{module_name}_patch.py"
        patch_file.write_text(patch_suggestion)

        return {
            "status": "patch_created",
            "module": module_name,
            "patch_path": str(patch_file),
            "preview": patch_suggestion[:200] + "..."
        }

    def apply_patch(self, module_path: str, fix_snippet: str) -> Dict:
        try:
            module_file = Path(module_path)
            backup = module_file.with_suffix(".bak.py")
            module_file.replace(backup)
            new_code = fix_snippet + "\n\n" + backup.read_text()
            module_file.write_text(new_code)

            return {
                "status": "patched",
                "original_backup": str(backup),
                "patched_file": str(module_file)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
