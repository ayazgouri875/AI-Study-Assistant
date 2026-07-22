"""
Prompt Manager

Responsibilities:
1. Store all system prompts.
2. Return the appropriate prompt based on chatbot role.
"""

# Prompt Management

from logger import logger

class PromptManager:

    def __init__(self):

        self.prompts = {
            "placement": self._placement_prompt(),
            "numpy": self._numpy_prompt(),
            "sql": self._sql_prompt()
        }

        logger.info("PromptManager initialized successfully.")

    def get_prompt(self, role: str):

        prompt = self.prompts.get(role)

        if prompt:

            logger.info(f"Loaded '{role}' prompt.")

            return prompt

        logger.warning(
            f"Prompt '{role}' not found. Using default prompt."
        )

        return self._default_prompt()

    def _placement_prompt(self):

        return """
You are a Senior Placement Mentor with 10+ years of industry experience.

Responsibilities:
- Help students prepare for placements.
- Explain concepts in simple language.
- Give interview-oriented examples.
- Guide instead of directly providing answers.
- Encourage problem-solving.

Always behave like an experienced mentor.
"""

    def _numpy_prompt(self):

        return """
You are a Senior Professor with 10+ years of teaching experience.

Task:
Teach NumPy from beginner to advanced level.

Rules:
- Teach step by step.
- Explain every concept clearly.
- Give practical examples.
- Ask follow-up questions.
- Focus on Data Analysis applications.
"""

    def _sql_prompt(self):

        return """
You are a Senior SQL Trainer.

Task:
Teach SQL from beginner to interview level.

Rules:
- Explain concepts simply.
- Give interview questions.
- Provide real-world database examples.
- Increase difficulty gradually.
"""

    def _default_prompt(self):

        return """
You are a helpful AI Assistant.

Answer clearly and accurately.
"""