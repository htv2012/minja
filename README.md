# minja
A Mini Jinja Template Engine

I am creating this package because I need something like Jinja, but in
a much smaller footprint.

# Install

    pip install minja

# Usage

## A Simple Usage

```python
from minja import Template

template = Template("{{ flowers }} are {{ color }}")
print(template.render(flowers="Roses", color="red"))
# Roses are red
```

## What Is a Template?

A template is a string embedded variables. For example, the template in
previous example has two variables, `flowers` and `color`.

Note that the spaces surrounding the variables are insignificant: they
are there to improve readability. That means the following will render
to the same text:

```python
t1 = Template(">{{name}}<")
t2 = Template(">{{ name }}<")
t3 = Template(">{{     name     }}<")

print(t1.render(name="Anna"))  # '>Anna<'
print(t2.render(name="Anna"))  # '>Anna<'
print(t3.render(name="Anna"))  # '>Anna<'
```

## How Can I Get the Names of the Variables?

A template maintains a property called `.names` which keep track of the
names of the variables.

```python
template = Template("{{ flowers }} are {{ color }}")
print(template.names)  # {'flowers', 'color'}
```

