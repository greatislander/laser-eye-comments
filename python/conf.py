# Configuration for Sphinx.
# See https://tobywf.com/2019/08/running-sphinx-on-a-single-python-file/

import os
import sys

# Enable autodoc to load local modules
sys.path.insert(0, os.path.abspath("."))

project = "laser_eye_comments"
author = "Ned Zimmerman"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx"]
templates_path = ["_templates"]
html_theme = "alabaster"
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None)
}
html_theme_options = {"nosidebar": True}
