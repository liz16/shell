#!/usr/bin/env python
from cmd2 import Cmd as cmd
import os
import pwd
import subprocess
import datetime
import getpass
import grp
from subprocess import check_output

class commands(cmd):
	def __int__(self):
		cmd.__int__(self)
		self.prompt = ">>> "
		self.intro = 'Custom Shell - type help if needed '

	def do_pw(self,user_input):
		subprocess.call(['pwd'])

	def do_ifc(self,user_input):
		empty = 'eth0'
		if not user_input:
			com = '/sbin/ifconfig ' + empty
		else:
			com = '/sbin/ifconfig ' + user_input
		com = com.split()
		subprocess.call(com, shell = False)

	def do_dt(self,user_input):
		dt = datetime.datetime.now()
		dt = dt.strftime('%Y%m%d%H%M%S')
		print(dt)

	def do_ud(self,user_input):
	# all the information for the  command output
		username = getpass.getuser()
		groupname = pwd.getpwnam(username)
		userid = os.getuid()
		groupid = os.getgid()
		ino = os.stat('.')
		ino = ino.st_ino
		groups = [g.gr_name for g in grp.getgrall() if username in g.gr_mem]
		groupid = os.getgid()
		groups.append(grp.getgrgid(groupid).gr_name) 

	# output 
		output = str(userid),str(groupid),str(username),str(groups).strip("'[]"),str(ino)
		output = str(output)
		output = output.strip("()'[]")
		output = output.replace("'","")
		output = output.replace(' ','')
		print(output)

	def do_exit(self, user_input):
		return -1

	def do_help(self,userinput):
		print('Shell commards')
		print('pw - Displays the current working disctory')
		print('ifc - Displays network interface. eth0 by default')
		print('dt - Displays current time and date of the system ')
		print('ud- Displays userid, groupid,username, groupname and inode')
		print('exit - logout ')

	def do_shell(self,userinput):
		print ('you cannot use this command')
		pass
if __name__ == '__main__':
	shell = commands()
	shell.cmdloop()
