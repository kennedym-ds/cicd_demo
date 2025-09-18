# Configuration file for the Sphinx documentation builder.
from typing import List

# -- Project information -----------------------------------------------------
project = "Python CI/CD Demo"
copyright = "2025, Python CI/CD Demo Contributors"
author = "Python CI/CD Demo Contributors"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinxcontrib.mermaid",
]

templates_path: List[str] = ["_templates"]
exclude_patterns: List[str] = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Extension configuration -------------------------------------------------
# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# MyST settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "html_image",
]

# Mermaid support
myst_fence_as_directive = ["mermaid"]
