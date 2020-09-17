# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:44:05 2020

@author: alizadeh
"""

from keras.datasets import mnist
(train_images,train_labels),(test_images,test_labels)=mnist.load_data()

import numpy as np
import filter

Lett=train_images[0]

#This script runs over the test data and one by one draws those hand-
#writing images that were mis classified. (You can change != to == in the 
#if statement to look at those which are correctly classified.)

import matplotlib.pyplot as plt
plt.imshow(Lett,cmap=plt.cm.binary)

print("label of this images:", test_labels[4])

plt.imshow(Lett,cmap=plt.cm.binary)
plt.show()

F1=np.zeros((5,5)) #vertical edge detector
F1[:,2]=np.ones((5))
F1[:,3]=-np.ones((5))

F2=np.ones((2,2)) #smoother (moving average)

F3=np.ones((2,2))-np.eye(2)

F4=np.zeros((1,1)) 
F4[0,0]=1

#sharpen chnage 5 to larger numbers and see the effect.
F5=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=np.float32)

# Edge detect
F6=np.array([[0,1,0],[1,-4,1],[0,1,0]])

# Stronger edge detect
F7=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
plt.imshow(filter.filter(Lett,F7),cmap=plt.cm.binary) #Change to F1, F2,... to see effects if various fileters
plt.show()
               