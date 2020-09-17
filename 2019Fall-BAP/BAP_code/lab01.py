# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:51:55 2019
@author: Weijun

Lab01:NYC DataSets
"""
#%%
import pandas as pd 
import numpy as np

#%%
nyc = pd.read_csv('D:/Spyder/BAP/data/ny.csv',index_col=False)

#%%
nyc.head(10)

#%%
nyc['cand_nm']

#%%
nyc['cand_nm'].count()

#%%
nyc.contbr_employer
nyc.cand_nm.value_counts()

#%%
pd.isnull(nyc.contbr_employer).value_counts()

#%%
dfc = nyc.cand_nm.value_counts()
type(dfc)
#%%
dfc.values
dfc.index
ucm = dfc.index.values # 注意和上边的代码结果不一样！一个是index，一个是array！
#%%
dfc2 = pd.DataFrame({'cand_nm':ucm})    

#%%
dfc2.loc[0:2,'Party']='Democrat'
dfc2.loc[1,'Party']='Democrat'

#%%
dfc2.loc[0:1,'Party']='Liberal'
dfc2.loc[[0,1,18,21,14],'Party']='Democrat'
dfc2.loc[10,'Party']='Green'
dfc2.loc[11,'Party']='Liberatrain'
dfc2.loc[19,'Party']='Independent'
#%%
dfc2.Party.isnull()

#%%
# dfc2[dfc2.Party.isnull(),'Party'] = 'Republican' # error
#%%
dfc2.loc[dfc2.Party.isnull(),'Party'] = 'Republican'

#%%
cand_dict = dict(zip(dfc2.cand_nm,dfc2.Party))
#%%
cand_dict['Sanders', 'Bernard']
#%%
nyc['Party'] = nyc['cand_nm'].map(cand_dict)
nyc[['cand_nm','Party']].head(10)

#%%
nyc.describe()


#%%
nyc.info()
#%%
# this takes time
nyc['Date'] = pd.to_datetime(nyc['contb_receipt_dt'])

#%%
######################## 09/22 ############################
# goup by
A = pd.Series(['red','blue','yellow','orange','red','blue','yellow','orange'])
B = pd.Series([1,1,1,1,2,2,2,2])
Price = pd.Series(np.arange(1,9)) # arange包头不包尾！
dfexmp = pd.DataFrame({'A':A,'B':B,'Price':Price})


#%%
a = dfexmp.groupby('A') # find unique values in column A
for i in a:
    print(i)
#%%
df7 = nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum()
df7

#%%
# 注意和上边结果的区别
df7=nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum().reset_index()
df7
#%%
B

#%%
######################## 09/29 ############################
df7.sort_values(by='contb_receipt_amt',
               ascending=False,inplace=True)
pd.options.display.float_format = '{:,.2f}'.format
df7.head(5)
#%%
df8 = nyc.groupby('contbr_occupation')['contb_receipt_amt'].sum().reset_index()
df8.sort_values(by='contb_receipt_amt',inplace=True)
df8.head(5)

#%%
df9 = nyc.groupby('contbr_employer')['contb_receipt_amt'].sum().reset_index()
df9.sort_values('contb_receipt_amt',ascending=False,inplace=True)
df9.iloc[0:5]


#%%
df10 = nyc.groupby(['cand_nm','contbr_occupation'])['contb_receipt_amt'].sum().reset_index()
df10.sort_values(['cand_nm','contb_receipt_amt'],ascending=[True,False],inplace=True)
df10.groupby('cand_nm').head(10)

#%%
df11= nyc.groupby('cand_nm')['contb_receipt_amt'].sum().reset_index()
df11_p = df11.nlargest(5,'contb_receipt_amt')
df11_g = nyc[nyc.cand_nm.isin(df11_p.cand_nm)][['cand_nm','Date','contb_receipt_amt']]

dfpiv = pd.pivot_table(df11_g, values='contb_receipt_amt',
                       index=['Date'],columns=['cand_nm'],aggfunc=np.sum)
dfpiv.loc['2016-04-01':'2016-04-30'].plot.line()

#%%
# df13 = nyc[nyc.cand_nm='Clinton, Hillary Rodham']['cand_nm']
# 注意双括号的使用!!
df13 = nyc[nyc.cand_nm=='Clinton, Hillary Rodham'][['Date','cand_nm','contb_receipt_amt']]

# or
df13_1 = nyc.loc[(nyc.cand_nm=='Clinton, Hillary Rodham') | (nyc.cand_nm=='Sanders, Bernard'),
                 ['Date','cand_nm','contb_receipt_amt']]



###################################################
###################################################
###################################################
#%%
price=pd.Series({'cherry':2,'berry':1,'orange':3,'apple':4,'plum':7})
qty=pd.Series({'cherry':12,'berry':7,'orange':8,'apple':31})
fruitdf=pd.DataFrame({'price':price,'qty':qty})

#%%
df = pd.DataFrame([[100,100,100],[90,90,90],[86,80,80]],index=['张三','李四','王五'],columns=['语文','数学','外语'])
df







