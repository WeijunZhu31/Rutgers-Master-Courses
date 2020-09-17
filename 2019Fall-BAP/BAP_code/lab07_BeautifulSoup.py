# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:08:29 2019

@author: Weijun
"""
#%%
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

#%%  
urls=['http://cherryblossom.org/results/2012/2012cucb10m-m.htm',
      'http://cherryblossom.org/results/2011/2011cucb10m-m.htm',
      'http://www.cherryblossom.org/results/2010/2010cucb10m-m.htm',
      'http://www.cherryblossom.org/results/2009/09cucb-M.htm',
      'http://www.cherryblossom.org/results/2008/men.htm',
      'http://www.cherryblossom.org/results/2007/men.htm',
      'http://www.cherryblossom.org/results/2006/men.htm',
      'http://www.cherryblossom.org/results/2005/CB05-M.htm',
      'http://www.cherryblossom.org/results/2004/men.htm',
      'http://www.cherryblossom.org/results/2003/CB03-M.HTM',
      'http://www.cherryblossom.org/results/2002/oofm.htm',
      'http://www.cherryblossom.org/results/2001/oof_m.html',
      'http://cherryblossom.org/results/2000/Cb003m.htm',
      'http://cherryblossom.org/results/1999/cb99m.html']

#urls=['http://cherryblossom.org/results/2012/2012cucb10m-m.htm',
#      'http://cherryblossom.org/results/2011/2011cucb10m-m.htm']


#%%
#res = requests.get('http://cherryblossom.org/aboutus/results_list.php')
#menu = BeautifulSoup(res.content,'lxml')

#%%
#table = menu.find("a").contents[1]
resdf = pd.DataFrame()
date_v=2012
for i in urls:
    res = requests.get(i)
    soup = BeautifulSoup(res.content,'lxml')
    
    #table = soup.find("pre").contents[0]
    table = soup.find_all("pre")
    
    
    if len(table)<5:
        tablerows=table[0].text.split('\r\n')
        if len(tablerows)<10:
            tablerows=table[0].text.split('\n')
        if len(tablerows)<10:
            table = soup.find_all("font")[3:]
            tablerows=table[0].text.split('\r\n')
    else:
        tablerows=[]
        for x in table:
            tablerows.append(x.text.replace('\xa0',' '))
    
    webdf=pd.DataFrame({'raw':tablerows})
    
    rownumber=webdf.loc[webdf.raw.str.contains("=")].index.values[0]
    #dash=webdf.loc[rownumber,'raw']
    dash = webdf.loc[webdf.raw.str.contains("="),'raw'].values[0]
    
    sampletext=webdf.loc[rownumber+1,'raw']
    colraw=webdf.loc[rownumber-1,'raw']
    da=np.array(list(dash))
    dashpos=np.argwhere(da==' ').flatten().tolist()
    webdf['rawa']=webdf.raw.apply(lambda x: np.array(list(x)))
    webdf['rawal']=webdf.rawa.apply(lambda x: np.split(x, dashpos))
    
    newcol=list(range(len(dashpos)+1))
    
    webdf[newcol] = pd.DataFrame(webdf.rawal.values.tolist())
    
    newrows=[rownumber-1] + list(range(rownumber+1,webdf.shape[0]))
    
    webdf2=webdf.loc[newrows,newcol]
    
    webdf3=webdf2.applymap(lambda r: ''.join(r))
    webdf3=webdf3.applymap(lambda r: r.strip())
    
    datadf = webdf3.iloc[1:]
    datadf.columns = webdf3.iloc[0].tolist()
    datadf=datadf.reset_index(drop=True)
    datadf['Year']=date_v
    date_v=date_v-1
    
    if '' in datadf.columns:
        del datadf['']
        
    datadf.columns.duplicated()
    col_names=np.array(datadf.columns)
    mult_n=len(col_names[datadf.columns.duplicated()])
    new_col_nm=np.arange(mult_n).astype(str)
    col_names[datadf.columns.duplicated()]=col_names[datadf.columns.duplicated()]+new_col_nm
    datadf.columns=col_names
    resdf=pd.concat([resdf,datadf], axis=0, ignore_index=True)
    
resdf[resdf.Year==2010].shape
#resdf.to_pickle('resdf.pkl')
    








#%%
y = 'the cat hat'
yy = np.array(list(y))
yyy = np.split(yy, [3,7])
















