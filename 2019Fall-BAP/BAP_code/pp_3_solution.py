#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 16:34:56 2019

@author: wajgilani
"""

import numpy as np
import pandas as pd

Fruit = ['Apple','Orange','Grapes','Plums','Peaches','Water Melon','Pineapple']
Price=[2,2,5,2,6,5,4]
Sales=[140,400,180,300,120,180,60]
Date=['Jan-1-2017','May-10-2017','Feb-5-2017','Mar-7-2017','Apr-12-2017','Nov-18-2017','Jul-13-2017']

df = pd.DataFrame({'Fruit':Fruit,'Price':Price,'Sales':Sales,'Date':Date})

#3
df.loc[df.Fruit=='Orange','Price']=4

#4
df.loc[(df.Fruit=='Orange') & (df.Sales<100),'Price']=5



#5
df2=df[['Sales','Price']]

#6
df['Period']=pd.to_datetime(df.Date)

#7
df2 = df.loc[(df.Sales>100) & (df.Price>5)]

#8
df2 = df.loc[df.Sales<250].sort_values('Price').head(20)

#%%
df = pd.DataFrame([('bird', 389.0),
                   ('bird', 24.0),
                   ('mammal', 80.5),
                   ('mammal', np.nan)],
                  index=['falcon', 'parrot', 'lion', 'monkey'],
                  columns=('class', 'max_speed'))
df






