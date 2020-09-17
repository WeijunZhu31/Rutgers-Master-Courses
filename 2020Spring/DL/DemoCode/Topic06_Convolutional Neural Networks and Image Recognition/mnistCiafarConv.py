# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:49:54 2020

@author: alizadeh
"""

#This code is adopted from "Deep Learning with Python", by F. Chollet, CH. 2
# The data is a a set of 50,000 color low resolution pictures that should
# belong to ten categories (animals and moving vheicles)

# It may be quicker if you run this on colab with GPU's (See description in HW2)
# However, when I run this code on Colab it behaves differently and gives 
# incorrect results. Your experience may be different
# 

# In this script we just run the plain vanila three desne layer neural net
# without any kind of regularization or initialization 
# This script will serve as a basis for comparison
from keras.datasets import cifar10

(train_images,train_labels),(test_images,test_labels)=cifar10.load_data()

from keras.layers import Input, Flatten, Dense, Conv2D, MaxPool2D
from keras.models import Model

import numpy as np

#np.random.seed(13) #To obtain consistent and reproducible data
#This code is adopted from "Deep Learning with Python", by F. Chollet, CH. 2
# The data is a a set of 50,000 color low resolution pictures that should
# belong to ten categories (animals and moving vheicles)

# It may be quicker if you run this on colab with GPU's (See description in HW2)
# However, when I run this code on Colab it behaves differently and gives 
# incorrect results. Your experience may be different
# 

# In this script we just run the plain vanila three desne layer neural net
# without any kind of regularization or initialization 
# This script will serve as a basis for comparison
from keras.datasets import cifar10

(train_images,train_labels),(test_images,test_labels)=cifar10.load_data()

from keras.layers import Input, Flatten, Dense
from keras.models import Model

import numpy as np

#np.random.seed(13) #To obtain consistent and reproducible data
inputLayer=Input(shape=(32,32,3)) 
tmp=Conv2D(filters=10,kernel_size=(4,4),strides=2,activation='relu',padding='same')(inputLayer)
tmp=Conv2D(filters=20,kernel_size=(3,3),strides=2,activation='relu',padding='same')(tmp)
tmp=Flatten()(tmp)
outputLayer=Dense(units=10,activation='softmax')(tmp)

network=Model(inputLayer,outputLayer)

network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

train_images=train_images.astype('float32')/255
test_images=test_images.astype('float32')/255

from keras.utils import to_categorical

train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)

network.fit(train_images, train_labels01, epochs=30, batch_size=128)

test_loss, test_acc=network.evaluate(test_images, test_labels01)
print('test_acc:',test_acc)


import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

pred=network.predict(test_images) #pred contains probabilities of each class

names=['Airplane','Automobile','Bird','Cat','Deer','Dog','Frog','Horse',
       'Ship','Truck']
print("The confustion matrix:\n",confusion_matrix(test_labels, list(map(np.argmax,pred))))

#Visualizing the confusion matrix. If all the colors are in the diagonal 
#it means all were correctly classified. Off diagonal colors indicate 
#misclassification
print("The visualization of the confusion matrix:")
import seaborn as sns
sns.heatmap(confusion_matrix(test_labels, list(map(np.argmax,pred))),cmap="Spectral")
plt.show()

#Now running over misclassified data, printing the real abd predicted
#values, showin gthe actual image, and printing and showing the bar
#graph of probability assigned to each class 
# Now examine the performance of the model on various inputs if you wish.

if input("Do you wish to see performance on the test set? y/n")=='y':
    for i in range(len(test_images)):
        if test_labels[i]!=np.argmax(pred[i]):
            print("ERROR PREDICTION")
        plt.imshow(test_images[i])
        plt.show()
        print("predicted value of data item ",i,':', names[np.argmax(pred[i])], " actual value:", names[test_labels[i][0]])
        print(pred[i])
        plt.bar(height=pred[i],x=range(10))
        plt.xticks(range(len(names)),names, rotation=90)
        plt.show()
        if input("continue? y/n")=='n':
            break
