# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from sphinx_needs.api import add_dynamic_function

# -- Path setup --------------------------------------------------------------

import os
import sys

# Path for local extensions
sys.path.insert(0, os.path.abspath('exts'))

# -- Project information -----------------------------------------------------

project = 'Example System'
copyright = '2023, Hugh Greene'
author = 'Hugh Greene'

# The full version, including alpha/beta/rc tags
release = '3.14'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.jquery',
    'sphinxcontrib.plantuml',
    'sphinx_needs',
    'sphinx_needs_planguage'
]

primary_domain = 'planguage'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

default_role = 'emphasis'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_js_files = [
    'scripts/needs-planguage.js'
]
html_css_files = [
    "styles/needs_planguage.css"
]

# -- Options for sphinx-needs ------------------------------------------------


def child_needs_of_type(app, need, needs, type, *args, **kwargs):
    for other_need_id, other_need in needs.items():
        if other_need["type"] == type and other_need["parent_need"] == need["id"]:
            return other_need_id
    return "some data"

def setup(app):
        add_dynamic_function(app, child_needs_of_type)

needs_types = [
    dict(directive="sys", title="System", prefix="SYS:", color="#FF001C", style="node"),
    dict(directive="fr", title="Function Requirement", prefix="FR:", color="#BFD8D2", style="node"),
    dict(directive="qr", title="Quality Requirement", prefix="QR:", color="#BFD8D2", style="node"),
    dict(directive="dc", title="Design Constraint", prefix="DC:", color="#BFD8D2", style="node"),
    dict(directive="di", title="Design Idea", prefix="DI:", color="#BFD8D2", style="node"),
    dict(directive="qual", title="Qualifier", prefix="Q:", color="#BFD8D2", style="node"),

    dict(directive="milestone", title="Milestone", prefix="Milestone:", color="#808080", style="node"),
]

needs_extra_options = [
    # Basic Information
    'notes',
    'source',
    'author',
    'owner',

    # Measurement
    'tests',

    # Priority and Risk Management
    'rationale',
    'priority',
    'issues',
]

needs_extra_links = [
    # Relationships
    {
        "option": "qualifiers",
        "incoming": "qualifies",
        "outgoing": "is qualified by",
        "allow_dead_links": True,
    },
    {
        "option": "qualities",
        "incoming": "is a quality requirement of",
        "outgoing": "has quality requirements",
        "allow_dead_links": True,
    },
    {
        "option": "functions",
        "incoming": "is a sub-function of",
        "outgoing": "has sub-fuctions",
        "allow_dead_links": True,
    },
    {
        "option": "related",
        "incoming": "is related to",
        "outgoing": "is related to",
        "allow_dead_links": True,
    },
    {
        "option": "design_constraints",
        "incoming": "constrains",
        "outgoing": "is constrained by",
        "allow_dead_links": True,
    },
    # Design
    {
        "option": "design_ideas",
        "incoming": "is a design idea for",
        "outgoing": "has design idea",
        "allow_dead_links": True,
    },
]

needs_global_options = {
    'pre_template': 'pre_template',
    'template': 'template',
    'layout': [
        ('focus', 'type in ["milestone"]'),
        ('planguage', 'type not in ["milestone"]')
    ]
}

needs_build_json = True

needs_id_regex = "^([A-Za-z]+)(_[A-Za-z]+)*"
needs_id_required = True
needs_title_optional = False

needs_role_need_template = "{id} ({title})"

needs_warnings = {
    "missing_source": "not source",
    "missing_owner": "not owner",
    "missing_author": "not author",
}

needs_css = "blank.css"
needs_layouts = {
    'planguage': {
        'grid': 'complex',
        'layout': {
            'head_right': [
                '<<collapse_button(target="content", collapsed="-Text", visible="+Text", initial="True")>>',
                '<<collapse_button(target="footer", collapsed="-Meta", visible="+Meta", initial="True")>>',
            ],
            'head': [
                '<<meta("full_title")>>',
            ],
            'footer': [
                '<<meta_all(exclude=["pre_template", "template", "layout", "notes", "qualifiers", "qualities", "functions", "related", "design_constraints", "tests", "rationale", "issues", "priority", "design_ideas"])>>'
            ]
        }
    }
}
needs_default_layout = 'planguage'
needs_default_style = 'clean'

jira_base_url = 'https://jira.mycorp.com/browse/'
test_results_url_format_string = 'https://bamboo.mycorp.com/browse/AUTOTEST/latest/artifact/JOB1/Results.html#?pretendFilter=tags:%s'
