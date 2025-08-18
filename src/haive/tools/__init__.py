"""Haive Tools Package - Comprehensive collection of utility tools and integrations.

This package provides a rich ecosystem of tools that can be used independently
or integrated with Haive agents for enhanced functionality. The tools cover
a wide range of capabilities including web search, data analysis, external
API integrations, and specialized utilities.

Tool Categories:

Search and Information Retrieval:
    - Google Search: Comprehensive Google search integration
    - DuckDuckGo Search: Privacy-focused search capabilities
    - ArXiv: Academic paper search and retrieval
    - Google Books: Book search and information

Location and Geographic:
    - Google Places: Location search and business information
    - Google Maps: Mapping and navigation tools

Data Analysis and Finance:
    - Google Finance: Financial data and stock information
    - Google Trends: Search trends and popularity data
    - DataForSEO: SEO and web analytics tools

Social and Demographics:
    - Genderize Tool: Name-based gender prediction
    - Report of the Week: Weekly report generation

Specialized APIs:
    - Pokebase Tool: Pokemon data and information
    - Techy Phrase Tool: Technical phrase generation
    - Google Lens: Visual search and analysis
    - Google Jobs: Job search and listings

The tools are designed with the following principles:
- Consistent API interface across all tools
- Comprehensive error handling and validation
- Rate limiting and quota management
- Extensible configuration options
- Rich output formatting with metadata
- Async/await support for performance

Usage:
            from haive.tools.google import GoogleSearchTool
            from haive.tools.arxiv import ArxivTool
            from haive.tools.dataforseo import DataForSEOTool

            # Initialize search tool
            search_tool = GoogleSearchTool(api_key="your_key")

            # Perform a search
            results = await search_tool.search("artificial intelligence")

            # Search academic papers
            arxiv_tool = ArxivTool()
            papers = await arxiv_tool.search("machine learning", max_results=10)

            # SEO analysis
            seo_tool = DataForSEOTool(username="user", pass="pass
            analysis = await seo_tool.analyze_website("example.com")

Configuration:
    Most tools require API keys or credentials. These can be provided via:
    - Direct initialization parameters
    - Environment variables
    - Configuration files
    - Haive configuration system

Each tool includes:
- Comprehensive validation of inputs and outputs
- Detailed error messages and recovery suggestions
- Usage examples and documentation
- Integration tests and benchmarks
- Performance monitoring and metrics
"""

import lazy_loader as lazy

# Define submodules to lazy load
submodules = ["tools", "toolkits"]

# Define specific attributes from submodules to expose
submod_attrs = {
    "tools": [
        "arxiv_query_tool",
        "duckduckgo_search_results",
        "duckduckgo_search_tool",
        "google_search_tool",
    ],
    "toolkits": [],  # Heavy toolkits are fully lazy loaded
}

# Attach lazy loading - this creates __getattr__, __dir__, and __all__
__getattr__, __dir__, __all__ = lazy.attach(
    __name__, submodules=submodules, submod_attrs=submod_attrs
)

# Add version and other lightweight imports
__version__ = "0.1.0"

# Add eager imports to __all__
__all__ += ["__version__"]

# Note: Heavy toolkits and specialized tools are lazy loaded for performance
