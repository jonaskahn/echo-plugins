"""Echo Plugins Package - Auto-registers all plugins when imported."""

try:
    from . import math_agent, myinfo_agent, search_agent
except ImportError as e:
    pass
