#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 04:48:32 2018

@author: rishi
"""
#from __future__ import print_function
import sys

current_word = None
current_label = None
current_count = 0
word = None

'''
Refer to this link
https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
'''
for line in sys.stdin:
    
    line1, count = line.split('\t')
    label, word = line1.split(' ')
    #label, word, count = line.split('\t')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_label == label:        
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print('%s\t%s\t%s' % (current_label, current_word, current_count))
            current_count = count
            current_word = word
            current_label = label
    else:
        if current_label:
           print('%s\t%s\t%s' % (current_label, current_word, current_count))        
        current_label = label
        current_count = count
        current_word = word

# do not forget to output the last word if needed!
if current_label == label and current_word == word:
    print('%s\t%s\t%s' % (current_label, current_word, current_count))