Readme
Step 1: Software installation
Use the sudo apt-get install command to install python 3,net-tools  and pip.  Then use sudo  pip install command the install the following python packages: datautil, ditrack and cmd2
Step 2: 
•	Create a new user  - sudo useradd -m USERNAME
•	Give the new user a password - sudo passwd USERNAME
•	Add the new user to a group - sudo adduser USERNAME GROUPNAME
•	Create a new groups if needed - sudo groupadd GROUPNAME
Step 3: change the new users shell in the /etc/passwd file to the custom shell.
•	To access the /etc/passwd file - sudo nano /ect/passwd.
•	Look thought the file for your new user and change the default shell /bin/bash to the new shell and save.
Step 4: Custom shell commands
•	pw - Displays the current working directory 
•	ifc-  Displays network interface information. eth0 by default 
•	dt - Displays Current time and date of the system
•	ud - Displays userID, groupID, username, groupname and  iNode of user’s home directory
•	help-  help will display a copy of  step 4  
•	exit- exit program
References
15.1. os — Miscellaneous operating system interfaces — Python 2.7.14 documentation. 2017. Docs.python.org. Available from: https://docs.python.org/2/library/os.html [Accessed October 20, 2017].
17.5. subprocess — Subprocess management — Python 3.6.3 documentation. 2017. Docs.python.org. Available from: https://docs.python.org/3/library/subprocess.html [Accessed October 22, 2017].
Linux / UNIX: Display file inode (index number). 2017. nixCraft. Available from: https://www.cyberciti.biz/faq/howto-print-inode-data-structure/ [Accessed October 19, 2017].
Lloyd, G. 2017. Python: How to get group ids of one username (like id -Gn ). Stackoverflow.com. Available from: https://stackoverflow.com/questions/9323834/python-how-to-get-group-ids-of-one-username-like-id-gn [Accessed October 18, 2017].
Python Exercises: Split a string with multiple delimiters - w3resource. 2017. w3resource. Available from: https://www.w3resource.com/python-exercises/re/python-re-exercise-47.php [Accessed October 24, 2017].
Why "-bash: ifconfig : command not found" when typing "$ifconfig." 2017. Linuxquestions.org. Available from: https://www.linuxquestions.org/questions/linux-server-73/why-bash-ifconfig-command-not-found-when-typing-%24ifconfig-687928/ [Accessed October 24, 2017].


  
