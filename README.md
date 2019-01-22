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

### (IF Statement)[https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php]
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

### (For, While, Until)[http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-7.html]
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
