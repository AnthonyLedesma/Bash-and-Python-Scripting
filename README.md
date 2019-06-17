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

RANDOM CHANGE to README.md
