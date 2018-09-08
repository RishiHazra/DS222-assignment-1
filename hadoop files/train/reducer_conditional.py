#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 23:50:35 2018

@author: rishi
"""
import sys
import math
vocab={}
class_count={}
vocabSet=set()

for line in sys.stdin:    
    line = line.strip() 
    if(len(line.split('\t'))==3):
        try:
            label, word, count1 = line.split('\t')
            #print('1',line.split('\t'))            
            if word not in vocabSet:
                vocab[word]={}
                vocabSet.add(word)
            vocab[word][label] = count1           
        except ValueError:
            continue
        
    elif(len(line.split('\t'))==2):
        try:
            label, count2 = line.split('\t')
            
            if label!='vocabCount':
                class_count[label] = count2 
                #print('2',line.split('\t'))
            else:
                vocabCount = count2                
        except ValueError:
            continue     
        
for k,v in vocab.items():
    for key,value in v.items():
        print(k,' ', key,'\t', math.log((int(vocab[k][key]) + 1) / (int(class_count[key]) + int(vocabCount))))
    
    
    
        
    
    
    
    
    

    
    