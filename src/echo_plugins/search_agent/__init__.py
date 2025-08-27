"""Search Agent Plugin for Echo - SDK Version.

This plugin demonstrates the new SDK-based architecture with true decoupling.
Auto-registers the plugin when imported.
"""

from echo_sdk import register_plugin

from .plugin import SearchPlugin

register_plugin(SearchPlugin)
