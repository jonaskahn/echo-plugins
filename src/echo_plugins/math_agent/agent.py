"""Math Agent Implementation using ECHO SDK."""

from typing import List

from echo_sdk import BasePluginAgent, tool
from echo_sdk.base.metadata import PluginMetadata


class MathAgent(BasePluginAgent):
    """Math operations and problem-solving agent using SDK."""

    def __init__(self, metadata: PluginMetadata):
        """Initialize the math agent."""
        super().__init__(metadata)

    def get_tools(self) -> List:
        """Get available math tools."""
        from .tools import math_tools

        return math_tools

    def get_system_prompt(self) -> str:
        """Get system prompt for the math agent."""
        return (
            "You are the Math Agent, specialized in mathematical operations and calculations. "
            "You have access to tools for: addition, subtraction, multiplication, division, "
            "exponentiation (power), and modulo operations. "
            "\n\n"
            "Your responsibilities:\n"
            "- Parse mathematical problems and expressions\n"
            "- Break down complex calculations into step-by-step operations\n"
            "- Use appropriate tools for each mathematical operation\n"
            "- Show your work clearly and explain each step\n"
            "- Provide accurate results with clear explanations\n"
            "- Handle edge cases like division by zero gracefully\n"
            "\n"
            "Always use the provided tools to perform calculations rather than doing math "
            "mentally. This ensures accuracy and allows the user to see your work."
        )
