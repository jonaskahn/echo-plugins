"""Math Agent Plugin using ECHO SDK."""

from echo_sdk import BasePlugin, PluginMetadata, BasePluginAgent


class MathPlugin(BasePlugin):
    """Math Plugin Bundle using SDK interfaces."""

    @staticmethod
    def get_metadata() -> PluginMetadata:
        """Return plugin metadata."""
        return PluginMetadata(
            name="math_agent",
            version="1.0.0",
            description="Mathematical calculations and arithmetic operations agent",
            capabilities=[
                "addition",
                "subtraction",
                "multiplication",
                "division",
                "power",
                "modulo",
                "arithmetic",
                "calculations",
            ],
            llm_requirements={
                "provider": "openai",
                "model": "gpt-4o",
                "temperature": 0.1,  # Lower temperature for more precise calculations
                "max_tokens": 1024,
            },
            agent_type="specialized",
            dependencies=["echo-plugin-sdk>=1.0.0"],
            sdk_version=">=1.0.0",
        )

    @staticmethod
    def create_agent() -> BasePluginAgent:
        """Create math agent instance."""
        from .agent import MathAgent

        return MathAgent(MathPlugin.get_metadata())

    @staticmethod
    def validate_dependencies() -> list[str]:
        """Validate plugin dependencies."""
        errors = []

        # Check if SDK is available
        try:
            import echo_sdk
        except ImportError:
            errors.append("echo-plugin-sdk is required")

        return errors

    @staticmethod
    def get_config_schema() -> dict:
        """Return configuration schema."""
        return {
            "type": "object",
            "properties": {
                "precision": {
                    "type": "integer",
                    "default": 10,
                    "description": "Number of decimal places for calculations",
                },
                "max_calculation_size": {
                    "type": "integer",
                    "default": 1000000,
                    "description": "Maximum number size for calculations",
                },
            },
            "required": [],
        }

    @staticmethod
    def health_check() -> dict:
        """Perform health check."""
        try:
            # Test basic math operations
            from .tools import add, subtract, multiply

            # Basic functionality test
            assert add(2, 3) == 5
            assert subtract(5, 3) == 2
            assert multiply(2, 4) == 8

            return {
                "healthy": True,
                "details": "Math plugin is operational",
                "checks": {"basic_operations": "OK", "tool_availability": "OK"},
            }
        except Exception as e:
            return {
                "healthy": False,
                "details": f"Math plugin health check failed: {e}",
                "error": str(e),
            }
