# .bashrc
# Beginnings of Bash Scriping

Shell Script Order and Checklist
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

### [IF Statement](https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php)
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

### [For, While, Until](http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html)
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


### [mp3_processor](https://github.com/paranoia1906/.bashrc/blob/master/mp3s/mp3_processor)
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

### [Find Command](http://man7.org/linux/man-pages/man1/find.1.html)
```bash
#This command will find only file with names ending with .mp3 within the current directory 
#-execdir to execute rm command on each item. -exec & -execdir replace {} with each item returned.
#"{}" should be quoted if find is being invoked from a shell.  
#This a much more secure method for invoking commands, as it avoids race conditions during resolution of 
#the paths to the matched files.
find ./ -type f -name "*.mp3" -execdir rm "{}" \;
```

### [User Input](https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php)
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

### [Case Statements](https://www.tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_03.html)
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
