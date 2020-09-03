# Python Documentation

Python documentation can use different formats: Google docstrings, reStructured Text, and NumPy/SciPy docstrings. [Examples can be found here.](https://realpython.com/documenting-python-code/#docstring-formats)

## Sphinx

```bash
pip3 install -r requirements.txt
sphinx-build -b html . docs/sphinx
```

The generated files will be found in the `docs/sphinx` directory.

More info: https://www.sphinx-doc.org/en/master/

## Pycco

```bash
pip3 install -r requirements.txt
pycco *.py
```

The generated files will be found in the `docs/` directory.

More info: https://pycco-docs.github.io/pycco/
