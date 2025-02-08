"""
Simple usage
"""

from minja import Template


def main():
    """Entry"""
    template = Template("{{ flowers }} are {{ color }}")
    print(template.render(flowers="Roses", color="red"))
    # Roses are red


if __name__ == "__main__":
    main()
