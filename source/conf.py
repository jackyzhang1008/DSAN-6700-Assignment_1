# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'dsan-6700-assignment-1'
copyright = '2024, Isfar Baset, Sheeba Moghal, Bella Shi, Jacky Zhang, Ziyan Di'
author = 'Isfar Baset, Sheeba Moghal, Bella Shi, Jacky Zhang, Ziyan Di'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
    # 'autoapi.extension'
]

# AutoAPI configuration 
# autoapi_dirs = ['../ml_app']  

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
