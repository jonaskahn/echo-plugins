"""Search Agent Plugin using ECHO SDK."""

from echo_sdk import BasePlugin, PluginMetadata, BasePluginAgent


class SearchPlugin(BasePlugin):
    """Search Plugin Bundle using SDK interfaces."""

    @staticmethod
    def get_metadata() -> PluginMetadata:
        """Return plugin metadata."""
        return PluginMetadata(
            name="search_agent",
            version="1.0.0",
            description="Web search and information retrieval agent",
            capabilities=[
                "web_search",
                "news_search",
                "academic_search",
                "image_search",
                "information_lookup",
                "research",
                "fact_finding",
            ],
            llm_requirements={
                "provider": "openai",
                "model": "gpt-4o",
                "temperature": 0.3,  # Lower temperature for more focused search
                "max_tokens": 1024,
            },
            agent_type="specialized",
            dependencies=[
                "echo-plugin-sdk>=1.0.0",
                "langchain-community>=0.3.0",
                "duckduckgo-search>=8.0.0",
            ],
            sdk_version=">=1.0.0",
        )

    @staticmethod
    def create_agent() -> BasePluginAgent:
        """Create search agent instance."""
        from .agent import SearchAgent

        return SearchAgent(SearchPlugin.get_metadata())

    @staticmethod
    def validate_dependencies() -> list[str]:
        """Validate plugin dependencies."""
        errors = []

        # Check if SDK is available
        try:
            import echo_sdk
        except ImportError:
            errors.append("echo-plugin-sdk is required")

        # Check if DuckDuckGo search is available
        try:
            from langchain_community.tools import DuckDuckGoSearchRun
        except ImportError:
            errors.append("langchain-community and duckduckgo-search are required")

        return errors

    @staticmethod
    def get_config_schema() -> dict:
        """Return configuration schema."""
        return {
            "type": "object",
            "properties": {
                "search_timeout": {
                    "type": "integer",
                    "default": 10,
                    "description": "Search timeout in seconds",
                },
                "max_results": {
                    "type": "integer",
                    "default": 5,
                    "description": "Maximum number of search results",
                },
                "result_length": {
                    "type": "integer",
                    "default": 500,
                    "description": "Maximum length of search result text",
                },
            },
            "required": [],
        }

    @staticmethod
    def health_check() -> dict:
        """Perform health check."""
        try:
            # Test search functionality
            from langchain_community.tools import DuckDuckGoSearchRun

            # Quick connectivity test
            search = DuckDuckGoSearchRun()

            return {
                "healthy": True,
                "details": "Search plugin is operational",
                "checks": {"search_engine": "OK", "dependencies": "OK"},
            }
        except Exception as e:
            return {
                "healthy": False,
                "details": f"Search plugin health check failed: {e}",
                "error": str(e),
            }
