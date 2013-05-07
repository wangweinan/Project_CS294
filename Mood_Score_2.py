#!/usr/bin/env python
import sys
import math
Date_Score
r = {}
for d in Date_Score:
    # (assumes just one key/value per dict)
    ((x, y),) = d.items() 
    r.setdefault(x, []).append(y)

print [{k: sum(v)/float(len(v))} for (k, v) in r.items()]
  

