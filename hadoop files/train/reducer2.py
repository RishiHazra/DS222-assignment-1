#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 00:12:38 2018

@author: rishi
"""
#from __future__ import print_function
import sys
current_label = None
current_count = 0
word = None
#vocab_count = 0
label = None

for line in sys.stdin:
    
    label, count = line.split('\t')
    
    try:
        count = int(count)
    except ValueError:
        continue

    if current_label == label:
        current_count += count
        #vocab_count += 1
    else:
        if current_label:
           print('%s\t%s' % (current_label, current_count))
        
        current_count = count
        current_label = label
        #vocab_count+= 1
        
        
if current_label == label:
    #vocab_count += count
    print('%s\t%s' % (current_label, current_count))
    #print('vocab_count ', vocab_count)