"""Math Agent Plugin for ECHO - SDK Version.

This plugin demonstrates the new SDK-based architecture with true decoupling.
Auto-registers the plugin when imported.
"""

from echo_sdk import register_plugin

from .plugin import MathPlugin

# Auto-register when plugin package is imported
register_plugin(MathPlugin)
