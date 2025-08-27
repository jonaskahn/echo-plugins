# Echo Plugins

Collection of specialized sample AI agent plugins for the Echo multi-agent system.

## Overview

Echo Plugins extends the Echo multi-agent system with domain-specific capabilities through specialized AI agents. Each
plugin implements the Echo SDK interfaces to provide seamless integration with the core orchestration system.

## Available Plugins

### 🧮 Math Agent

A specialized agent for mathematical operations and calculations.

**Capabilities:**

- Addition, subtraction, multiplication, division
- Exponentiation (power operations)
- Modulo operations
- Step-by-step calculation breakdown
- Error handling (division by zero, overflow protection)

**Configuration:**

```python
{
    "precision": 10,  # Decimal places for calculations
    "max_calculation_size": 1000000  # Maximum number size limit
}
```

**Example Usage:**

```python
# The Math Agent can handle various mathematical operations
"Calculate 15 * 8 + 42"
"What's 2^10?"
"Find the remainder when 17 is divided by 5"
```

**Tools Available:**

- `add(a, b)` - Addition of two numbers
- `subtract(a, b)` - Subtraction operation
- `multiply(a, b)` - Multiplication operation
- `divide(a, b)` - Division with zero-check
- `power(a, b)` - Exponentiation with overflow protection
- `modulo(a, b)` - Modulo operation with zero-check

### 🔍 Search Agent

A comprehensive web search and information retrieval agent.

**Capabilities:**

- Web search via DuckDuckGo
- News and current events search
- Academic and research information lookup
- Image search and visual content discovery
- Source citation and result organization

**Configuration:**

```python
{
    "search_timeout": 10,  # Search timeout in seconds
    "max_results": 5,  # Maximum number of results
    "result_length": 500  # Maximum result text length
}
```

**Example Usage:**

```python
# The Search Agent can find current information on various topics
"Search for recent developments in AI research"
"Find news about renewable energy trends"
"Look up academic papers on quantum computing"
"Search for images of sustainable architecture"
```

**Tools Available:**

- `web_search(query)` - General web search
- `search_news(query)` - Recent news and events
- `search_academic(query)` - Academic and research content
- `search_images(query)` - Visual content search

## Installation

### From Source

```bash
cd plugins/
poetry install
```

### Dependencies

The plugins package requires:

- `echo_sdk` (>=0.1.0,<0.1.0) - Core SDK framework
- `langchain-core` (>=0.3.74,<0.4.0) - LangChain foundation
- `langgraph` (>=0.6.5,<0.7.0) - Graph-based workflows
- `pydantic` (>=2.11.7,<3.0.0) - Data validation

**Additional Plugin Dependencies:**

- `langchain-community` (>=0.3.0) - For search functionality
- `duckduckgo-search` (>=8.0.0) - Search engine integration

## Architecture

Each plugin follows the Echo SDK architecture:

```
plugins/
├── src/echo_plugins/        # Main plugins package
│   ├── __init__.py          # Auto-registration of all plugins
│   ├── math_agent/          # Math operations plugin
│   │   ├── __init__.py      # Plugin registration
│   │   ├── plugin.py        # Plugin configuration and metadata
│   │   ├── agent.py         # Agent implementation
│   │   └── tools.py         # Tool definitions and implementations
│   └── search_agent/        # Web search plugin
│       ├── __init__.py      # Plugin registration
│       ├── plugin.py        # Plugin configuration and metadata
│       ├── agent.py         # Agent implementation
│       └── tools.py         # Tool definitions and implementations
├── pyproject.toml           # Package configuration
├── README.md                # This documentation
└── LICENSE                  # MIT license
```

### Plugin Structure

**Plugin Class** (`plugin.py`):

- Metadata definition (name, version, capabilities)
- LLM requirements and configuration
- Health checks and dependency validation
- Configuration schema

**Agent Class** (`agent.py`):

- System prompt definition for specialized behavior
- Tool integration and management
- Agent initialization and setup

**Tools** (`tools.py`):

- Individual tool implementations with error handling
- SDK decorators for seamless integration
- Comprehensive validation and safety checks

## Development

### Creating New Plugins

1. **Create Plugin Structure:**

```bash
mkdir src/echo_plugins/your_plugin/
touch src/echo_plugins/your_plugin/{__init__.py,plugin.py,agent.py,tools.py}
```

2. **Implement Plugin Class:**

