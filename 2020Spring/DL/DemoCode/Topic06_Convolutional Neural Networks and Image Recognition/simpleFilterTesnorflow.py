# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:11:39 2020

@author: -
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


from sklearn.datasets import load_sample_image


china = load_sample_image("china.jpg")/255
flower=load_sample_image("flower.jpg")/255
plt.imshow(china)
plt.show()
input("hit Enter")
plt.imshow(flower)
plt.show()
input("The original pictures. Hit Enter to continue")

images=np.array([china, flower])
batch_size, hight, width, channels = images.shape

filters=np.zeros(shape=(7,7,channels,2), dtype=np.float32)
filters[:,3,:,0]=1
filters[3,:,:,1]=1

outputs=tf.nn.conv2d(images, filters,strides=1, padding="SAME")


plt.imshow(outputs[0,:,:,1], cmap="gray")
plt.show()
input('Hit enter')
plt.imshow(outputs[1,:,:,1],cmap="gray")
plt.show()