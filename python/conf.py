import os
import sys

# Enable autodoc to load local modules
sys.path.insert(0, os.path.abspath("."))

project = "laser_eye_comments"
author = "Ned Zimmerman"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx"]
templates_path = ["_templates"]
html_theme = "alabaster"
# html_static_path = ["_static"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None)
}
html_theme_options = {"nosidebar": True}
