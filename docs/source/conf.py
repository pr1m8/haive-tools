"""Simple Sphinx configuration for haive-tools documentation."""

import os
import sys
from datetime import datetime

# Path setup
sys.path.insert(0, os.path.abspath("../../src"))

# Project information
project = "haive-tools"
copyright = f"{datetime.now().year}, Haive Team"
author = "Haive Team"
release = "0.1.0"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.githubpages",
    "sphinx.ext.todo",
    "sphinx_autodoc_typehints",
    "autoapi.extension",
    "myst_parser",
    "sphinxcontrib.mermaid",
    "sphinx_copybutton",
]

# AutoAPI configuration
autoapi_dirs = ["../../src/haive"]
autoapi_type = "python"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]
autoapi_ignore = ["*/test_*.py", "*/conftest.py", "*/tests/*", "*/.venv/*"]
autoapi_add_toctree_entry = True
autoapi_member_order = "groupwise"
autoapi_python_class_content = "both"
autoapi_python_use_implicit_namespaces = True

# Autodoc settings
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "show-inheritance": True,
}
autodoc_typehints = "both"

# MyST configuration
myst_enable_extensions = [
    "deflist",
    "tasklist",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "pydantic": ("https://docs.pydantic.dev/latest/", None),
    "langchain": ("https://python.langchain.com/", None),
    "haive-core": ("https://docs.haive.ai/packages/haive-core/", None),
}

# HTML output
html_theme = "furo"
html_static_path = ["_static"]
html_title = "haive-tools"
html_baseurl = "https://docs.haive.ai/packages/haive-tools/"
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7C4DFF",
        "color-brand-content": "#6C3DDF",
    },
    "dark_css_variables": {
        "color-brand-primary": "#9C7DFF",
        "color-brand-content": "#8C6DFF",
    },
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/haive/haive-tools",
            "html": '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path></svg>',
        },
    ],
    "announcement": "<b>🛠️</b> Haive Tools - 120+ AI tools and toolkits",
}

# Source suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Master doc
master_doc = 'index'

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Pygments style
pygments_style = 'sphinx'

def setup(app):
    """Custom setup for documentation."""
    pass