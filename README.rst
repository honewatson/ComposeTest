===============================
Compose Test Generator
===============================


.. image:: https://img.shields.io/pypi/v/compose_test_generator.svg
        :target: https://pypi.python.org/pypi/compose_test_generator

.. image:: https://img.shields.io/travis/honewatosn/compose_test_generator.svg
        :target: https://travis-ci.org/honewatosn/compose_test_generator

.. image:: https://readthedocs.org/projects/compose-test-generator/badge/?version=latest
        :target: https://compose-test-generator.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/honewatosn/compose_test_generator/shield.svg
     :target: https://pyup.io/repos/github/honewatosn/compose_test_generator/
     :alt: Updates


Generates Composable Function(s) and Tests From Yaml


* Free software: BSD license
* Documentation: https://compose-test-generator.readthedocs.io.


Features
--------

Create a yaml file called example.yaml with function names and docs.

     .. code-block:: yaml

          config:
               parameter_name: obj
          newObj:
               doc: Creates a copy of the passed in object
          addCarValue:
               doc: Adds a car value to the Object

Run the command composet against the example.yaml file with the language output.

     .. code-block:: bash

          composet python example.yaml

From here composet will generate a module with functions, docs, and tests.

- example/__init__.py
- example/example.py
- tests/test_example.py

     .. code-block:: python

          import toolz

          def newObj(obj):
               """Creates a copy of the passed in object"""         
               pass
         
          def addCarValue(obj):
               """Adds a car value to the Object"""
               pass

          main = toolz.compose(addCarValue, newObj)


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

