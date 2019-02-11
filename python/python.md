# Python

-Extensible Design

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
- Modules can be executed directly with ```python3 module_name.py```
- Brought into the REPL or other modules with ```import module_name```
- Named functions defined with the def keyword ```def function_name(arg1, argn): ```
- Return from functions using ```return``` keyword with optional parameter
- Omitted return parameter or implicit return at end returns ```None```
- Use ```__name__``` to determine how the module is being used 
- If ```__name == "__main__"``` the module is being executed
- Command line arguments are accessible through ```sys.argv```
- The script filename is in ` sys.argv[0]```
- Docstrings are standalone literal string as the first statement of a function or a module 
- Docstrings are delimited by triple quotes
- Docstrings provide ```help()```
- Module docstrings should precede other statements
- Comments begin with # and run to the end of the line
- A special comment on the first line beginning #! controls module execution by the program loader


## Objects - Summary
- Think of named references to objects rather than variables
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
  * Produces a new string with multiple copies of the operand
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

## Exception Handling
- Raising an exception interrupts normal program flow and transfers control to an exception handler
- Exception handlers defined using the `try...except` construct
- `try` blocks define a context for detecting exceptions
- Corresponding `except` blocks handle specific exception types
- Python uses exceptions pervasively
  * Many build-in language features depend on them
- `except` blocks can capture an exception, which are often a standard type
- Programmer errors should not normally be handled
- Exceptional conditions can be normally handled
- `raise` without an argument re-raises the current exception
- Generally do not check for `TypeErrors`
- Exception objects can be converted to strings using `str()`
- A function's exceptions form part of its API
  * They should be documented properly
- Prefer to use built-in exception types when possible
- Use the `try...finally` construct to preform cleanup actions
  * May be used in conjunction with `except` blocks
- Output of `print()` can be redirected using the optional `file` argument
- Use `and` and `or` for combining Boolean expressions
- Return codes are too easily ignored
- Platform-specific actions can be implemented using EAFP along with catching `importError`s


### Comprehensions, Generators and Iterables in Python
- Specify iterable sequences
  * All generators are iterators
- Are lazily evaluated
  * The next value in the sequence is computed on demand
- Can model infinite sequences
  * Such as data streams with no definite end
- Are composable into pipelines
  * For natural stream processing
- Comprehensions are concise syntax for describing lists, sets and dictionaries
- Comprehensions operate on an iterable source object and apply an optional predicate filter and a mandatory expression, both of which are usually in terms of the current item
- Iterables are objects over which we can iterate item by item
- We retrieve an iterator from an iterable object using the built-in `iter()` function
- Iterators produce items one-by-one from the underlying iterable series each time they are passed to the built-in next() function
- Generator functions allow us to describe series using imperative code
- Generator functions contain at least one use of the `yield` keyword.
- Generators are iterators. When advanced with `next()` the generator starts or resumes execution up to and including the next yield
- Each call to a generator function creates a new generator object.
- Generators can maintain explicit state in local variables between iteractions.
- Generators are lazy, and so can model infinite series of data.
- Generator expressions have a similar syntactic form to list comprehensions and allow for a more declarative and concise way of creating generator objects.
- Iteration tools - Built-ins
  * `sum()`
  * `any()`
  * `zip()`
  * `all()`
  * `min()`
  * `max()`
  * `enumerate()`
- Standard library itertools module
  * `chain()`
  * `islice()`
  * `count()`
  * many more!

### Classses in Python
- All types in Python have a `class`
- Classes define the structure and behavior of an object
- Class is determined when an object is created
  * Normally fixed for the lifetime
- Classes are the key support for Object-Oriented Programming in Python
- Classes defined using the `class` keyword followed by CamelCase name
- Class instances created by calling the calss as if it were a function
- Instance methods are functions defined inside the class
  * Should accept an object instance called `self` as the first parameter
- Methods are called using `instance.method()`
  * Syntactic sugar for passing self instance to method
- The optional `__init__()` method initialized new instances
  * If present, the constructor calls `__init__()`
  * `__init__()` is not the constructor
- Instance attributes are created simply by assigning to them
- Implementation details are denoted by a leading underscore
  * There are no public, protected or private access modifiers in Python
- Accessing implementation details can be very useful
  * Especially during development and debugging
- Class invariants should be established in the initializer
  * if the invariants can't be established raise exceptions to signal failure
- Methods can have docstrings, just like regular functions
- Classes can have docscrings
- Even within an object method calls must be preceeded with `self`
- You can have as many calsses and functions in a module as you wish
  * Related calsses and global functions are usually grouped together this way
- Polymorphism in Python is achieved through duc typing
- Polymorphism in Python does not use shared base classes or interfaces

### Exception Handling in Python
- Strings support slicing, because they implement the __sequence__ protocol
- Following the __Law of Demeter__ can reduce coupling
- We can nest comprehensions
- It can sometimes be useful to discard the current item in a comprehension
- When dealing with one-based collections it's often easier just to waste one list entry
- Don't feel compelled to use classes when a simple function will suffice
- Comprehensions or generator expressions can be split over multiple lines
- Statements can be split over multiple lines using backslash
  * Use this feature sparingly and only when it improves readability
- Use __Tell! Don't ask.__ to avoid tight coupling between objects

## Working with files
### `open()` modes
| Character | Meaning |
| -------- |:--------:|
| `r` | open for reading (default) |
| `w` | open for writing, truncating the file first |
| `x` | open for exclusive creation, failing if the file already exists|
| `a` | open for writing, appending to the end of the file if it exists |
| `b` | binary mode |
| `t` | text mode (default) |
| `+` | open a disk file for updating (reading and writing) |
| `u` | universal newlines mode (for backwards compatibility; should not be used in new code) |

### Files and Resource Mamanagement
- files are opened using the built-in `open()` function which accepts a file mode to control read/write/append behavior and whether the file is to be treated as raw binary or encoded text data
- For text data you should specify a text encoding
- Text files deal with string objects and preform universal newline translation and string encoding
- Binary files deal with `bytes` objects with no newline translation or encoding
- When writing files, its our responsibility to provide newline characters for line breaks
- Files should always be closed after use
- Files provide various line-oriented metgods for reading, and are also iterators which yield line by line
- Files are context managers and the with-statement can be used with context managers to ensure that clean up operations, such as closing files, are preformed
- The notion of file-like-objects is loosely defined, but very usefil in practice
  * Exercise EAFP to make the most of them. __Easier to Ask for Forgiveness than Permission__
- Context managers aren't restricted to file-like-objects. We can use tools in the `contextlib` standard library module such as the `closing()` wrapper to create our own context managers
- `help()` can be used on instance objects, not just types
- Python supports bitwise operators `&`, `|` and left `<<` and right shifts `>>` 

## Unittest - Automated and Repeatable
Key Concepts
- TestCase
  * Groups together related test functions
  * Basic unit of test organization in unittest
- fixtures
  * Code runs before and/or after each test function
- assertions
  * Specific tests for conditions and behaviors



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


## Example Using Auto reload with iPython
This example hot loads a python script after file changes. This is done using iPython3 utility and the extension 'autoreload'
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