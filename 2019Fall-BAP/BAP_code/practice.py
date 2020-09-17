# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 18:22:55 2019

@author: Weijun
"""
#%%
import pandas as pd
import numpy as np

#%%
'''
bap_pp3
'''
Fruit = ['Apple','Orange','Grapes','Plums','Peaches','Water Melon','Pineapple']
Price=[2,2,5,2,6,5,4]
Sales=[140,400,180,300,120,180,60]
Date=['Jan-1-2017','May-10-2017','Feb-5-2017','Mar-7-2017','Apr-12-2017','Nov-18-2017','Jul-13-2017']

df = pd.DataFrame({'Fruit':Fruit,'Price':Price,'Sales':Sales,'Date':Date})

#%%
# 3.
#df[df.Fruit == 'Orange', Price] = 4  #This is ERROR !!!
df.loc[df.Fruit == 'Orange', 'Price'] = 4
#df.iloc[df.Fruit == 'Orange', 1] = 4  #This is ERROR !!!
#df.iloc[df.Fruit == 'Orange']['Price']  = 4  #This is ERROR !!!

#%%
# 4.
df.loc[(df.Fruit == 'Orange') & (df.Sales < 100), 'Price'] = 5

#%%
# 5.
df2 = df[:, ['Sales', 'Price']]  # This is ERROR !!
df2 = df.iloc[:, ['Sales', 'Price']]  # This is ERROR !!


df2 = df.loc[:, ['Sales', 'Price']] 
df2=df[['Sales','Price']]

#%%
# 6.
df.loc[:, 'Period'] = pd.to_datetime(df.Date)

df.loc['Period'] = pd.to_datetime(df.Date)
#%%
# 7.
df2 = df.loc[(df.Sales) > 100 & (df.Price > 5)]

df2 = df.loc[(df['Sales']) > 100 & (df['Price'] > 5)]

df2 = df[(df.Sales) > 100 & (df.Price > 5)]

#%%
# 8.
dft = df.loc[df.Sales < 250]

dft.sort_values('Price', inplace = True)

df2 = dft.head(20)






#%%
'''
bap_pp4
'''
#%%
# 1.
a=pd.Series([5,4,3,2,1], index=['peach','orange','melon','cherry','apple'])
b=pd.Series([50,40,30, 20,10],index=['apple','cherry','melon','orange','peach'])
df=pd.DataFrame({'a':a,'b':b})
x=sum(df.iloc[2,0:2])
x

#%%
# 2.
a=pd.Series([5,4,3,2,1], index=['apple', 'cherry', 'melon', 'orange', 'peach'])
b=pd.Series([50,40,30, 20,10],index=['apple','cherry','melon','orange','peach'])
df2=pd.DataFrame({'a':a,'b':b})
df2=pd.DataFrame({'a': a, 'b':b})
x=sum(df2.iloc[3,[0,1]])
x

#%%
# 3.
a=pd.Series([5,4,3,2,1], index=['peach','orange','melon','cherry','apple'])
b=pd.Series([50,40,30, 20,10],index=['peach','orange','melon','cherry','apple'])
df3=pd.DataFrame({'a':a,'b':b})
x=df3.iloc[2]['b']
x

#%%
# 4.
a=pd.Series([5,4,3,2,1], index=['peach','orange','melon','cherry','apple'])
b=pd.Series([50,30,20,10],index=['peach','melon','cherry','apple'])
df4=pd.DataFrame({'a':a,'b':b})
x=df4.iloc[3].sum()
x

#%%
# 5.
x=np.arange(5.)
x[2]=3.5
y=sum(x)
y

#%%
# 7.
x=np.array([0,2,4,6,8])
y=x*1.5
z=y.copy()
z[1:3]=y[[0,4]]
z





#%%
'''
bap_pp5
'''
#%%
from textblob import TextBlob

text=['Thanks so much for driving me home.','Thanks so much for cooking dinner. I really appreciate it.',
      'Excuse me sir, you dropped your wallet.','I’m sorry for the mess. I wasn’t expecting anyone today.',
      'My name is Sophie and I’m learning English.']
df=pd.DataFrame({'a':range(5),'b':range(5),'text':text})

#%%
#1
df2=df[['text','b']]

#2
polarity=[]
subj=[]
 
for t in df.text:
    tx=TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    subj.append(tx.sentiment.subjectivity)
    
df2['Polarity']=polarity
df2['Subj']=subj


df2['Polarity2']=df2.text.apply(lambda x: TextBlob(x).sentiment.polarity)
df2['Subj2']=df2.text.apply(lambda x: TextBlob(x).sentiment.subjectivity)

#3
df2['textl']=df2.text.str.lower()

#4
df2['textlist']=df2.textl.str.split()

#5
df2['textarray']=df2.textlist.apply(np.array)

#6
df2['textadj']=df2.textarray.apply(lambda x: x[~np.isin(x,['i','me'])])

#7
s=np.array(['apple','orange','plum'])
s2=np.insert(s,0,'cherry')
print(s2)

df2['textadj2']=df2.textadj.apply(lambda x: np.insert(x,0,'Batman'))

#painful
df2['textadj2']=df2.textadj.apply(lambda x: np.array(['Batman']+x.tolist()))

#8
df2['textadj3']=df2.textadj2.apply(lambda x: pd.Series(x)[~pd.Series(x).str.contains('ing')].values)

#9
df2['textnew']=df2.textadj3.apply(lambda x: ' '.join(x))

#10
tx=df2.textnew.str.cat(sep=' ')
print(tx)

#11
list11=[]
df2.textadj3.apply(lambda x: list11.extend(x.tolist()))
print(list11)

dfw=pd.DataFrame({'w':list11,'w2':list11})
dfw2=dfw.groupby('w')['w2'].count().reset_index()












#%%




