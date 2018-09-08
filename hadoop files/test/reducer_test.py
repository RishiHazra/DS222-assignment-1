#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 03:52:03 2018

@author: rishi
"""

# test map-reduce
import sys
import re
import math
vocabSet = set()
likelihood = {}
prior = {}


f = open('conditional')
for line in f.readlines():
    count = line.split('\t')[1]
    try:
        word, label = line.split('\t')[0]
    except ValueError:
        continue
        
    if word not in vocabSet:
        likelihood[word]={}
        vocabSet.add(word)
    likelihood[word][label] = count   
     
   
f1 =open('prior')
for line in f1.readlines():        
    try:
        label, prob = line.split('\t')
    except ValueError:
        continue
    prior[label] = float(prob)
    
   
 
Posterior = {}    
j=0
labels = {}
for line in sys.stdin: 
    try:
        label, text = line.split('\t')
    except ValueError:
        continue
    
    Posterior[j] = {}   
    words = re.split(' ', text)
    
    
    for lab in prior.keys(): 
        
        Posterior[j][lab] = prior[lab]
        
        for word in words:
            try:
                Posterior[j][lab] += float(likelihood[word][lab])                              
            except KeyError:
                Posterior[j][lab] += math.log(1/100000)
              
       
    k=[];
    for labe in label.split(','):
        k.append(labe)
    labels[j]=k 
    j += 1

pred_labels=[]    
for k,v in Posterior.items():
    pro=list(v.values())
    l=list(v.keys())
    pred_labels.append(l[pro.index(max(pro))])
        

correct=0
for i in range(0,len(pred_labels)):
    #print(i)
#print(list(labels.values()))

    if pred_labels[i] in list(labels.values())[i]:
        correct += 1
        
acc = correct/len(pred_labels)

print('accuracy','=',acc)        
  
  
    
    