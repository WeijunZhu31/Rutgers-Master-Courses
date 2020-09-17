# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:37:54 2019

@author: farid alizadeh
"""

# This file simulates a data by creating a vector 't', and the vector
# 'y' by setting y=3+4*t + eps 
# where 'eps' is a random error following normal distribution with mean
# zero and standard deviation 3. We use this data to create a kNN
# regression model.
# 
# 
# 

import numpy as np

#Generate data
n=10
tt=np.linspace(0,n,20)
#yy=4*tt+3+np.random.normal(0,3.5,size=len(tt))

def f(x):
 return(2*x+np.cos(x**2/4)-3*np.log(x+1)**2)
 #return 4*x+3 #a linear example

yy=f(tt)++np.random.normal(0,0.9,size=len(tt))

#Plot the real function and the scatter data
import matplotlib.pyplot as plt
import seaborn as sn

plt.scatter(tt,yy,color='black')
ttt=np.linspace(0,n,200)
#plt.plot(ttt,4*ttt+3,color='black')
plt.plot(ttt,f(ttt))
plt.show()

#Ask the user for k and generate the knn model
print('Enter value of k:')

from sklearn.neighbors import KNeighborsRegressor

print('Enter k (0 to exit):')
k=int(input())

while k>0:
    model=KNeighborsRegressor(n_neighbors=k)
    #model=KNeighborsRegressor(n_neighbors=k,weights='distance')
    model.fit(tt.reshape(-1,1),yy)
    testT=tt
    testY=model.predict(testT.reshape(-1,1))
    plt.scatter(tt,yy,color='black')
    plt.plot(testT,testY,color='black')
    plt.show()
    print('Enter k (0 to exit):')
    k=int(input())