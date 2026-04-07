# haive-tools

[![PyPI version](https://img.shields.io/pypi/v/haive-tools.svg)](https://pypi.org/project/haive-tools/)
[![Python Versions](https://img.shields.io/pypi/pyversions/haive-tools.svg)](https://pypi.org/project/haive-tools/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/pr1m8/haive-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/pr1m8/haive-tools/actions/workflows/ci.yml)
[![Docs](https://github.com/pr1m8/haive-tools/actions/workflows/docs.yml/badge.svg)](https://pr1m8.github.io/haive-tools/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/haive-tools.svg)](https://pypi.org/project/haive-tools/)

**Tool implementations for Haive agents** — search, calculators, APIs, code execution, and integrations.

A curated collection of LangChain-compatible tools, ready to drop into any Haive agent. Each tool is wrapped, tested, and exposed via a consistent interface. Use them with `ReactAgent`, `MultiAgent`, `MemoryAgent`, or any agent that takes tools.

---

## Why haive-tools?

LangChain has hundreds of tools but they're scattered across packages, have inconsistent interfaces, and many require fiddly setup. `haive-tools` curates the most useful ones, fixes their quirks, and packages them as a coherent toolkit.

### Tool categories

| Category | Tools | What they do |
|----------|-------|--------------|
| **🔍 Search** | Tavily, Google Search, DuckDuckGo, SerpAPI, Brave Search | Web search with structured results |
| **🧮 Calculators** | Python REPL, math expressions, Wolfram Alpha | Calculation and symbolic math |
| **🌐 Web** | Fetch URL, scrape HTML, parse JSON | HTTP requests and web scraping |
| **🐍 Code** | Python REPL (sandboxed), shell commands | Code execution |
| **📊 Data** | CSV/JSON parsers, structured extractors | Data processing |
| **🎮 Fun APIs** | Pokémon (PokéBase), Pokémon TCG | API wrappers for testing |
| **📖 Documents** | PDF reader, docx parser, web fetcher | Document loading |
| **🗄️ Databases** | SQL execution, schema inspection | Database tools |

---

## Installation

```bash
pip install haive-tools

# For Tavily search:
pip install haive-tools[tavily]

# For all extras:
pip install haive-tools[all]
```

---

## Quick Start

### Web Search with Tavily

```python
from haive.tools.search import tavily_search_tool
from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig
import os

# Set TAVILY_API_KEY in env
os.environ["TAVILY_API_KEY"] = "tvly-..."

agent = ReactAgent(
    name="researcher",
    engine=AugLLMConfig(
        tools=[tavily_search_tool],
        system_message="Use the search tool to find information.",
    ),
    max_iterations=5,
)

result = agent.run("What are the latest advances in quantum computing in 2025?")
```

### Calculator + Web Search Combo

```python
from haive.tools.search import tavily_search_tool
from haive.tools.calculators import python_calculator
from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

agent = ReactAgent(
    name="research_assistant",
    engine=AugLLMConfig(
        tools=[tavily_search_tool, python_calculator],
        system_message="Use search for facts and calculator for math.",
    ),
)

result = agent.run("What is the population of Tokyo divided by the area of Japan?")
# Agent: searches for both values, then calculates ratio
```

### Custom Tool Composition

```python
from langchain_core.tools import tool
from haive.tools.search import tavily_search_tool
from haive.tools.web import fetch_url

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    # ... your custom logic ...
    return f"Sunny, 72°F in {city}"

agent = ReactAgent(
    name="multi_tool",
    engine=AugLLMConfig(tools=[
        tavily_search_tool,
        fetch_url,
        get_weather,
    ]),
)
```

---

## Tool Routing

All tools work with Haive's automatic tool routing system. You can mix:

- **LangChain `BaseTool`** (from `@tool` decorator) → routed to `langchain_tool`
- **Pydantic models with `__call__`** → routed to `pydantic_tool` (stateful tools)
- **Plain callables** → routed to `function`

```python
from pydantic import BaseModel

class StatefulSearchTool(BaseModel):
    """Search tool with configurable settings."""
    api_key: str
    max_results: int = 5
    region: str = "us"

    def __call__(self, query: str) -> str:
        # Each instance has its own state
        return f"Searching {self.region}: {query}"

# Two instances with different config
us_search = StatefulSearchTool(api_key="...", region="us")
eu_search = StatefulSearchTool(api_key="...", region="eu")

agent = ReactAgent(engine=AugLLMConfig(tools=[us_search, eu_search]))
```

---

## Tool Reference

### Search

- `tavily_search_tool` — Tavily web search (5 results, news + general)
- `google_search_tool` — Google Custom Search API
- `duckduckgo_search_tool` — Free DuckDuckGo search
- `brave_search_tool` — Brave Search API
- `serpapi_search_tool` — SerpAPI for Google/Bing/etc.

### Calculators

- `python_calculator` — Sandboxed Python REPL for math expressions
- `wolfram_alpha_tool` — Symbolic math via Wolfram Alpha API

### Web

- `fetch_url` — HTTP GET with auto-decoding
- `scrape_url` — Scrape HTML with BeautifulSoup
- `parse_json` — Parse JSON responses

### Code

- `python_repl` — Sandboxed Python execution
- `shell_command` — Execute shell commands (with safety checks)

### Documents

- `read_pdf` — Extract text from PDF files
- `read_docx` — Parse Word documents
- `web_loader` — Load and parse web pages

---

## Documentation

📖 **Full documentation:** https://pr1m8.github.io/haive-tools/

---

## Related Packages

| Package | Description |
|---------|-------------|
| [haive-core](https://pypi.org/project/haive-core/) | Foundation: engines, graphs |
| [haive-agents](https://pypi.org/project/haive-agents/) | Production agents |
| [haive-mcp](https://pypi.org/project/haive-mcp/) | Dynamic MCP server tools (1,960+) |

---

## License

MIT © [pr1m8](https://github.com/pr1m8)
