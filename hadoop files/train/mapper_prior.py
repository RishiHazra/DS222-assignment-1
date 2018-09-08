#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 05:21:57 2018

@author: rishi
"""

# prior probabilities map-reduce

#from __future__ import print_function
import sys

# input from hdfs
for line in sys.stdin:
    labels = line.split(' \t')[0]
    
    for lab in labels.split(','):
        print('%s\t%s' % (lab, 1))
    