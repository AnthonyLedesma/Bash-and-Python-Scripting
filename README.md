# Scripting Repository Reference
Click Options To Jump To Topic

## [Bash](#bash) 

[Bash Script Order](#bash.order)

[Bash If Statement](#bash.if)

[Bash Loops](#bash.loops)

[Bash Case Statement](#bash.case)

[Bash Script Input](#bash.input)

[Bash Find](#bash.find)

[Bash Example Script - MP3 Processor](#bash.example1)



## [Python](#python)

[Python Input/Outout](#python.inout)


# <a name="bash"></a>Bash Scriping Reference

<a name="bash.order">Shell Script Order and Checklist
```bash
1. Shebang (#!/usr/bin/env bash)
2. Comments /file header
3. Global variables
4. Functions
--Use local vairables
5. Main script contents
6. Exit with an exit status.
--Exit <STATUS> at various exit points

```

### <a name="bash.if"></a>[IF Statement](https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php)
```bash
#!/usr/bin/env bash
# Basic if statement
if [ $1 -gt 100 ]
  then
  echo Hey that\'s a large number.
  pwd
fi
date
```

### <a name="bash.loops"></a>[For, While, Until](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html)
```bash
#!/usr/bin/env bash
#For Loop
for i in $( ls ); do
  echo item: $i
done

#!/usr/bin/env bash
#While Loop
COUNTER=0
while [  $COUNTER -lt 10 ]; do
  echo The counter is $COUNTER
  let COUNTER=COUNTER+1 
done

#!/usr/bin/env bash
#Until Loop
COUNTER=20
until [  $COUNTER -lt 10 ]; do
  echo COUNTER $COUNTER
  let COUNTER-=1
done
```

## AWK
```bash
$ ifconfig lo | awk -F" " '/TX/{ print toupper($3 $4 $5 $6 $7) }'
77BYTES6543(6.5KB)
0DROPPED0OVERRUNS0
```
- `-F` => Flag to specify text delmiter
- `/*/` => Create regex match
- `{ print toupper($0) }` => Awk commands 

```bash
$ awk -F"," ' BEGIN {OFS=" => "} {  print toupper($1), tolower($2), $3 } END { print "Rows: " NR }' employees
```
- `-F","` - Sets input field seperator
- `OFS=" => "` - Sets the default field seperator for output
- ` BEGIN ... END ` - Expression runs a start, end once and containing commands once for each matching input
- `$1, $2, $3` - Variables indicating field one, two, and three.
- `NR` - Variable containing row count for document.

### AWK example
#### 40K lines + access log - Using AWK to parse
##### access.awk
```bash 
BEGIN { FS=" "; print "Unknown status codes:"; }
{ if($9 == "404") FOF++}
{ if($9 == "200") TOO++}
{ if($9 == "206") TOX++}
{ if($9 == "500") FOO++}
{ if($9 == "304") TOF++}
{ if($9 == "301") TON++}
{ ip[$1]++ }
{ if( $9 != "404" && $9 != "200" && $9 != "304" && $9 != "301" && $9 != "206" && $9 != "500" ) \
printf "%-4s\n",$9}
END {
printf "\nKnown status code occurrences:\n\
200: %-5s\n\
206: %-5s\n\
301: %-5s\n\
304: %-5s\n\
404: %-5s\n\
500: %-5s\n\
Together that is %-5s codes\n\
Document contains %-5s codes leaving %s unknown codes\n\
\n\
Highest frequency access: (> 400)\n"\
, TOO, TOX, TON, TOF, FOF, FOO, ( FOF + TOO + TOF + TON + FOO + TOX), NR, (NR - (FOF + TOO + TOF + TON + FOO + TOX));

for (i in ip)
{if(ip[i] >= 400) printf "%-15s has accessed %-5s times.\n", i, ip[i]}
}
```
- `{ if(EXPRESSIONS) CMD; }` 
  * If statment expressions contained in curly braces
- `{ ip[$1]++ }` 
  * Setting key for associative array as the value of field one, then incrementing the key value using `++`
- ` printf "%-5s: %-10s", value1, value2; `
  * Formatted print `%-5s` string with 5 characters & `%-10s` string with 10 characters
  * Values passed after comma
- `for (i in ip)...` 
  * Nested for loop to iterate over associative array

#### Output
```bash
Unknown status codes:
405 
405 
405 
405 
405 
501 
405 

Known status code occurrences:
200: 39755
206: 21   
301: 85   
304: 725  
404: 3772 
500: 14   
Together that is 44372 codes
Document contains 44379 codes leaving 7 unknown codes

Highest frequency access: (> 400)
213.150.254.81  has accessed 434   times.
205.167.170.15  has accessed 13967 times.
37.1.206.196    has accessed 438   times.
84.112.161.41   has accessed 712   times.
148.251.50.49   has accessed 1929  times.
52.22.118.215   has accessed 734   times.
```

#### catalog xml awk parse
```bash
$ awk 'BEGIN { FS="[<>]"; RS="\n\n"; OFS=" "} $0 ~ search  {print $4 ": " $5, $8 ": " $9, $12 ": " $13 }' search="screw driver" catalog.xml
```
- `' '` - use half quote to begin awk command logic
- `FS, RS and OFS` - Field seperator, Row seperator, and Output field seperator.
- `$0` - Matched row
- `~` - Initiates regex match on following token
- `search` - This is an `awk` variable
#### output
```bash
name: screw driver price: 10 stock: 200
```


#### users.awk
```bash
BEGIN {
	printf "%8s %11s\n","Username", "Login date"
	print "==========================="
}
!(/Never logged in/ || /^Username/ || /^root/) {
	count++
	if( NF == 8 )
		printf "%16s %2s %3s %4s\n", $1, $2, $3, $4
	else
		printf "%16s %2s %3s %4s\n", $1, $2, $3, $4
}
END { 
	print "==========================="
print " Total Number of Users Processed: ", count
}
```
#### termnial
```bash
$ lastlog | awk -f users.awk
```

## SED
### Using sed commands
- `$ sed ' p ' /etc/passwd`
  * The command `p` will print the patter space (matched lines)
- `$ sed -n ' p ' /etc/passwd`
  * The `-n` option supresses standard outpit so only matched lines display
- `$ sed -n '1,$ p ' /etc/passwd`
  * adding a `range` will print only those matched lines 
  * `$` character represents end of document
- `$ sudo sed -i.bak ' /^#/ d ; /^$/ d' /etc/debconf.conf`
  * `/*/ d ;` => Regex Match (`d` flag to delete match)
  * `-i[suffex]` => Flag to in-place edit, suffix to create backup of original with sufix appended
- `$ sed ' [range] s/<string>/<replacement>/ ' /etc/passwd`
- `$ sed -n ' /^#!/ s@/bin/bash@/binsh@g p' /~/script.sh` 
  * The substitute command in sed is your `search and replace` tool
  * The character following the `s` represents the delimiters, often the `/` is used
  * the `@` is a delimiter as in the example
  * `^` prefix matches beginning of string
  * `/ /` characters contain the regular expression
  * `p` to print the output of sed
- `$ sed ' /\.dat$/ d' /etc/debconf.conf`
  * Delete the matched line
- `$ sed ' /^Template/ i # Here is a comment' /etc/debconf.conf`
  * Insert new line before the matched line
- `sed ' /^Template/ a # Here is a comment' /etc/debconf.conf`
  * Appends a new line after the matched line
- `$ sed ' { /^[F,f]ilename:/ i # The following line is the filename /^[D,d]river:/ d } ' /etc/debconf.conf`
  * Multiple `expressions` may be used with sed by including brace brackets within the quoted sed instructions

### SED Substitution Groups
```bash
$ sed ' s@\([^,]*\),\([^,]*\)@\U\1,\L\2@ ' employees
```
`s@`
- Substitution

`\([^,]*\),\([^,]*\)`
- Grouping defined with escaped parentheses
- Group `1` and `2` are created

`@\U\1,\L\2/@`
- Replace string: upper cases first grouping
- Insert comma and transform lowercase group two

### SED and SSH
```bash
$ ssh -t user@server sudo -i.bak -f /tmp/ntp.sed
```
- `-t` - Assigns a TTY allowing for sudo password
- `-i.bak` - creates backup with `.bak` extension
- `-f /tmp/ntp.sed` - Sed file on remote server

### sed - Code reuse
```javascript
$ cat ntp.sed
/^server 0/ i ntp.example.com
/^server\s[0-9]\.ubuntu/ d
$ sed -f ntp.sed /etc/ntp.conf
```
  * To resuse sed expressions, use sed files
  * The sed file can be referenced with the `-f` option
  * Once we check the file behaves as expected we can implement the `-i` option

## SCP
```bash 
$ scp ntp.sed user@192.168.1.1:/tmp/
```
- Secure copy
  * `ntp.sed` - local path
  * `:/tmp/` - remote path

## GREP
```bash
paranoia@paranoia:~$ cat /proc/cpuinfo | grep -iA4 Name
model name	: Intel(R) Core(TM) i5-4590T CPU @ 2.00GHz
stepping	: 3
cpu MHz		: 1995.388
cache size	: 6144 KB
physical id	: 0
```
- `i` - Case insensitve
- `A#` - Display match + '#' amount of lines after match
- `B#` - Display '#' lines before match
- `C#` - Display '#' lines before and after match

```bash
grep 'rotate [^4]$' /etc/logrotate.d/*
```
- `[^4]` - Carret character negates the following character from the match
- `[]$` - Dollar symbox suffix enforces match on end characters of string

```bash
grep -E 'rotate [46]$' /etc/logrotate.d/*
```
- `[46]` - Matches 4 or 6
- `[]$` - Dollar symbol suffix enforces match on charactes at end of string
- `-E` - Extended regular expression



## REGEX - Regular Expressions
```perl
A*?+{1}.{1,3}[0-0]*
```
- 

```
\b[Cc]olou?r\b
```
- Matches the words Color, Colour, color, or colour
- `?` - 0 or 1 matches of preceeding character.
- 

### Anchors
- `'^' `
  * Start/beginning of string
- `'^root'`
  * String starts with `root`
- `'$'`
  * End of string
- `'4$'`
  * String ends with 4

### Ranges
- `'[A-Za-z]'`
  * any letter
- `'[0-9]'`
  * Any digit
- `'[a-z_]'`
  * Lowercase a-z or underscore character
- `'[349]'`
  * Matches 3, 4, or 9

### Boundaries
- `'\s'`
  * Whitespace
- `'\ssystem'`
  * Matches "file system"
- `'\b'`
  * Word boundary
- `'\bsystem'`
  * Matches "file system" and "file-system"

### Quanitifiers
- `'u*'`
  * Matches `u` zero or more times
- `'u?'`
  * Matches `u` zero or once only (optional)
- `'u+'`
  * Matches one or more occurrences of `u`
- `'u{3}'`
  * Matches exactly three occurrences: `uuu`






### <a name="bash.find"></a>[Find Command](http://man7.org/linux/man-pages/man1/find.1.html)
```bash
#This command will find only file with names ending with .mp3 within the current directory 
#-execdir to execute rm command on each item. -exec & -execdir replace {} with each item returned.
#"{}" should be quoted if find is being invoked from a shell.  
#This a much more secure method for invoking commands, as it avoids race conditions during resolution of 
#the paths to the matched files.
find ./ -type f -name "*.mp3" -execdir rm "{}" \;
```

### <a name="bash.input"></a>[User Input](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php)
```bash
OLD_DIR=$(pwd)
echo "Please enter the file extension to search for";
read EXTENSION;
echo "The extension given was: $EXTENSION"; 

echo "Please enter the directory to search(Press enter to select pwd)";
read DIRECTORY;
if [ -z "$DIRECTORY" ]
then
	DIRECTORY=$(pwd);
	echo "Searching for directory $DIRECTORY";
else
	echo "Searching for directory $DIRECTORY";
fi
if [ -d "$DIRECTORY" ]
then
	echo "Directory found. Moving to $DIRECTORY";
	PROCEED="y";
else
	echo "No matching path was found."
	echo "pwd : $(pwd)";
	echo "Do you want to switch to pwd? (y/n)";
	read PROCEED;
	[ "$PROCEED" == "y" ] && DIRECTORY=$(pwd);
fi
if [ "$PROCEED" == "y" ]
then	
	cd "$DIRECTORY";
	echo "Working in $(pwd)";
else
	echo "Opperation aborted";
	exit 1;
fi
#Code continued
```

### <a name="bash.case"></a>[Case Statements](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html)
```bash
#!/usr/bin/env bash
#Select an option to run commands.
EXIT=false;
while [ "$EXIT" == "false"  ]; do
	echo "Select the option that you want";
	echo "1. Show disk usage.";
	echo "2. Show system uptime";
	echo "3. Show current users logged into the system";
	echo "Enter 'q' to quit the script";
	read SELECTION

	case "$SELECTION" in
		1)
		df;
		;;
		2)
		uptime;
		;;
		3)
		who;
		;;
		q)
		echo "Goodbye";
		EXIT=true;
		;;
		*)
		echo "Invalid option";
		;;
	esac
done
```

### <a name="bash.example1"></a>[mp3_processor](https://github.com/paranoia1906/.bashrc/blob/master/mp3s/mp3_processor)
```bash
#!/usr/bin/env bash
#Set return strings
NO_DIR_ARG="Passed argument is not a directory"
NO_ARG="No directory given. Defaulting to pwd: $(pwd)"
YES_DIR="Directory detected: $1"

#Safely return to origination directory
DIR=$(pwd) 
#Ensure that argument passed is a dir and not a file otherwise exit
[ $# -gt 0 ] && [ -f $1 ] && echo "$NO_DIR" && exit 2
#set working dir using DIR var to either pwd or the argument if applicapable
[ $# -eq 0 ] && DIR=$(pwd) && echo "$NO_ARG" || DIR=$1 && echo "$YES_DIR"
#Make sure that var DIR matches type directory before we cd, otherwise we exit
[ -d "$DIR" ] && cd "$DIR" || exit 1

#setting nullglob on for *.mp3 detection prior to action
shopt -s nullglob
found=0

#check that files exist and set var found if so
for i in *.mp3; do
  echo "file $i found" 
	found=1
done
shopt -u nullglob
[ $found -eq 0 ] && echo "Directory is empty"

#If something was found during nullglob check then we can proceed with the rest of the script logic.
if(( "$found" > "0"))
then
#List all files in directory and act on each
	for i in $(ls); do
#Use PCRE case insensitive regex to make sure each item matches *.mp3 format
		if( ls $i | grep "(.mp3){1}" -Pi )
		then
#Move/rename file to include formatted date concatenated with the current filename
			mv $i "$(date +%F)-$i"
			echo "Transformed item: $i into => '$(date +%F)-$i'"	
		fi
	done
fi

cd "$DIR"
#Done with opperation
```

# <a name="python"></a> Python Scriping Reference

### <a name="python.inout"></a>[Input/Output JSON](https://docs.python.org/3/tutorial/inputoutput.html)
```python
import json
with open('input.json', 'r') as input:
	obj = json.load(input)
	with open('output.txt', 'w') as output:
		output.write(obj['name'] + "'s Hobbies:\n")
		for hobby in obj['hobbies']:
			output.write(hobby + "\n")
```

# Python
- Extensible Design
- Community Involved Design
- Emphasizing Fun
- Culture


## __Python definitions__
- REPL - (Read, Eval, Print, Loop)
- Package - A module which can contain other modules
  * Packages are generally directories
- Module - A script/application which stands alone
  * Modules are generally files
- `sys.path` - List of directories Python searches for modules
- Absolute Imports - Imports which us a full path to the module. `from reader.reader import Reader`
- Relative Impoorts - Imports which use a relative path to modules in the same package `from .reader import Reader`
  * Can reduce typing in deeply nested package structures
  * Promote certain forms of modifiability
  * Can aid package renaming and refactoring
  * General advice is to avoid them in most cases
- `__all__` - List of attribute names imported via `from module import *`
- Namespace Packages - Packages wplit across several directories
  * Namespace packages have no `__init__.py`
  * This avoids complex initilization ordering problems
- Executable Directories - Directories containing an entry point for Python execution
- Executable Zip File - Zip file containing an entry point for Python execution
- `__call__()` - Special method - Callable instances
- Lambdas - Nameless function instanciators
  * Expression which evaluates to a function
  * Anonymous
  * Argument list terminated by colon, separated by commas
  * Can contain only a single expression - no statments
  * Lambdas cannot have docstrings
- `callable()` - Built in function
```python 
>>> def is_even(x):
...     return x%2 == 0
...
>>> callable(is_even)
True
>>> is_odd = lambda x: x%2 == 1
>>> callable(is_odd)
True
>>> callable(list)
True
>>> callable(list.append)
True
>>> class CallMe:
...     def __call__(self):
...             print("Called!")
...
>>> call_me = CallMe()
>>> callable(call_me)
True
>>> callable("This is not callable")
False  
```
- Extended Formal Argument Syntax 
  * ```def extended(*args, **kwargs):```
- Transposing Tables
  * using `list(zip(*args)` to transpose two-dimension tables of data
  * Converts rows to columns and vice-versa. 
  * Zip and __stargs__ (`*args`) are used in production enough to know what they are and how to spot
  * Used on an iterable series of iterable series
- `local functions` - Functions defined within the scope of other functions


## Local Functions 
```python
def func():
        def local_func():
                a = 'hello, '
                b = 'world'
                return a + b
        x = 1
        y = 2
        return x + y
```



## Recomended Project structure
```javascript
project_name
|-> __main__.py
|-> project_name
|   |-> __init__.py
|   |-> more_source.py
|   |-> subpackage1
|   |   |-> __init__.py
|   |-> test
|       |-> __init__.py
|-> setup.py
```

- Pip
  * 3rd Party Libraries
  * Install/Uninstall/Dependencies/Package Groups/Versions
  * Install PIP
```bash
$ curl https://bootstrap.pypa.io/get-pip.py | python
```
- ipython
  * Robust interactive CLI utility



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


## Debugging in Python
PDB
- The Python DeBugger
  * `import pdb`
  * `pdb.set_trace()`

## distutils - `setup.py`
```python
from distutils.core import setup

setup(
        name = 'palindrome',
        version = '1.0',
        py_modules = ['palindrome'],

        # metadata
        author = 'Anthony Ledesma',
        author_email = 'anthonymledesma@gmail.com',
        description = 'A module for finding palindromic integers.',
        license = 'Public domain',
        keywords = 'example',
)
```


## Shipping Working and Maintainable Code
- `unittest` is a framework for developing reliable automated tests
- You define `test cases` by subclassing from `unittest.TestCase`
- `unittest.main()` is useful for running all of the tests in a module
- `setUp()` and `tearDown()` run code before and after each test method
- Test methods are defined by creating method names that start with `test_`
- `TestCAse.assert...` methods make a test method fail when the right conditions aren't met
- Use `TestCase.assertRaises()` in a with-statement to check that the right exceptions are thrown in a test
- Python's standard debugger is called `PDB`
- `PDB` is a standard command-line debugger
- `pdb.set_trace()` can be used to stop program execution and enter the debugger
- Your REPL's prompt will change to (pdb) when you're in the debugger
- You can access PDB's built-in help system by typing `help`
- Use `python -m pdb <script-name>` to run a program under PDB from the start
- PDB's `where` command shows the current call stack
- PDB's `next` command lets execution continue to the next line of code
- PDB's `continue` command lets program execution continue indefinitely, or until you stop it with `ctrl + c` 
- PDB's `list` command shows you the source code at your current location
- PDB's `return` command resumes execution until the end of the current function
- PDB's `print` command lets you see the values of objects in the debugger
- Use `quit` to exit PDB
- Virtual environments are light-weight, self-contained Python installations that any user can create
- `venv` accepts both a source-installation argument as well as a directory name into which a new environment will be created
- To use a virtual environment, you need to run its `activate` script
- When you activate a virtual environment, your prompt is modified to remind you
- The `distutils` package is used to help you distribute your Python code
- `distutils` is generally used inside a `setup.py` script which users run to install your software
- The main function in `distutils` is `setup()`
- `setup()` takes a number of arguments describing both the source files as well as metadata for the code
- The most common way to use `setup.py` is to install code using `python setup.py install`
- `setup.py` can also be used to generate distributions of your code
- Distributions can be zip files, tarballs, or several other formats
- Pass `--help` to see all of its options
- Common tools for installing third-party software are `distutils` and `pip`
- The central repository for Python packages is the Python Package Index, also called PyPi or "cheeseshop"
- To install modules with `pip`, use the subcommand notation `pip install package-name`
- `divmod()` calculates to quotient and remainder for a devision operation at one time
- `reversed` function can reverse a sequence
- You can pass `-m` to your Python command to have it run a module as a script
- Debugging makes it clear that Python is evaluating everything at run time
- You can use the `__file__` attribute on a module to find out where its source file is located
- Third-party python is generally installed into your installations's `site-packages` directory
- `nose` is a useful tool for working with `unittest` based tests

## Packages
- Packages are modules that contain other modules
- Packages are generally implemented as directores containing a special `__init__.py` file
- The `__init__.py` file is executred when the package is imported
- Packages can contain sub packages which themselves are implemented with `__init__.py` files in directories

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
