#!/usr/bin/python
import fcntl, sys
pid_file = '/home/pi/Public/lockfile.pid'
fh = open(pid_file, 'w')
try:
    fcntl.lockf(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
	#another instance is running
	print 'Error: Another instance is running...'
	sys.exit(0)

#from here my script code

import os
import cgi
import subprocess

os.remove("/home/pi/Downloads/scripts/mplayer-control.pipe")
os.system("mkfifo /home/pi/Downloads/scripts/mplayer-control.pipe")
os.system("mplayer -slave -input file=/home/pi/Downloads/scripts/mplayer-control.pipe /var/www/html/africa.mp3")
