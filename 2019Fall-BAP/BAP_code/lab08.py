# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:07:09 2019

@author: Weijun
"""

import pandas as pd
import numpy as np

resdf = pd.read_pickle('resdf.pkl')

resdf.info()
dd = resdf.iloc[0]

resdf['Year'].shape
resdf[resdf['Year'].isnull()]

resdf[resdf['Name'].notnull()].shape
resdf[resdf['NAME'].notnull()].shape

resdf.loc[resdf['Name'].isnull(),'Name']=resdf['NAME']
resdf[resdf['Name'].notnull()].shape
del resdf['NAME']
resdf.shape

resdf[resdf['10 Km'].notnull()].shape
resdf[resdf['5 Mi'].notnull()].shape
resdf[resdf['5 Mile'].notnull()].shape

resdf[resdf['10 Km'].notnull()].groupby('Year')['Year'].count()
resdf[resdf['5 Mi'].notnull()].groupby('Year')['Year'].count()
resdf[resdf['5 Mile'].notnull()].groupby('Year')['Year'].count()

resdf['Year'].unique()

df2007 = resdf[resdf['Year']==2007]

df2007=df2007[df2007.columns[~df2007.isnull().all()]]

resdf[resdf['Time'].notnull()].shape
resdf[resdf['TIME'].notnull()].shape

resdf.loc[resdf['Time'].notnull() | resdf['TIME'].notnull(),'Year'].unique()

dfs = resdf.groupby('Year').head(2).reset_index(drop=True)

resdf['time']=resdf['Time']
resdf.loc[resdf['TIME'].notnull(),'time']=resdf['TIME']

resdf[resdf['time'].notnull()].groupby('Year')['Year'].count()

resdf.loc[resdf['Net Tim'].notnull(),'time']=resdf['Net Tim']

resdf[resdf['time'].notnull()].groupby('Year')['Year'].count()

dfs = dfs.loc[dfs.Year.isin([2006, 2005, 2004, 2003, 2002, 2001,2000])]
resdf.loc[resdf['Gun Tim'].notnull(),'time']=resdf['Gun Tim']
resdf.loc[resdf['Net'].notnull(),'time']=resdf['Net']

resdf[resdf['time'].notnull()].groupby('Year')['Year'].count()

resdf.loc[resdf['NET'].notnull(),'time']=resdf['NET']
resdf.loc[resdf['NET TIM'].notnull(),'time']=resdf['NET TIM']
resdf.loc[resdf['Gun Ti'].notnull(),'time']=resdf['Gun Ti']
resdf[resdf['time'].notnull()].groupby('Year')['Year'].count()

del resdf['Time']
del resdf['TIME']
del resdf['Net Tim']
del resdf['Gun Tim']
del resdf['Net']
del resdf['NET']
del resdf['NET TIM']
del resdf['Gun Ti']
del resdf['10 Km']
del resdf['5 Mi']
del resdf['5 Mile']

dfs = resdf.groupby('Year').head(2).reset_index(drop=True)

resdf.columns
resdf['Hometown2']= resdf['Hometown        Net Tim'].str.extract(pat = '([A-Z a-z]+)') 
dfs = resdf.groupby('Year').head(2).reset_index(drop=True)

resdf.time2 = '00:' + resdf.time
resdf.ftime = pd.to_timedelta(resdf.time,unit='m')
