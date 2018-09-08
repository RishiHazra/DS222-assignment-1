#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 03:12:57 2018

@author: rishi
"""

# test map-reduce
import sys
import re

count = 0
for line in sys.stdin:
    if count>=3:
        
        labels = line.split(' \t')[0] 
        line = line.split(' \t')[1]
        line = re.sub(r'http\S+', '', line)
        line = re.sub(r"[-()\"#/@;%&$:<>{}`+=~|.!?,]", "", line)
        line = line.lower()
        line = re.sub("\d+", "",line)
        line = re.sub('@en', '', line) 
        line = re.sub('[^a-zA-Z]', ' ', line)  
        line = re.sub('\s+', ' ', line)  
        line = line.strip()  
          
        print(labels+'\t'+line)                    
                            
    count+=1  
