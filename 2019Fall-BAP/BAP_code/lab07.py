# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:22:29 2019

@author: Weijun
"""
#%%
import pandas as pd 
import numpy as np
import requests 
from bs4 import BeautifulSoup

#%%
res = requests.get('http://www.cherryblossom.org/results/2012/2012cucb10m-m.htm')
soup = BeautifulSoup(res.content, 'lxml')
print(soup)

#%%
table = soup.find('pre').contents[0]
type(table)

#%%
tablerows = table.split('\r\n')
tablerows[0:5]

#%%
x = 'the cat in the hat is fat'
y = x.split('at')
print(y)

