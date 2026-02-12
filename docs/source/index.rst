.. minja documentation master file, created by
   sphinx-quickstart on Sun May 25 10:32:05 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

minja - A Mini Jinja Template Engine
====================================

I am creating this package because I need something like Jinja, but in
a much smaller footprint.


Install
-------

.. code-block:: bash

    pip install minja


A Simple Usage
--------------

.. code-block:: python

    from minja import render

    template = "{{ flowers }} are {{ color }}"
    print(render(template, flowers="Roses", color="red")
    # Roses are red

That code was the same as:

.. code-block:: python

    from minja import Template

    template = Template("{{ flowers }} are {{ color }}")
    print(template.render(flowers="Roses", color="red"))
    # Roses are red


What Is a Template?
-------------------

A template is a string embedded variables. For example, the template in
the previous example has two variables, flowers and color.

Note that the spaces surrounding the variables are insignificant: they
are there to improve readability. That means the following will render
to the same text:

.. code-block:: python

    t1 = Template(">{{name}}<")
    t2 = Template(">{{ name }}<")
    t3 = Template(">{{      name     }}<")

    print(t1.render(name="Anna"))  # '>Anna<'
    print(t2.render(name="Anna"))  # '>Anna<'
    print(t3.render(name="Anna"))  # '>Anna<'


How Can I Get the Names of the Variables?
-----------------------------------------

A template maintains a property called .names which keeps track of the
names of the variables.

.. code-block:: python

    template = Template("{{ flowers }} are {{ color }}")
    print(template.names)  # {'flowers', 'color'}


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
