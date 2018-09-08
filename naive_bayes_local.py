#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:13:16 2018

@author: rishi
"""

import re
from tqdm import tqdm
import numpy as np
import nltk
stop_words = nltk.corpus.stopwords.words('english')
#from nltk.stem.wordnet import WordNetLemmatizer
#lemmatizer = WordNetLemmatizer()
from nltk.stem import PorterStemmer

lemmatizer =PorterStemmer()

f = open('/scratch/ds222-2017/assignment-1/DBPedia.full/full_train.txt')

text={}
label={}
#vocabulary = []
vocabularySet = set()
vocabularyCount = 0
countDocuments = 0
vocab={}
for line in tqdm(f.readlines()[3:]):
    #print(line.split('\t')[0])
    
    labels = line.split(' \t')[0]
    line = line.split(' \t')[1].split('"')[1]
    line = re.sub(r'http\S+', '', line)
    line = re.sub(r"[-()\"#/@;%&$:<>{}`+=~|.!?,]", "", line)
    line = line.lower()
    line = re.sub("\d+", "",line)
    line = re.sub('@en', '', line)  # remove end of sentence
    line = re.sub('[^a-zA-Z]', ' ', line)  # remove all punctuations, special-char and digits
    line = re.sub('\s+', ' ', line)  # replace multiple spaces
    line = line.strip()  # replace multiple spaces
    text[countDocuments] = line
    #text[countDocuments] = ' '.join(word for word in text[countDocuments])    
    words = re.split(' ', line)
    for word in words: 
        #word = lemmatizer.stem(word)                          
        if word not in vocabularySet and word not in stop_words:
            vocabularySet.add(word)
            #vocabulary.append(word)
            vocabularyCount = vocabularyCount + 1
            vocab[word]=1
        elif word in vocabularySet:
            vocab[word]=vocab[word]+1
                    
    j=[];
    for lab in labels.split(','):
        j.append(lab)
    label[countDocuments]=j
    countDocuments = countDocuments+1         

# class-conditional densities
#conditional = {k: v / vocabularyCount for k, v in vocab.items()}

from sklearn.preprocessing import MultiLabelBinarizer
mlb = MultiLabelBinarizer()

encoded = mlb.fit_transform(label.values())

cond={}
class_count={}
for z in range(0,encoded.shape[1]):
    column = encoded[:,z]
    ind = [i for i, x in enumerate(column) if x == 1]
    from operator import itemgetter
    lines= itemgetter(*ind)(list(text.values()))
    if len(ind)==1:
        line = lines
    else:
        line = " ".join([each for each in lines])     
    words = re.split(' ', line)
    cond[z]={}
    class_count[z]=0
    for word in words:
        if word not in cond[z]:
            cond[z][word] = 1
            class_count[z]+=1
        elif word in cond[z]:
            cond[z][word] = cond[z][word] + 1
            class_count[z]+=1

            
cond1 = {k: {key: (value + 1) / (class_count[k]+vocabularyCount) for key, value in v.items()} for k, v in cond.items()}       
#class_count = {k: sum(v.values()) for k,v in cond.items()}


#Calculating prior of each class    
prior=[(sum([row[i] for row in encoded]))/countDocuments for i in range(0,len(encoded[0]))]


'''
test set accuracy
'''

f_dev = open('/scratch/ds222-2017/assignment-1/DBPedia.full/full_test.txt')
text_dev={}
label_dev={}
countDocuments_dev=0
for line in f_dev.readlines()[3:]:
    #print(line.split('\t')[0])
    labels_dev = line.split(' \t')[0]
    line = line.split(' \t')[1].split('"')[1]
    line = re.sub(r'http\S+', '', line)
    line = re.sub(r"[-()\"#/@;:$<>{}`+=~|.!?,]", "", line)
    line = line.lower()
    line = re.sub("\d+", "",line)
    line = re.sub('@en', '', line)  # remove end of sentence
    #line = re.sub('[^a-zA-Z]', ' ', line)  # remove all punctuations, special-char and digits
    line = re.sub('\s+', ' ', line)  # replace multiple spaces
    line = line.strip()  # replace multiple spaces
    text_dev[countDocuments_dev] = line
    #text_dev[countDocuments_dev] = [i for i in line.split() if i not in stop_words]
    #text_dev[countDocuments_dev] = ' '.join(word for word in text_dev[countDocuments_dev])
    words = re.split(' ', line)
              
    j=[];
    for lab in labels_dev.split(','):
        j.append(lab)
    label_dev[countDocuments_dev]=j
    countDocuments_dev += 1    
   
    
Posterior = {}
j=0
for line in tqdm(text_dev.values()):
    Posterior[j]={}
    words = re.split(' ', line)
    for i in range(0, len(encoded[1])):
        #print(j,i)
        Posterior[j][i] = np.log(prior[i])
        for word in words:
            #word = lemmatizer.stem(word)
            try: 
                cond1[i][word] 
                Posterior[j][i] += np.log(cond1[i][word]) 
                #print(word,' ',i,' ',np.log(cond1[i][word]))                
            except KeyError:
                Posterior[j][i] += np.log(1/(class_count[i] + vocabularyCount)) 
        #Posterior[j][i] += np.log(prior[i])       
        
    j = j + 1
    
    
import operator
a={}
for key,value in Posterior.items():
    a[key]=max(value.items(), key=operator.itemgetter(1))[0]
    
pred_labels=list(a.values())

count=0
for i in range(0,len(pred_labels)):
    #print('Pred: ',mlb.classes_[pred_labels[i]],' ','True: ',list(label_dev.values())[i])
    if mlb.classes_[pred_labels[i]] in label_dev[i]:
        count=count+1
        
print('accuracy ',count/len(pred_labels))


