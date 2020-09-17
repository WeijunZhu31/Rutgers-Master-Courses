# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:49:42 2020

@author: naina
"""

from keras.datasets import fashion_mnist as datasets
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense
from tensorflow.keras.utils import to_categorical


(train_images,train_labels),(test_images,test_labels)=datasets.load_data()


inputLayer=Input(shape=(28,28)) 
tmp=Flatten()(inputLayer) #Will turn int a 1D array
tmp=Dense(units=512, activation='sigmoid')(tmp)
outputLayer=Dense(units=10,activation='softmax')(tmp)

network=Model(inputLayer,outputLayer)

network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])


train_images=train_images.astype('float32')/255
test_images=test_images.astype('float32')/255



train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)

network.fit(train_images, train_labels01, epochs=5, batch_size=128)

g = input("Please press enter to run with epochs 5") 
test_loss, test_acc=network.evaluate(test_images, test_labels01)
print('test_acc(epochs 5):',test_acc)

g = input("Please press enter to run with epochs 20") 
network.fit(train_images, train_labels01, epochs=20, batch_size=128)

test_loss, test_acc=network.evaluate(test_images, test_labels01)
print('test_acc(epochs 20):',test_acc)


print("with epochs 5 relu has given better accuracy rate as compare to logistic but with epochs 20 both give same accuracy rate ")

