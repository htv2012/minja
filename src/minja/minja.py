"""
Implement a simple template rendering because the default string.Template in
Python versions prior to 3.11 is did not provide a way to get the names of the
variables.  The name `minja` means to be a mini jinja engine.
"""

import re
from typing import Optional

__all__ = ["Template"]


NAME_PATTERN = re.compile(
    r"""
    {{                 # openning double braces
    \s*                # any number of white spaces
    (                  # begin group
        [a-zA-Z_]      # first char of variable
        [a-zA-Z0-9_]*  # subsequent chars
    )                  # end group
    \s*                # any number of white spaces
    }}                 # closing double braces
    """,
    re.VERBOSE,
)


def _create_replace_function(mapping: dict):
    def replace(match: re.Match):
        key = match[1]
        return str(mapping[key])

    return replace


class Template:
    """A simple Jinja-like template rendering class."""

    def __init__(self, text: Optional[str] = ""):
        self.text = text

    @property
    def names(self):
        return set(NAME_PATTERN.findall(self.text))

    def render(self, **kwargs):
        return NAME_PATTERN.sub(_create_replace_function(kwargs), self.text)
