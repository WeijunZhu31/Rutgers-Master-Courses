# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:33:13 2019

@author: Weijun
"""

#import TextBlob
import pip

#!pip install textblob
#!python -m textblob.download_corpora

from textblob import TextBlob

import numpy as np
import pandas as pd
import nltk
nltk.download()

#df = dftsla.copy()
#df= pd.read_pickle('dftrumpall.pkl')
tx = df.loc[0,'full_text']
blob = TextBlob(tx)
blob.tags
blob.tags[0]
blob.sentences
blob.sentences[0]
blob.sentences[0].words
blob.sentences[0].words[0]
blob.noun_phrases
blob.ngrams(3)
blob.ngrams(5)
blob.ngrams(5)[0]
blob.correct()
blob.words[1].spellcheck()
blob.words[5].spellcheck()
blob.detect_language()
blob.translate(to= 'fr') 

#%%
verbs = []
for word, tag in blob.tags:
  if (tag=='VB') | (tag=='VBG'):
    verbs.append(word.lemmatize())

#%%
verbs = []
for word, tag in blob.tags:
  if tag in ['VB','VBG']:
    verbs.append(word.lemmatize())

#%%
nouns = []
for word, tag in blob.tags:
	if tag == 'NN':
		nouns.append(word.lemmatize())

#%%
nounsp = []
for word, tag in blob.tags:
	if tag == 'NNP':
		nounsp.append(word.lemmatize())

#%%
blob.sentiment.polarity
blob.sentiment.subjectivity

#%%
#Create 2 arrays
polarity=[]
subj=[]

#%%
#Get polarity and sentiment for each row and put it in either polarity or sentiment 
for t in df.full_text:
    tx=TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    subj.append(tx.sentiment.subjectivity)

#%%
#Put in dataframe polsubj which has a column of polarity values and a column of subjectivity values
polsubj = pd.DataFrame({'polarity': polarity,'subjectivity': subj})

#%%
#Plot the line graph
polsubj.plot(title='Polarity and Subjectivity')

polsubj.plot(kind='bar',title='Polarity and Subjectivity')

polsubj.tail(30).plot(title='Polarity and Subjectivity')
polsubj.head(30).plot(title='Polarity and Subjectivity')






