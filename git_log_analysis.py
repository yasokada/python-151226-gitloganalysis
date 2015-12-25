#!/usr/bin/env python

from datetime import datetime as dt 
from datetime import timedelta

'''
v0.1 2015/12/26
	- add main routine
 	  + take two datetime difference
	  + have two datetime
	  + read files
	- add calcElapsedTimeInMinutes()
'''

def calcElapsedTimeInMinutes(diff_sec):
	diff_min = diff_sec / 60
	diff_hr = diff_min / 60
	if diff_hr >= 4:
		return 0
	else:
		return diff_min

fd = open("tmp.log")
lines = fd.readlines()
fd.close()

bfStart = False
acc_min = 0
for line in lines:
	items = line.split(' ')
	strdt = items[1] + " " + items[2]
	tdt1 = dt.strptime(strdt, "%Y-%m-%d %H:%M:%S")
#	print tdt1
	if bfStart:
		diff_sec = (tdt2 - tdt1).seconds
		acc_min += calcElapsedTimeInMinutes(diff_sec)
		print tdt1, diff_sec, acc_min, "# sec, min"
	else:
		bfStart = True
	tdt2 = tdt1

