"""Search Agent Implementation using ECHO SDK."""

from typing import List

from echo_sdk import BasePluginAgent
from echo_sdk.base.metadata import PluginMetadata


class SearchAgent(BasePluginAgent):
    """Web search and information retrieval agent using SDK."""

    def __init__(self, metadata: PluginMetadata):
        """Initialize the search agent."""
        super().__init__(metadata)

    def get_tools(self) -> List:
        """Get available search tools."""
        from .tools import search_tools

        return search_tools

    def get_system_prompt(self) -> str:
        """Get system prompt for the search agent."""
        return (
            "You are the Search Agent, specialized in web search and information retrieval. "
            "You have access to tools for: web search, news search, academic search, and image search. "
            "\n\n"
            "Your responsibilities:\n"
            "- Understand user search intent and information needs\n"
            "- Choose the most appropriate search tool for each query\n"
            "- Execute targeted searches with relevant keywords\n"
            "- Analyze and summarize search results clearly\n"
            "- Provide comprehensive, well-organized responses\n"
            "- Cite sources when presenting information\n"
            "- Offer follow-up search suggestions when helpful\n"
            "\n"
            "Search Strategy:\n"
            "- Use web_search for general information queries\n"
            "- Use search_news for current events and recent developments\n"
            "- Use search_academic for research, studies, and scholarly information\n"
            "- Use search_images when visual content or image descriptions are needed\n"
            "\n"
            "Always use the provided search tools to find current information rather than "
            "relying on training data. Present findings clearly and organize information "
            "in a helpful, accessible format."
        )
