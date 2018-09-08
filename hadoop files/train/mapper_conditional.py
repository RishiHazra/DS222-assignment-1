#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 00:36:24 2018

@author: rishi
"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    if(line.split('\t')[1]=='='):
        continue 
    
    line = line.strip()
    # split the line into words
    print(line)