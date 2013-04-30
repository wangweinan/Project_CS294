#!/usr/bin/env python
import sys
import re
import math
import numpy as np
Date_Count = dict()

for line in sys.stdin:
    line = line.strip()
    score, date = line.split('\t',1)
    try:
    	Date_Count[date] += 1
    except KeyError:
    	Date_Count.update(dict(zip(date,1)))

print(Date_Count)