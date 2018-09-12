#!/usr/bin/python

import RPi.GPIO as GPIO
import os
os.system("pgrep -f timers.py")
os.system("pkill -9 -f timers.py")
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

all_lines = (2,3,4,5,6,7,9,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27)
GPIO.setup(all_lines, GPIO.OUT)
GPIO.output(all_lines, GPIO.LOW)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.HIGH)

os.system("echo stop > /home/pi/Downloads/scripts/mplayer-control.pipe")