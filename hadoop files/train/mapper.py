#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 04:19:00 2018

@author: rishi
"""

import re
import sys
#import nltk
#stop_words = nltk.corpus.stopwords.words('english')
#from nltk.stem import PorterStemmer
#lemmatizer =PorterStemmer()
vocabularySet = set()
vocabularyCount = 0
stop_words = {"some", "don", "she", "wasn't", "didn't", "once", "it", "between", "which", "s", "these",
			  "such", "me", "few", "from", "will", "same", "whom", "needn", "very", "through", "are", "she's", "we", "down", "off", "against",
			  "here", "o", "above", "when", "him", "he", "if", "am", "who", "haven't", "do", "has", "should", "you", "mustn't", "a", "again", "had", "up",
			  "ve", "weren", "yours", "their", "only", "her", "them", "aren", "not", "shouldn", "ourselves", "your", "too", "hasn", "most", "until", "d", "did", "all", "ma", "won't",
			  "no", "after", "wouldn", "didn", "of", "with", "t", "you'd", "couldn", "so", "doesn", "wouldn't", "ours", "there", "don't", "hadn", "needn't", "aren't", "its", "now",
			  "mightn", "yourselves", "you'll", "doing", "can", "but", "you've", "in", "other", "wasn", "and", "further", "won", "own", "they", "an", "how", "this", "because", "than",
			  "hadn't", "before", "were", "just", "as", "having", "isn", "himself", "during", "what", "couldn't", "ain", "into", "shouldn't", "weren't", "does", "was", "is", "that'll",
			  "about", "nor", "themselves", "while", "y", "mustn", "you're", "myself", "where", "at", "yourself", "doesn't", "itself", "i", "re", "each", "why", "those", "theirs", "to",
			  "both", "that", "his", "below", "ll", "mightn't", "should've", "haven", "it's", "any", "out", "being",
			  "shan", "then", "isn't", "herself", "hasn't", "under", "have", "on", "hers", "m", "over", "our", "shan't", "for", "more", "be", "or", "the", "my", "by", "been", }

count=0
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
          
        words = re.split('\W', line)
        for word in words: 
            if word not in vocabularySet and word not in stop_words:
                vocabularySet.add(word)
                vocabularyCount = vocabularyCount + 1            
                #word = lemmatizer.stem(word)                          
        #if word not in stop_words:
            for lab in labels.split(','):
                if word:
                    print(lab+' '+word+'\t'+'1')
                     
                        
    count+=1
print('%s %s\t%s' % ('vocabCount', '=', vocabularyCount)) 