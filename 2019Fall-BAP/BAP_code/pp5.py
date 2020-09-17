# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:35:25 2019

@author: Weijun
"""

import numpy as np
import pandas as pd

from textblob import TextBlob

text=['Thanks so much for driving me home.','Thanks so much for cooking dinner. I really appreciate it.',
      'Excuse me sir, you dropped your wallet.','I’m sorry for the mess. I wasn’t expecting anyone today.',
      'My name is Sophie and I’m learning English.']
df=pd.DataFrame({'a':range(5),'b':range(5),'text':text})

#%%
# 1
df2=df[['text','b']]

#%%
# 2
polarity=[]
subj=[]
 
# Method 1
for t in df.text:
    tx=TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    subj.append(tx.sentiment.subjectivity)
    
df2['Polarity']=polarity
df2['Subj']=subj

# Method 2
df2['Polarity2']=df2.text.apply(lambda x: TextBlob(x).sentiment.polarity)
df2['Subj2']=df2.text.apply(lambda x: TextBlob(x).sentiment.subjectivity)

#%%
# 3
df2['textl']=df2.text.str.lower()

#%%
# 4
df2['textlist']=df2.textl.str.split() # list keep the commas ！！！

#%%
# 5
# Method 1
df2['textarray']=df2.textlist.apply(np.array) # commas disappear ！！！
df2.loc[0, 'textlist']

# Method 2
df2['textarray']=df2.textlist.apply(lambda x: np.array(x))

#%%
# 6
df2['textadj']=df2.textarray.apply(lambda x: x[~np.isin(x,['i','me'])])

#  step by step
aa = np.array(['apple', 'batman', 'chocolate', 'car', 'plum'])
bb = ['batman', 'plum']
~np.isin(aa,bb)  # ~ --> flip everything ！！！
aa[np.isin(aa,bb)]

# give this in final！！！
df2['textadj']=df2.textarray.apply(lambda x: x[~np.isin(x,['home','wallet'])])


#%%
# 7
# Ex.
s=np.array(['apple','orange','plum'])
s2=np.insert(s,0,'cherry')
print(s2)

# 
df2['textadj2']=df2.textadj.apply(lambda x: np.insert(x,0,'Batman'))

# painful:more complicated
df2['textadj2']=df2.textadj.apply(lambda x: np.array(['Batman']+x.tolist()))

#%%
# 8
df2['textadj3']=df2.textadj2.apply(lambda x: pd.Series(x)[~pd.Series(x).str.contains('ing')].values)

#%%
# 9
df2['textnew']=df2.textadj3.apply(lambda x: ' '.join(x))

#%%
# 10
tx=df2.textnew.str.cat(sep=' ')
print(tx)

#%%
# 11
list11=[]
df2.textadj3.apply(lambda x: list11.extend(x.tolist()))
print(list11)

dfw=pd.DataFrame({'w':list11,'w2':list11})
dfw2=dfw.groupby('w')['w2'].count().reset_index()


