# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 00:00:07 2020

@author: naina
"""

import q1c
from keras.datasets import fashion_mnist as datasets
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix


name = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat","Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

(train_images,train_labels),(test_images,test_labels)=datasets.load_data()


# keras sequential approach model
network=models.Sequential()
network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

# adding relu layer
network.add(layers.Dense(512,activation='relu',input_shape=(28*28,)))
# adding softmax layer which will return probability of an image to be out of the 10 categories mentioned
network.add(layers.Dense(10,activation='softmax',))

# converting image to 1D vector
train_images = train_images.reshape(60000,28*28)
test_images=test_images.reshape((10000,28*28))

# standardizing images
train_images=train_images.astype('float32')/255
test_images=test_images.astype('float32')/255

# converting labels to categorical values
train_labels_1 = to_categorical(train_labels)
test_labels_1 = to_categorical(test_labels)

# training the model with train data
network.fit(train_images, train_labels_1, epochs=5, batch_size=128)

# evaluating accuracy 
predicted_labels = network.predict_classes(test_images)

table1 = confusion_matrix(test_labels,predicted_labels)

g = input("Please press enter to print confusion matrix")

q1c.print_cm(table1,name)


pred = network.predict(test_images)

g = input("Please press enter to  print the percentage of times the second choice was the correct one. ")

q1c.check(test_images, test_labels, pred, predicted_labels, False)
       