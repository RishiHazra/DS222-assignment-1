#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:08:23 2018

@author: rishi
"""

#from __future__ import print_function
import sys

for line in sys.stdin:    
    
    try:
        label, _, count = line.split('\t')
    except ValueError:
        continue
    
    # convert count (currently a string) to int
    try:        
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    
    
    print('%s\t%s' % (label, count))