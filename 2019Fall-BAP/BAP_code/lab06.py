# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:39:56 2019

@author: Weijun
"""
#%%
#http://www.cherryblossom.org/results/2011/2011cucb10m-m.htm

#http://www.cherryblossom.org/results/2010/2010cucb10m-m.htm

#http://www.cherryblossom.org/results/2009/09cucb-M.htm

#%%
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#%%
res = requests.get('http://www.cherryblossom.org/results/2012/2012cucb10m-m.htm')

#%%
#######  save res object to folder  ######################
a=pd.Series('res object')
dfres = pd.DataFrame({'a':a})
dfres['avalue']=res
dfres.to_pickle('dfres.pkl')
dfres2 = pd.read_pickle('dfres.pkl')
res2 = dfres2.loc[0,'avalue']
#######  end ############################################


#%%
soup = BeautifulSoup(res.content,'lxml')
print(soup)


#%%
table = soup.find("pre").contents[0]
type(table)


#%%
xx = 'Hi I love the dark chocolate mousse'
xx[0:5]
xxlist = xx.split(' ')


#%%
table[0:5]
table[0:100]
tablerows=table.split('\r\n')
print(tablerows)
tablerows[0:5]


#%%
marvel='iron man is not as rich as batman'
marvel[3:10]


#%%
#example
x='the cat in the hat is fatty'
y=x.split('at')
y


#%%
webdf=pd.DataFrame({'raw':tablerows})

#%%
webdf.loc[7, 'raw']

#%%
rownumber=webdf.loc[webdf.raw.str.contains("=")]
rownumber
type(rownumber)


#%%
rownumber=webdf.loc[webdf.raw.str.contains("=")].index.values[0]
dash=webdf.loc[rownumber,'raw']

#%%
dash =webdf.loc[webdf.raw.str.contains('='),'raw'].values[0]
type(dash)
print(dash)


#%%
sampletext=webdf.loc[rownumber+1,'raw']
colraw=webdf.loc[rownumber-1,'raw']

#%%
vv='batman'
print(list(vv))
da=np.array(list(dash))
print(da)


#%%
dashpos = np.argwhere(da == ' ')
dashpos = np.argwhere(da==' ').flatten().tolist()
print(dashpos)


#%%
ww="I love dark chocolate mousse from Mara's"
wwa=np.array(list(ww))
wwl=np.split(wwa,[6,21]) # 分成了三个部分
print(wwl)
''.join(wwl[0])

#%%
# apply() --> for lop
ee = ['I love', 'dark chocolate', 'chocolate fountain']
dfx = pd.DataFrame({'food':ee})
dfx['food2'] = dfx.food.apply(lambda x : x[0:3]) # is the same thing as for loop


#%%
webdf['rawa']=webdf.raw.apply(lambda x: np.array(list(x)))
webdf['rawal']=webdf.rawa.apply(lambda x: np.split(x, dashpos))


#%%
#Example: Splitting Lists into New Columns
expl=[['toyota','black'],['bmw','red'],['ford','grey'],['audi','white']]
dfexp = pd.DataFrame({'First':expl})
dfexp[['Second','Third']]=pd.DataFrame(dfexp.First.values.tolist())

#%%
webdf.loc[7, 'rawal']

#%%
len(webdf.loc[7, 'rawal']) 
len(dashpos) + 1
range(len(dashpos) + 1)
list(range(len(dashpos) + 1))

newcol=list(range(len(dashpos)+1))

#%%
webdf[newcol] = pd.DataFrame(webdf.rawal.values.tolist())

#%%
webdf[newcol] = pd.DataFrame(webdf.rawal.values.tolist(), index= webdf.index)
newrows=[rownumber-1]+list(range(rownumber+1,webdf.shape[0]))

#%%
[rownumber-1]
webdf.shape[0]
list(range(rownumber+1, webdf.shape[0]))

[rownumber-1] + list(range(rownumber+1, webdf.shape[0]))

#%%
webdf2=webdf.loc[newrows,newcol]

#%%
# applymap()
webdf3=webdf2.applymap(lambda r: ''.join(r))
webdf3=webdf3.applymap(lambda r: r.strip())

#%%
datadf = webdf3.iloc[1:]
datadf.columns = webdf3.iloc[0].tolist()
datadf=datadf.reset_index(drop=True)

