#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import time

def timer(x):
    while time.time() - start < x:
        pass

def convert(time_str):
    m, s = time_str.split(':')
    return float(m) * 60 + float(s)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

all_lines = (2,3,4,5,6,7,9,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27)
GPIO.setup(all_lines, GPIO.OUT)
GPIO.output(all_lines, GPIO.LOW)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.HIGH)

start = time.time()

provoleas = convert("00:01.009")
timer(provoleas)
GPIO.output(8, GPIO.LOW)

andras = convert("00:04.632")
timer(andras)
GPIO.output(12, GPIO.HIGH)

gynaika = convert("00:21.302")
timer(gynaika)
GPIO.output(18, GPIO.HIGH)

pano = convert("00:38.572")
timer(pano)
GPIO.output(19, GPIO.HIGH)
GPIO.output(18, GPIO.LOW)
GPIO.output(12, GPIO.LOW)

dromos = convert("01:00.595")
timer(dromos)
GPIO.output(17, GPIO.HIGH)
GPIO.output(19, GPIO.LOW)

dasos_mprosta = convert("01:32.151")
timer(dasos_mprosta)
GPIO.output(9, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(17, GPIO.LOW)

dasos_pisw = convert("01:46.469")
timer(dasos_pisw)
GPIO.output(3, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(16, GPIO.LOW)

change1 = convert("01:54.237")
timer(change1)
GPIO.output(11, GPIO.HIGH)
GPIO.output(3, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

change2 = convert("01:55.827")
timer(change2)
GPIO.output(3, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)

change3 = convert("01:57.755")
timer(change3)
GPIO.output(9, GPIO.HIGH)
GPIO.output(3, GPIO.LOW)

change4 = convert("01:59.625")
timer(change4)
GPIO.output(6, GPIO.HIGH)
GPIO.output(9, GPIO.LOW)

dasos_mprosta = convert("02:01.572")
timer(dasos_mprosta)
GPIO.output(9, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)
GPIO.output(6, GPIO.LOW)

change1 = convert("02:03.227")
timer(change1)
GPIO.output(3, GPIO.HIGH)
GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(16, GPIO.LOW)

dasos_pisw = convert("02:05.012")
timer(dasos_pisw)
GPIO.output(6, GPIO.HIGH)

change1 = convert("02:06.75")
timer(change1)
GPIO.output(9, GPIO.HIGH)
GPIO.output(3, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

change2 = convert("02:08.455")
timer(change2)
GPIO.output(11, GPIO.HIGH)
GPIO.output(9, GPIO.LOW)

dasos_mprosta = convert("02:10.33")
timer(dasos_mprosta)
GPIO.output(9, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)

dasos_pisw = convert("02:12.061")
timer(dasos_pisw)
GPIO.output(3, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(16, GPIO.LOW)

black_out = convert("02:13.826")
timer(black_out)
GPIO.output(3, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

shine = convert("02:15.548")
timer(shine)
GPIO.output(3, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(9, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)

poulia = convert("02:34.411")
timer(poulia)
GPIO.output(7, GPIO.HIGH)
GPIO.output(3, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(16, GPIO.LOW)

dasos_pisw = convert("02:40.645")
timer(dasos_pisw)
GPIO.output(3, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(7, GPIO.LOW)

batraxia = convert("02:48.367")
timer(batraxia)
GPIO.output(2, GPIO.HIGH)
GPIO.output(3, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

dasos_pisw = convert("02:52.487")
timer(dasos_pisw)
GPIO.output(3, GPIO.HIGH)
GPIO.output(6, GPIO.HIGH)
GPIO.output(2, GPIO.LOW)

shine = convert("02:56.047")
timer(shine)
GPIO.output(9, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)
GPIO.output(16, GPIO.HIGH)

dasos_mprosta = convert("03:02.640")
timer(dasos_mprosta)
GPIO.output(3, GPIO.LOW)
GPIO.output(6, GPIO.LOW)

hlianthoi = convert("03:09.448")
timer(hlianthoi)
GPIO.output(4, GPIO.HIGH)
GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(16, GPIO.LOW)

skala = convert("03:19.318")
timer(skala)
GPIO.output(5, GPIO.HIGH)
GPIO.output(4, GPIO.LOW)

lelekia = convert("03:41.448")
timer(lelekia)
GPIO.output(10, GPIO.HIGH)
GPIO.output(5, GPIO.LOW)

change1 = convert("03:48.031")
timer(change1)
GPIO.output(11, GPIO.HIGH)
GPIO.output(10, GPIO.LOW)

change2 = convert("03:54.769")
timer(change2)
GPIO.output(16, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)

skroutz = convert("04:04.509")
timer(skroutz)
GPIO.output(13, GPIO.HIGH)
GPIO.output(11, GPIO.LOW)

xrysalida = convert("04:24.5")
timer(xrysalida)
GPIO.output(25, GPIO.HIGH)
GPIO.output(13, GPIO.LOW)

kazani = convert("05:39.593")
timer(kazani)
GPIO.output(26, GPIO.HIGH)

pania = convert("06:10.646")
timer(pania)
GPIO.output(21, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)

forema = convert("06:27.559")
timer(forema)
GPIO.output(20, GPIO.HIGH)

pano = convert("07:09.053")
timer(pano)
GPIO.output(24, GPIO.HIGH)
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(26, GPIO.LOW)

fin = convert("07:30.121")
timer(fin)
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
GPIO.output(25, GPIO.HIGH)
GPIO.output(26, GPIO.HIGH)
