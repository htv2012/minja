"""
Test the Template class.
"""

import pytest

from minja import Template


@pytest.fixture
def template_text():
    return "{{ flowers }} are {{ color }}"


@pytest.fixture
def flowers_template():
    return Template(template_text)


def test_simple(flowers_template):
    assert flowers_template.render(color="red", flowers="Roses") == "Roses are red"


def test_load_text_should_set_names(flowers_template):
    assert flowers_template.names == {"flowers", "color"}


def test_no_duplicate_names():
    """Names should be a set, hence no duplicates."""
    template = Template("{{ a }}, {{ b }}, {{ a }}")
    assert template.names == {"a", "b"}


def test_ignore_spaces_inside_braces():
    """Ensure {{foo}} and {{ foo }} are the same."""
    template = Template("{{foo}},{{ foo }}")
    assert template.render(foo="bar") == "bar,bar"


def test_single_char():
    """Single-char variable such as {{a}}, {{b}}."""
    template = Template("Hello, {{w}}")
    assert template.render(w="world") == "Hello, world"


def test_render_without_key(flowers_template):
    with pytest.raises(KeyError, match="flowers"):
        flowers_template.render()


def test_template_without_braces():
    """Test a template which has no braces."""
    template = Template("Hello, world")
    assert template.render() == "Hello, world"


def test_render_multiple_times(flowers_template):
    """Ensure that expansion works many time."""
    assert flowers_template.render(flowers="Roses", color="red") == "Roses are red"

    with pytest.raises(KeyError, match="color"):
        flowers_template.render(flowers="Violet")


def test_empty_braces():
    """Test empty braces."""
    template = Template("{{}}")
    assert template.render(foo="bar") == "{{}}"


def test_render_non_string():
    """Render other types of data, not just string."""
    template = Template("{{bool_var}}, {{int_var}}")
    assert template.render(bool_var=True, int_var=19) == "True, 19"


def test_update_text():
    """Update text and the names should be updated as well."""
    template = Template("Hello {{ person }}")
    assert template.names == {"person"}

    template.text = "{{ flowers }} are {{ color }}"
    assert template.names == {"flowers", "color"}
