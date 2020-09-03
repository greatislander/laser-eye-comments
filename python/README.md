# Python Documentation

Python documentation can use different formats: Google docstrings, reStructured Text, and NumPy/SciPy docstrings. [Examples can be found here.](https://realpython.com/documenting-python-code/#docstring-formats)

You can display basic info about a Python function using `help()`:

```bash
python3
>>> from laser_eye_comments import convert_to_morse_code
>>> help(convert_to_morse_code)
```

This will display the following:

```python
Help on function convert_to_morse_code in module laser_eye_comments:

convert_to_morse_code(str: str)
    Converts a string to Morse Code.

    Parameters
    ----------
    str : str
        The string to be converted to Morse Code.

    Returns
    -------
    str
        The string as Morse Code.
```

## Sphinx

```bash
pip3 install -r requirements.txt
sphinx-build -b html . docs/sphinx
```

The generated files will be found in the `docs/sphinx` directory.

More info: [Sphinx](https://www.sphinx-doc.org/en/master/)

## Pycco

```bash
pip3 install -r requirements.txt
pycco *.py
```

The generated files will be found in the `docs/` directory.

More info: [Pycco](https://pycco-docs.github.io/pycco/)
