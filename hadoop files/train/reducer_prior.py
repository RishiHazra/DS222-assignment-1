#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 05:31:40 2018

@author: rishi
"""
#from __future__ import print_function
import sys
current_label = None
current_count = 0
total_docs = 0
label=None

for line in sys.stdin:
    
    label, count = line.split('\t')
    
    try:
        count = int(count)
    except ValueError:
        continue

    if current_label == label:
        current_count += count
        total_docs += count
    else:
        if current_label:
           print('%s\t%s' % (current_label, current_count))
        
        total_docs += count
        current_count = count
        current_label = label
        
        
if current_label == label:
    print('%s\t%s' % (current_label, current_count))
    print('%s\t%s' % ('total_docs', total_docs))