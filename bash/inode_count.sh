#!/usr/bin/env bash
temp=$IFS; IFS=$'\n'; total=0; echo; echo "Searching path $(pwd)"; echo; for x in `find ./ -maxdepth 1 -type d  | egrep './' | sed 's:./::'`; do files=$(find $x | wc -l); total=$(($total + $files)); echo -e "$files\t\t $x"; done; echo; echo -e "Inode total for the above directories: \t$total"; echo; IFS=$temp;
