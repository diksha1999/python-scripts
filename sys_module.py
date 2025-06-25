import sys

# The sys module provides access to system-specific parameters and functions. 
# Besides sys.argv (for command-line arguments), sys.platform (to get OS type), and sys.exit() (to exit the script)

print(sys.path)
# `sys.path` is a built-in list in Python that tells the interpreter where to look for modules to import.
# It’s part of the `sys` module, which provides access to some variables and functions related to the Python interpreter.


# How Does `sys.path` Work?
# When you run `import some_module` in Python, the interpreter searches for `some_module` in the directories listed in `sys.path`.
# It checks each directory in order until it finds the module or raises an `ImportError`

print(f"This is the python interpretor version: {sys.version}")

print(f"Tuple containing the five components of the version number: major, minor, micro, releaselevel, serial: {sys.version_info}")

print(f"A string giving the absolute path of the Python Interpretor executable binary: {sys.executable}")

# These are file objects representing standard input, standard output, and standard error streams.

# print() writes to sys.stdout by default. input() reads from sys.stdin. Error messages from
#  the interpreter often go to sys.stderr. You can redirect these if you need to for advanced I/O operations.