```python
from echo_sdk import BasePlugin, PluginMetadata


class YourPlugin(BasePlugin):
    @staticmethod
    def get_metadata() -> PluginMetadata:
        return PluginMetadata(
            name="your_plugin",
            version="0.1.0",
            description="Your plugin description",
            capabilities=["capability1", "capability2"],
            llm_requirements={
                "provider": "openai",
                "model": "gpt-4o",
                "temperature": 0.1,
                "max_tokens": 1024
            },
            dependencies=["echo_sdk>=1.0.0,<2.0.0"],
            sdk_version=">=1.0.0,<2.0.0"
        )

    @staticmethod
    def create_agent() -> BasePluginAgent:
        from .agent import YourAgent
        return YourAgent(YourPlugin.get_metadata())

    @staticmethod
    def validate_dependencies() -> list[str]:
        """Validate plugin dependencies."""
        errors = []
        try:
            import echo_sdk
        except ImportError:
            errors.append("echo_sdk is required")
        return errors

    @staticmethod
    def health_check() -> dict:
        """Perform health check."""
        try:
            # Test basic functionality
            return {
                "healthy": True,
                "details": "Plugin is operational",
                "checks": {"basic_functionality": "OK"}
            }
        except Exception as e:
            return {
                "healthy": False,
                "details": f"Health check failed: {e}",
                "error": str(e)
            }
```

3. **Implement Agent:**

```python
from echo_sdk import BasePluginAgent
from echo_sdk.base.metadata import PluginMetadata


class YourAgent(BasePluginAgent):
    def __init__(self, metadata: PluginMetadata):
        super().__init__(metadata)

    def get_tools(self) -> List:
        from .tools import your_tools
        return your_tools

    def get_system_prompt(self) -> str:
        return "You are YourAgent specialized in..."

    def bind_model(self, model):
        """Bind tools to an LLM model."""
        return model.bind_tools(self.get_tools())

    def initialize(self):
        """Initialize the agent."""
        pass

    def create_agent_node(self):
        """Create LangGraph node function."""
        pass

    def should_continue(self, state):
        """Decide whether to continue or return to coordinator."""
        pass
```

4. **Create Tools:**

```python
from echo_sdk import tool


@tool
def your_tool(param: str) -> str:
    """Your tool description."""
    # Implementation with error handling
    try:
        # Your tool logic here
        result = f"Processed: {param}"
        return result
    except Exception as e:
        return f"Error processing {param}: {str(e)}"


# Export tools list
your_tools = [your_tool]
```

5. **Register Plugin** (`__init__.py`):

```python
from echo_sdk import register_plugin
from .plugin import YourPlugin

register_plugin(YourPlugin)
```

### Testing

Run the test suite:

```bash
poetry run pytest tests/
```

### Code Quality

The project uses several code quality tools:

- **Black** - Code formatting (120 character line length)
- **isort** - Import sorting
- **mypy** - Type checking (strict mode)
- **ruff** - Linting

Run quality checks:

```bash
poetry run black src/
poetry run isort src/
poetry run mypy src/
poetry run ruff check src/
```

## Plugin Health Checks

Each plugin implements comprehensive health checks to ensure proper functionality:

```python
# Math Agent Health Check
- Basic
operations
verification(add, subtract, multiply)
- Tool
availability
confirmation
- Dependency
validation

# Search Agent Health Check
- DuckDuckGo
connectivity
test
- Dependency
verification
- Search
functionality
validation
```

## Configuration

Plugins can be configured through the Echo core system. Each plugin defines its configuration schema and default values.

### Example Configuration

```python
{
    "math_agent": {
        "precision": 10,
        "max_calculation_size": 1000000
    },
    "search_agent": {
        "search_timeout": 10,
        "max_results": 5,
        "result_length": 500
    }
}
```

## Error Handling

All plugins implement robust error handling:

- **Math Agent**: Division by zero, overflow protection, calculation limits
- **Search Agent**: Network timeouts, API errors, malformed queries

## Auto-Registration

Plugins automatically register themselves when imported:

```python
# In src/echo_plugins/__init__.py
try:
    from . import math_agent
    from . import search_agent
except ImportError as e:
    pass
```

This ensures that all available plugins are automatically discovered by the Echo system without manual configuration.

## SDK Integration

These plugins are built using the Echo SDK, which provides:

- **Clean Interfaces**: Well-defined contracts for plugin development
- **Zero Core Dependencies**: Plugins only depend on the SDK, not the core system
- **Independent Distribution**: Plugins can be distributed as standalone packages
- **Version Management**: SDK versioning with compatibility checks
- **Testing Isolation**: Test plugins without running the core system
- **Auto-Registration**: Automatic plugin discovery through global registry

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-plugin`)
3. Implement your plugin following the architecture guidelines
4. Add comprehensive tests
5. Ensure code quality checks pass
6. Submit a pull request

### Development Standards

- Follow **KISS** (Keep It Simple, Stupid) principles
- Follow **DRY** (Don't Repeat Yourself) principles
- Write **self-documenting code** with meaningful names
- Avoid redundant comments inside methods
- Use comprehensive error handling
- Implement proper health checks
- Follow the established plugin structure

## License

MIT License - see [LICENSE](../LICENSE) for details.

## Support

For questions, issues, or contributions:

- **Issues**: [GitHub Issues](https://github.com/jonaskahn/echo-plugins/issues)
- **Documentation**: [Echo Plugins Docs](https://echo-plugins.readthedocs.io/)
- **Repository**: [GitHub Repository](https://github.com/jonaskahn/echo-plugins)
