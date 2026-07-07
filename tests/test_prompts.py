"""
Testes automatizados para validação de prompts.
"""

import yaml
from pathlib import Path


PROMPT_FILE = Path("prompts/bug_to_user_story_v2.yml")


def load_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestPrompts:

    def test_prompt_has_system_prompt(self):
        """Verifica se existe um system prompt."""
        prompt = load_prompt()

        assert "system" in prompt
        assert prompt["system"]
        assert len(prompt["system"].strip()) > 0

    def test_prompt_has_role_definition(self):
        """Verifica se há definição de persona."""
        prompt = load_prompt()

        system = prompt.get("system", "").lower()

        assert (
            "product manager" in system
            or "persona" in system
            or "especializado" in system
        )

    def test_prompt_mentions_format(self):
        """Verifica se existe definição de formato."""
        prompt = load_prompt()

        assert "output_format" in prompt
        assert len(prompt["output_format"].strip()) > 0

    def test_prompt_has_few_shot_examples(self):
        """Verifica se existem exemplos Few-shot."""
        prompt = load_prompt()

        assert "examples" in prompt
        assert isinstance(prompt["examples"], list)
        assert len(prompt["examples"]) >= 2

    def test_prompt_no_todos(self):
        """Verifica se o prompt não contém TODO."""
        prompt = load_prompt()

        yaml_content = str(prompt).lower()

        assert "todo" not in yaml_content
        assert "[todo]" not in yaml_content

    def test_minimum_techniques(self):
        """Verifica se pelo menos duas técnicas foram aplicadas."""
        prompt = load_prompt()

        techniques = prompt.get("techniques", [])

        assert len(techniques) >= 2

        expected = {
            "few-shot",
            "role-prompting",
            "chain-of-thought",
        }

        assert len(expected.intersection(set(techniques))) >= 2


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v", "--tb=short"])