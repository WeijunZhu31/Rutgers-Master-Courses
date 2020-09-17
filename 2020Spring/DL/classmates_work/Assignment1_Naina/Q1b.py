# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:36:57 2020

@author: naina
"""
import q1c
import numpy as np
from keras.datasets import fashion_mnist as datasets
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix

name = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat","Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
(train_images,train_labels),(test_images,test_labels)=datasets.load_data()

# functional approach implementation
inputLayer=Input(shape=(28,28)) 

#Will turn into a 1D array
tmp=Flatten()(inputLayer)
tmp=Dense(units=512, activation='relu')(tmp)
outputLayer=Dense(units=10,activation='softmax')(tmp)

network=Model(inputLayer,outputLayer)
network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])


# standardizing images
train_images=train_images.astype('float32')/255
test_images=test_images.astype('float32')/255


# converting labels to categorical values
train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)

#epochs = 5
g = input("Please press enter to run with epochs 5") 
network.fit(train_images, train_labels01, epochs=5, batch_size=128)
predicted_lables_epochs5 = network.predict(test_images)
final_predicted_lables_epochs5 = []
for i in range(len(predicted_lables_epochs5)):
    final_predicted_lables_epochs5.append(np.argmax(predicted_lables_epochs5[i]))
table2 = confusion_matrix(test_labels,final_predicted_lables_epochs5)
test_loss, test_acc=network.evaluate(test_images, test_labels01)
print("for epochs 5 :")
print('test_acc:',test_acc)

g = input("Please press enter to print confusion matrix")

q1c.print_cm(table2,name)

#epochs = 20
g = input("Please press enter to run with epochs 20") 
network.fit(train_images, train_labels01, epochs=20, batch_size=128)
predicted_lables_epochs20 = network.predict(test_images)
final_predicted_lables_epochs20 = []
for i in range(len(predicted_lables_epochs20)):
    final_predicted_lables_epochs20.append(np.argmax(predicted_lables_epochs20[i]))
table3 = confusion_matrix(test_labels,final_predicted_lables_epochs20)
test_loss, test_acc=network.evaluate(test_images, test_labels01)
print("for epochs 20 :")
print('test_acc:',test_acc)
g = input("Please press enter to print confusion matrix")
q1c.print_cm(table3,name)


g = input("Please press enter to  print the percentage of times the second choice was the correct one. ") 
q1c.check(test_images,test_labels, predicted_lables_epochs5,final_predicted_lables_epochs5 ,True)