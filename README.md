# haive-tools

[![PyPI version](https://img.shields.io/pypi/v/haive-tools.svg)](https://pypi.org/project/haive-tools/)
[![Python Versions](https://img.shields.io/pypi/pyversions/haive-tools.svg)](https://pypi.org/project/haive-tools/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/pr1m8/haive-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/pr1m8/haive-tools/actions/workflows/ci.yml)
[![Docs](https://github.com/pr1m8/haive-tools/actions/workflows/docs.yml/badge.svg)](https://pr1m8.github.io/haive-tools/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/haive-tools.svg)](https://pypi.org/project/haive-tools/)

**Tool implementations for Haive agents** — search, calculators, APIs, and integrations.

A curated collection of LangChain-compatible tools that work with any Haive agent.

## Installation

```bash
pip install haive-tools
```

## Features

- **🔍 Search** — Tavily, Google Search, DuckDuckGo, SerpAPI
- **🧮 Calculators** — math expressions, Wolfram Alpha
- **🌐 Web** — fetch URLs, scrape pages, parse HTML
- **🐍 Code** — Python REPL, sandboxed execution
- **📊 Data** — CSV/JSON parsing, structured extraction
- **🎮 Fun APIs** — Pokémon (PokéBase), Pokémon TCG, and more

## Quick Start

```python
from haive.tools.search import tavily_search_tool
from haive.agents.react.agent import ReactAgent
from haive.core.engine.aug_llm import AugLLMConfig

agent = ReactAgent(
    name="researcher",
    engine=AugLLMConfig(
        tools=[tavily_search_tool],
        system_message="Use the search tool to find information.",
    ),
)

result = agent.run("What is the latest Python version?")
```

## Documentation

📖 **Full documentation:** https://pr1m8.github.io/haive-tools/

## Related Packages

| Package | Description |
|---------|-------------|
| [haive-core](https://pypi.org/project/haive-core/) | Foundation: engines, graphs |
| [haive-agents](https://pypi.org/project/haive-agents/) | Production agents |
| [haive-mcp](https://pypi.org/project/haive-mcp/) | MCP server integration (1,960+ tools) |

## License

MIT © [pr1m8](https://github.com/pr1m8)
