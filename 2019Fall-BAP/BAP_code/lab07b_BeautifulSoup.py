# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:44:47 2019

@author: Weijun
"""
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

urls=['http://cherryblossom.org/results/2012/2012cucb10m-m.htm',
      'http://cherryblossom.org/results/2011/2011cucb10m-m.htm']

for i in urls:
    res = requests.get('http://www.cherryblossom.org/results/2012/2012cucb10m-m.htm')
    soup = BeautifulSoup(res.content, 'lxml')
    
    table = soup.find('pre').contents[0]
    tablerows = table.split('\r\n')
    
    
    
    
    
    
    webdf[newcol] = pd.DataFrame(webdf.rawal.values.tolist())
    
    newrows=[rownumber-1] + list(range(rownumber+1,webdf.shape[0]))
    
    webdf2=webdf.loc[newrows,newcol]
    
    webdf3=webdf2.applymap(lambda r: ''.join(r))
    webdf3=webdf3.applymap(lambda r: r.strip())
    
    datadf = webdf3.iloc[1:]
    datadf.columns = webdf3.iloc[0].tolist()
    datadf=datadf.reset_index(drop=True)
    resdf=pd.concat([resdf,datadf], axis=0, ignore_index=True)

