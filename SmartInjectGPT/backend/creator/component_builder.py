# ComponentBuilder — Generates Backend, UI, and Schema from Feature Plan

from pathlib import Path
from typing import Dict

class ComponentBuilder:
    def __init__(self, output_base="SmartInjectGPT/generated"):
        self.output_base = Path(output_base)
        self.output_base.mkdir(parents=True, exist_ok=True)

    def generate_fastapi_route(self, feature_name: str) -> str:
        route_code = f"""
from fastapi import APIRouter

router = APIRouter(prefix="/{feature_name.lower().replace(' ', '-')}")

@router.get("/")
def get_{feature_name.lower().replace(' ', '_')}():
    return {{"message": "{feature_name} endpoint ready"}}
""".strip()

        file_path = self.output_base / f"{feature_name.lower().replace(' ', '_')}_routes.py"
        file_path.write_text(route_code)
        return str(file_path)

    def generate_vue_component(self, feature_name: str) -> str:
        component_code = f"""
<template>
  <div class="p-4">
    <h1 class="text-xl font-bold">{feature_name}</h1>
    <p>This is the {feature_name} component.</p>
  </div>
</template>

<script setup>
// Logic for {feature_name}
</script>

<style scoped>
</style>
""".strip()

        file_path = self.output_base / f"{feature_name.replace(' ', '')}.vue"
        file_path.write_text(component_code)
        return str(file_path)

    def generate_sqlalchemy_schema(self, feature_name: str) -> str:
        table_name = feature_name.lower().replace(" ", "_")
        schema_code = f"""
from sqlalchemy import Column, Integer, String, DateTime
from backend.db import Base
from datetime import datetime

class {feature_name.replace(' ', '')}(Base):
    __tablename__ = "{table_name}"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
""".strip()

        file_path = self.output_base / f"{table_name}_model.py"
        file_path.write_text(schema_code)
        return str(file_path)

    def build_feature(self, parsed: Dict) -> Dict:
        feature_name = parsed.get("feature_name", "UnnamedFeature")
        paths = {}

        if "api" in parsed["requires"]:
            paths["route"] = self.generate_fastapi_route(feature_name)
        if "ui" in parsed["requires"]:
            paths["vue"] = self.generate_vue_component(feature_name)
        if "schema" in parsed["requires"]:
            paths["schema"] = self.generate_sqlalchemy_schema(feature_name)

        return {
            "feature": feature_name,
            "output": paths
        }
