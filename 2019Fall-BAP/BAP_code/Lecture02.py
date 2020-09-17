# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:09:00 2019

@author: Weijun
"""
#%%
import numpy as np
a = np.array([1,2,3])
a.shape
a.dtype

#%%
b = np.array([1,2,3,4,5,6,7,8,9,10])
b[0:12:2]
b[5:]

#%%
d = np.arange(5)

z=np.linspace(0,5,5) # 包括5，linspace()包头包尾！！
print(z)

#%%
e = np.arange(5.)

#%%

# 注意list 和 array的区别
f = [1,2,3,4]
g = [5,6]
f+g