#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 21:51:49 2018

@author: rishi
"""

import sys
import math
c=[]
lab=[]
for line in sys.stdin:
    
    try:
        label, count = line.split('\t')
    except ValueError:
        continue
    
    try:        
        count = int(count)
    except ValueError:
        continue
    
        
    if label == 'total_docs':
        total = count
    else:
        c.append(count)
        lab.append(label)
        
prob=[x / total for x in c] 

i=0
for x in prob: 
    print('%s\t%s' % (lab[i], math.log(x)))
    i+=1