# Python

-Exstensible Design

-Community Involved Design

-Emphasizing Fun

-Culture


### Working With Python
#### Python

Executing python file

Rudimentary REPL (Read, Eval, Print, Loop)

#### Pip

3rd Party Libraries

#### ipython

Robust interactive CLI utility

### What is PIP
Install

Uninstall

Dependencies

Package Groups

Versions

### Installing with PIP
#### Install PIP
```bash
$ curl https://bootstrap.pypa.io/get-pip.py | python
```


#### Install SomePackage with PIP
```bash
$ pip install SomePackage
```

### Python 2 Vs Python 3
#### Executable Comparison
| Python 2 | Python 3 |
| -------  |:--------:|
| pip      | pip3     |
| python   | python3  |
| ipython  | ipython3 |

### Which should you choose?
:heavy_check_mark: Default to Python 3 when possible 

:x: Python 2.x is legacy


### Executing Python Code
1. Interpreter

Executing python file using python.exe

2. REPL

Call out to python code within interactive REPL

3. Natively

 "Compile and Run" (py2exe, pyinstaller, etc.)


### Python Modularity Key Facts
- Python code is placed in *.py files called "modules"
- Modules can be executed directly with ```python python3 module_name.py```
- Brought into the REPL or other modules with ```python import module_name```
- Named functions defined with the def keyword ```python def function_name(arg1, argn): ```
- Return from frunctions using ```python return``` keyword with optional parameter
- Omitted return parameter or implicit return at end returns ```python None```
- Use ```__name__``` to determine how the module is being used 
- If ```__name == "__main__"``` the module is being executed
- Command line arguments are accessible through ```python sys.argv```
- The script filename is in ```python sys.argv[0]```
- Docstrings are standalone literal string as the first statment of a function or a module 
- Docstrings are delimited by tripple quotes
- Docstrings provide ```python help()```
- Module docstrings should precede other statements
- Comments begin with # and run to the end of the line
- A special comment on the first line beginning #! controls module execution by the program loader


## Objects - Summary
- Think of named references to objects rather then variables
  * Assignment attaches a name to an object
  * Assigning from one reference to another puts two name tags on the same object
- The garbage collector reclaims unreachable objects
- `id()` returns a unique and constant identifier
  * Rarely used in production
- The `is` operator determines equality of identity 
- Test for equivalence using `==`
- Function arguments are passed by object-reference
  * Functions can modify mutable arguments
- Reference is lost if a formal function argument is rebound
  * To change a mutable argument, replace its contents
- `return` also passes by object-reference
- Function arguments can be specified with defaults
- Default argument expressions evaluated once, when `def` is executed 
- Python uses dynamic typing
  * We don't specify types in advance
- Python uses strong typing
  * Types are not coerced to match
- Names are looked up in four nested scopes
  * LEGB rule: Local, Enclosing, Global, and Built-ins
- Global references can be read from a local scope
- Use `global` to assign to global references from a local scope
- Everything in Python is an object
  * This includes modules and functions
  * They can be treated just like other objects
- `import` and `def` result in binding to named references
- `type` can be used to determine the type of an object
- `dir()` can be used to introspect an object and get its attributes.
- The name of a function or module object can be accessed through its `__name__` attribute
- The docstring for a function or module object can be accessed through its `__doc__` attribute
- Use `len()` to measure the length of a string
- You can multiply a string by an integer
  * Productes a new string with multiple copies of the operand
  * this is called the "repetition" operation

## Collections - A Few Types
- `tuple` - Heterogeneous immutable sequences
- `str` - Homogeneous immutable sequence of Unicode codepoints (characters)
- `range` - Arithmetic progression of integers
- `list` - Heterogeneous mutable sequence
- `dict` - Unordered mapping from unique, immutable keys to mutable values
- `set` - Unordered collection of unique, immutable objects

#### Collection Protocols
| Protocol | Implementing Collections |
| -------- |:--------:|
| Container | str, list, range, tuple, bytes, set, dict |
| Sized | str, list, range, tuple, bytes, set, dict  |
| Iterable | str, list, range, tuple, bytes, set, dict |
| Sequence | str, list, range, tuple, bytes |
| Mutable Sequence | list |
| Mutable Set | set |
| Mutable Mapping | dict |

## A Few Things To Avoid
1. Abusing `range()`
  * Avoid `range()` for iterating over lists
  * Python is not C
  * Don't be un-pythonic!
- Prefer direct iteration over iterable objects such as lists

2. Do not use `range()`
  * prefer `enumerate()` for counters 




## Script Reloading Example for REPL Using importLib
In this example we utilize the 'importlib' module's reload function to refresh the python script for REPL to use 

#### hello_world.py - Created
```python
def sayHello():
        print("Hello, Functions!")
```

#### Bash to execute python3
```bash
$ python3
```

#### Python REPL
```python
>>> import hello_world
>>> hello_world.sayHello()
Hello, Functions!
```

#### hello_world.py - Edited
```python
def sayHello():
        print("Hello, Again!")
```

#### Python REPL
```python
>>> hello_world.sayHello()
Hello, Functions!
>>> import importlib
>>> importlib.reload(hello_world)
<module 'hello_world' from '/home/paranoia/development/scripting/python/hello_world/hello_world.py'>
>>> hello_world.sayHello()
Hello, Again!
```


## Example Using Autoreload with iPython
This example hotloads a python script after file changes. This is done using iPython3 utility and the extension 'autoreload'
#### hello_world.py - Created
```python
def sayHello():
        print("Hello, Again!")
```

#### iPython3 REPL
```bash
$ ipython3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
```

#### iPython3 REPL
```python
In [1]: %load_ext autoreload

In [2]: %autoreload 2

In [3]: from hello_world import sayHello

In [4]: sayHello()
Hello, Again!
```

#### hello_world.py - Edited
```python
def sayHello():
        print("Hello, Once More!")
```

#### iPython3 REPL
```python
In [5]: sayHello()
Hello, Once More!
```