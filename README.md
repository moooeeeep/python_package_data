
## A python package with associated data files

### Steps to reproduce:

Clone the package and change to package directory.

Create a virtual environment to install the package and upgrade pip in the virtual environment.

    python3 -m venv virtual_env
    source virtual_env/bin/activate
    pip install --upgrade pip

Install the package.

    pip install .

Access the file contents:

    import pkgutil
    print(pkgutil.get_data("foo_pkg", "data/my_file.txt").decode("utf-8"))

Should print:

    Hello World

For reference:

* https://setuptools.pypa.io/en/latest/userguide/datafiles.html
* https://docs.python.org/3/library/pkgutil.html#pkgutil.get_data
