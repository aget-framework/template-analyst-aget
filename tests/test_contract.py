#!/usr/bin/env python3
"""
Contract Tests for template-analyst-aget

Validates template compliance with AGET_TEMPLATE_SPEC v3.0.
"""

import json
import os
import pytest
from pathlib import Path


# Test utilities
def get_template_root():
    """Get the template root directory."""
    return Path(__file__).parent.parent


def is_template():
    """Check if this is a template (not an instantiated agent)."""
    version_path = get_template_root() / ".aget" / "version.json"
    if version_path.exists():
        with open(version_path) as f:
            data = json.load(f)
            return data.get("instance_type") == "template"
    return True


# ============================================================
# Template Structure Tests (Always Run)
# ============================================================

class TestTemplateStructure:
    """Tests for template directory structure."""

    def test_manifest_exists(self):
        """Template must have manifest.yaml."""
        manifest = get_template_root() / "manifest.yaml"
        assert manifest.exists(), "manifest.yaml is required"

    def test_governance_files(self):
        """Template must have governance files."""
        root = get_template_root()
        assert (root / "governance" / "CHARTER.md").exists()
        assert (root / "governance" / "MISSION.md").exists()
        assert (root / "governance" / "SCOPE_BOUNDARIES.md").exists()

    def test_5d_directories(self):
        """Template must have 5D directories."""
        aget = get_template_root() / ".aget"
        for dim in ["persona", "memory", "reasoning", "skills", "context"]:
            assert (aget / dim).is_dir(), f".aget/{dim}/ directory required"

    def test_identity_file(self):
        """Template must have identity.json."""
        identity = get_template_root() / ".aget" / "identity.json"
        assert identity.exists(), ".aget/identity.json is required"

    def test_version_file(self):
        """Template must have version.json."""
        version = get_template_root() / ".aget" / "version.json"
        assert version.exists(), ".aget/version.json is required"


# ============================================================
# Instance-Only Tests (Skip for Templates)
# ============================================================

@pytest.mark.skipif(is_template(), reason="Template, not instance")
class TestInstanceConfiguration:
    """Tests that only apply to instantiated agents."""

    def test_persona_configured(self):
        """Instance must have persona set."""
        version = get_template_root() / ".aget" / "version.json"
        with open(version) as f:
            data = json.load(f)
            assert data.get("persona"), "Instance must have persona"

    def test_instance_type_is_aget(self):
        """Instance must have instance_type: aget."""
        version = get_template_root() / ".aget" / "version.json"
        with open(version) as f:
            data = json.load(f)
            assert data.get("instance_type") == "aget"


# ============================================================
# Archetype-Specific Tests
# ============================================================

class TestAnalystArchetype:
    """Tests specific to analyst archetype."""

    def test_archetype_is_analyst(self):
        """Archetype must be analyst."""
        archetype = get_template_root() / ".aget" / "persona" / "archetype.yaml"
        if archetype.exists():
            content = archetype.read_text()
            assert "analyst" in content.lower() or "Analyst" in content

    def test_evidence_citation_inviolable(self):
        """Analyst must have evidence citation inviolable."""
        # Check archetype for inviolable
        archetype = get_template_root() / ".aget" / "persona" / "archetype.yaml"
        if archetype.exists():
            content = archetype.read_text()
            assert "INV-ANA-001" in content or "Evidence" in content


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
