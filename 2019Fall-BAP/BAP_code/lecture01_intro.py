# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:27:27 2019

@author: Weijun
"""
#%%
2+2
print(2+2)


#%%
x = 5
a = [1,2,3]

x
a
a[0] # R start from index 1
print(a[0])
print(a[1])
print(a[2])

#%%
for i in a:
    print(i)
#%%
len(a)

#%%
import numpy as np
i = [1,2,3]
a = np.array(i)
a
#%%
b = np.array([5.0,0.3,7])
b.dtype # float take more momery space
a[0:1]
a[0:7]

#%%
############# practice 01
x=[1,2,3,4,5]
y=x
x[1:2]=[10,11]

#%%
x = [ 1 , 2 , 3 , 4 , 5 ]
y=x.copy ( )
x[1:2] = [10 , 12]
#%%
x=[1,2,3,4,5]
y=[10,11,13,14,15]
z=[]
for i in range(len(x)):
    z.append(y[i]+x[i])
#%%
m1 = [4,2,1,3,1,2]
m2 = list(range(len(m1)-1))
m3 = list(range(m2[3]+m1[2]))

#%%
a = np.arange(5)
a[2] = 8.5 # array只能是一种数据类型

#%%
a = np.arange(5)
a = a*2.5
a[2] = 7.7

#%%
a = np.arange(5.)
a[2] = 8.5
    
    