# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Public Address'
copyright = '2022, Public Address'
html_show_sphinx = False
html_show_sourcelink = False
author = 'Public Address'

html_context = {
    "display_github": False, # Add 'Edit on Github' link instead of 'View page source'
    "last_updated": True,
    "commit": False,
}

release = '2.9.1'
version = '2.9.1'

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

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
