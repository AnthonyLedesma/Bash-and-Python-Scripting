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
:heavy_check_mark: Default to Python 3 when possible. 

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
- Use ```__name__``` to determine how the module is being used.
- If ```__name == "__main__"``` the module is being executed.
- Command line arguments are accessible through ```python sys.argv```
- The script filename is in ```python sys.argv[0]```
- Docstrings are standalone literal string as the first statment of a function or a module 
- Docstrings are delimited by tripple quotes
- Docstrings provide ```python help()```
- Module docstrings should precede other statements
- Comments begin with # and run to the end of the line
- A special comment on the first line beginning #! controls module execution by the program loader.


## Script Reloading Example for REPL Using importLib
In this example we utilize the 'importlib' module's reload function to refresh the python script for REPL to use.
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