#!/usr/bin/python
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

import subprocess
from time import sleep

y=(0.01)
subprocess.Popen(["python", 'music.py'])
sleep(y)
subprocess.Popen(["python", 'timers.py'])
sleep (y)
