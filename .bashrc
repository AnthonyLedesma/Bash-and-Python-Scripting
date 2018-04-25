# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

#Setting a function called wpconfig. 
#The script will connect to the database using the wp-config.php and will print the site and home URL. 
function wpconfig() (

# Defining important variables.
USER=$(ls -lad | cut -d\  -f3)
GROUP=$(ls -lad | cut -d\  -f4)
DBNAME=$(grep -i 'DB_NAME' wp-config.php | cut -d\' -f4)
DBUSER=$(grep -i 'DB_USER' wp-config.php | cut -d\' -f4)
DBPASSWORD=$(grep -i 'DB_PASSWORD' wp-config.php | cut -d\' -f4)
DBHOST=$(grep -i 'DB_HOST' wp-config.php | cut -d\' -f4 | rev | cut -d\: -f2 | rev)
DBPORT=$(grep -i 'DB_HOST' wp-config.php | rev |cut -d\: -f1 | rev | cut -d\' -f1)
PREFIX=$(grep -i 'table_prefix' wp-config.php | cut -d"'" -f2)

#Connect to the MYSQL Server and search for the siteurl and homeurl and set them as variables to be called later.
SITEURL=$(mysql -h ${DBHOST} -P ${DBPORT} -u ${DBUSER} -p${DBPASSWORD} -D ${DBNAME} -se "SELECT option_value FROM ${PREFIX}options WHERE option_name = 'siteurl';" | cut -f2)
HOMEURL=$(mysql -h ${DBHOST} -P ${DBPORT} -u ${DBUSER} -p${DBPASSWORD} -D ${DBNAME} -se "SELECT option_value FROM ${PREFIX}options WHERE option_name = 'home';" | cut -f2)

#test for config, this is using an if statement with a file test operator
# http://www.tldp.org/LDP/abs/html/fto.html
if [ -e wp-config.php ]
# if the config exists:
then
echo "we found the config data..."
echo "printing the info..."

# echoing useful stuff
echo "my dbname is ${DBNAME}"
echo "my dbuser is ${DBUSER}"
echo "my prefix is ${PREFIX}"
echo "my siteurl is ${SITEURL}"
echo "my home is ${HOMEURL}"

# if the config doesn't exist:
else
echo "we didn't find the config..."

# fi is the closing of our if statement
fi
#this is a command that will execute outside of our if statement, so regardless of whether or not it's true
echo "end of script"
)
#End of wpconfig function.




#Setting a function called debugtoggle.
#This script will toggle debug mode on and off using the wp-config.php file.
function debugtoggle () (

#Making sure config is here
if [ -e wp-config.php ]
then

#Checking to see if already toggled
if [ -e wp-config.php ] && [ -e wp-config.php.bak ]

#If already toggled on
then
echo "debug is currently on..."
echo "moving original config back..."

#here we replace the edited wp-config.php using the backup of the original file.
cp wp-config.php.bak wp-config.php

#Now lets remove the backup to keep files vanilla. 
rm wp-config.php.bak

#Quick identification of wheter or not the current setting is set as true or false.
DEBUG=$(grep -i "define( 'wp_debug" wp-config.php | cut -d\, -f2 | rev | cut -d' ' -f2 |rev)
echo "Checking... Debug is ${DEBUG}"


#If not already enabled then toggle on
else
echo "debug is currently off..."
echo "creating debug config..."
cp wp-config.php wp-config.php.bak
sed -i "/DEBUG/s/false/true/g" wp-config.php
DEBUG=$(grep -i "define( 'wp_debug" wp-config.php | cut -d\, -f2 | rev | cut -d' ' -f2 |rev)
echo "Checking... Debug is ${DEBUG}" 
fi

#If no wp-config.php is present then we will error with the following echo. 
else
echo "You are not in the install directory. Please run from install directory..."
fi
)


#working on finding the absolute path of the wp-config.php file and returning only the exact file.
#this will return ANY variations of wp-config.php such as wp-config.php.bak
#grep $USER /etc/passwd | cut -d\: -f6 | xargs find | grep "wp-config.php"

#Below is the decided upon code which will query the apache configuration to determine the document root/ WP install directory
grep -i "DocumentRoot " /etc/httpd/conf/httpd.conf | cut -d\" -f2

#Block of code for comparing one dir with another and NOT overwriting files but moving only new. 
#false | cp -i ABSPATH/www/wp-content/* ABSPATH/www/test/ 
#If this command is exceding the ARG_MAX then the command will kill iteself before finishing.
#getconf ARG_MAX 
#Here we have a sample of a loop that is intended to get around ARG_MAX limits.
#for file in /src/*; do cp "$file" /dst/; done 

#grep with regex match example. - Extracts IP addresses from access.log file located within the file system. 
#-r recursive | file not specified - recurse to look for pattern in all locations.
#-o Only show matches to pattern
#-P Perl Regex Pattern | ^starts with | \d digit char | {1,3} ranging from 1 char to 3 chars. | \. matches dot character | * match 0 or more of previous char.
#grep -roP "^\d{1,3}\.*\d{1,3}\.*\d{1,3}\.*\d{1,3}\.*"

