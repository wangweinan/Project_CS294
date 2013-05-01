#!/usr/bin/env python
import sys
import re
import math
import numpy as np
Date_Count = dict()

for line in sys.stdin:
    line = line.strip()
    score, date = line.split('\t',1)
    #print(score,date)
    try:
    	Date_Count[date] += 1
    except KeyError:
    	Date_Count[date] = 1
for item in Date_Count.keys():
	print('%s\t%.0f') % (item, Date_Count[item])
