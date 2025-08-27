from echo_sdk import tool


@tool
def my_info() -> str:
    """Get detail chatbot information"""
    return "I'm Echo AI - Multiple Agents Chatbot System,  I was specialized design for Business, created by JonasKahn."


my_info_tools = [my_info]
