# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# ...

sys.path.insert(0, os.path.abspath('../'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'tads_lener.settings'
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'LENER - School Admin'
copyright = '2023, Leon Augusto'
author = 'Leon Augusto'
release = '1.0'

# Exemplo de configuração para incluir apps
autodoc_mock_imports = ["agentes", "produtos"]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
]

html_output = os.path.abspath(os.path.join(os.path.dirname(__file__), '_build', 'html'))

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = 'https://leon-augusto.github.io/tads-lener/'
html_theme = 'furo'
html_static_path = ['_static']
