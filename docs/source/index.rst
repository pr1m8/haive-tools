Welcome to haive-tools
=======================

.. image:: https://img.shields.io/pypi/v/haive-tools?style=flat-square
   :target: https://pypi.org/project/haive-tools/
   :alt: PyPI Version

.. image:: https://img.shields.io/github/license/pr1m8/haive-tools?style=flat-square
   :target: https://github.com/pr1m8/haive-tools/blob/main/LICENSE
   :alt: License

**haive-tools** provides 120+ AI tools and toolkits for the Haive ecosystem - the most comprehensive collection of production-ready integrations.

✨ **Key Features**
------------------

🛠️ **120+ Production Tools**
   Comprehensive integrations across all major APIs and services

🔍 **Advanced Search Intelligence**
   Tavily context search, Google ecosystem, academic research

💻 **Development Toolkit**
   CST transformers, code analysis, automated refactoring

💰 **Financial Data APIs**
   FRED economic data, Alpha Vantage, Polygon, Yahoo Finance

📡 **Communication Tools**
   Discord, Slack, Twilio, Gmail, Jira integration

🎮 **Entertainment APIs**
   Gaming databases, reference materials, fun utilities

⚡ **Quick Start**
-----------------

Install haive-tools:

.. code-block:: bash

   poetry add haive-tools

Use advanced search tools:

.. code-block:: python

   from haive.tools.search_tools import tavily_qna
   
   # Context-aware question answering
   answer = tavily_qna(
       query="What are the latest developments in AI?",
       search_depth="advanced",
       include_answer=True,
       days=7
   )
   print(f"Answer: {answer}")

Access Google ecosystem:

.. code-block:: python

   from haive.tools.google import google_search_tool
   
   # Google search with rich metadata
   results = google_search_tool(
       query="machine learning frameworks",
       num_results=10,
       include_snippets=True
   )
   print(f"Found {len(results)} results")

📚 **Documentation**
-------------------

.. toctree::
   :maxdepth: 2
   :caption: 📖 User Guide

   getting_started
   tool_categories
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: 🔧 Tool Categories

   search_and_intelligence
   development_toolkit
   google_ecosystem
   financial_data_tools
   communication_tools
   entertainment_and_gaming

.. toctree::
   :maxdepth: 2
   :caption: 💻 Development

   examples
   api_integrations
   comprehensive_toolkits
   api_reference

.. toctree::
   :maxdepth: 1
   :caption: 📝 Reference
   
   changelog

🔍 **API Reference**
-------------------

Complete API documentation with examples:

.. toctree::
   :maxdepth: 1
   :caption: 🔍 API Reference

   autoapi/haive/tools/index

📊 **Project Info**
------------------

* **GitHub**: https://github.com/pr1m8/haive-tools
* **Documentation**: https://pub-7f716b302a2948e19f08b49b71408039.r2.dev/packages/haive-tools/
* **PyPI**: https://pypi.org/project/haive-tools/
* **License**: MIT

🔗 **Related Projects**
----------------------

* `haive-core <https://github.com/pr1m8/haive-core>`_ - Core agent framework
* `haive-agents <https://github.com/pr1m8/haive-agents>`_ - Pre-built agent implementations  
* `haive-hap <https://github.com/pr1m8/haive-hap>`_ - Agent orchestration protocol
* `haive-mcp <https://github.com/pr1m8/haive-mcp>`_ - Model Context Protocol integration

📄 **Indices and Tables**
-------------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`