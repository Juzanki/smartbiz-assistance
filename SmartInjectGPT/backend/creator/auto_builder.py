# backend/creator/auto_builder.py

import os
from pathlib import Path

class AutoBuilder:
    def __init__(self):
        self.base_dir = Path("backend/creator/generated")
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def generate_code(self, module_name: str) -> Path:
        """
        Auto-generates a module (Python file) given a module name.
        Returns the full path to the generated file.
        """
        filename = f"{module_name}.py"
        file_path = self.base_dir / filename

        if file_path.exists():
            print(f"⚠️ Module {filename} already exists.")
            return file_path

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# Auto-generated module: {module_name}\n\n")
            f.write("def run():\n")
            f.write("    print('✅ Running auto-generated module')\n")

        print(f"✅ Module {filename} created at {file_path}")
        return file_path
