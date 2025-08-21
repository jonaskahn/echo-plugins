from typing import List

from echo_sdk import BasePluginAgent
from langchain_core.tools import Tool

from .tools import my_info_tools


class MyInfoAgent(BasePluginAgent):
    def get_tools(self) -> List[Tool]:
        return my_info_tools

    def get_system_prompt(self) -> str:
        return """You're Echo AI, your goal is to help user understand, get to know who you are"""
