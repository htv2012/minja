"""
Implement a simple template rendering because the default `string.Template` in
Python versions prior to 3.11 is did not provide a way to get the names of the
variables.  The name `minja` means to be a mini jinja engine.
"""

import re

__all__ = ["Template"]


NAME_PATTERN: re.Pattern = re.compile(
    r"""
    {{                 # opening double braces
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
    def replace(match: re.Match) -> str:
        key = match[1]
        return str(mapping[key])

    return replace


def render(text: str, **kwargs) -> str:
    """Render template text.

    :returns: The text with all names rendered.
    """
    sub_func = _create_replace_function(kwargs)
    return NAME_PATTERN.sub(sub_func, text)


class Template:
    """A simple Jinja-like template rendering class."""

    def __init__(self, text: str):
        self.text = text

    @property
    def names(self):
        """Return a list of names used in the template."""
        return set(NAME_PATTERN.findall(self.text))

    def render(self, **kwargs):
        """Renter the template into an actual string.

        :returns: The text with all names rendered.
        """
        return render(self.text, **kwargs)
