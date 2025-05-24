# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Public Address'
copyright = '2025, Public Address'
html_show_sphinx = False
html_show_sourcelink = False
author = 'Public Address'

release = '4.3.0'
version = '4.3.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

language = 'en'

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'furo'

html_theme_options = {
    "light_logo": "logo-light.png",
    "dark_logo": "logo-dark.png",
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
