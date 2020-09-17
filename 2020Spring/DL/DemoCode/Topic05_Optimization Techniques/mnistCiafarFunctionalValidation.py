# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:42:18 2020

@author: alizadeh
"""

#This code is adopted from "Deep Learning with Python", by F. Chollet, CH. 2
#This is the "functional" form of the model

# In this script we use early stopping approach by using the provided
# callbacks. You can do this with or without ordinary l_1 or l_2 regularization
#
#It may be much faster if you run this script on the Google Colab servers
# using GPU

#tf.disable_v2_behavior() #Do this to use tesnorflow version <1.15
#%tensorflow_version 2.x # Do this if you wish to run Tensorflow 2.1
import tensorflow as tf

from tensorflow import keras
print("tesnorflow version:", tf.__version__, "Keras version:",keras.__version__)

from keras.datasets import cifar10



from keras.layers import Input, Flatten, Dense
from keras.models import Model

import numpy as np

(train_images,train_labels),(test_images,test_labels)=cifar10.load_data()
train_images=train_images.astype('float32')/255
test_images=test_images.astype('float32')/255

# First shuffle the data
perm=np.random.permutation(range(train_images.shape[0]))
train_images=train_images[perm]
train_labels=train_labels[perm]

from keras.utils import to_categorical
train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)

# generate training and validation sets
trainingSize=40000
train_images_used=train_images[:trainingSize]
train_labels01_used=train_labels01[:trainingSize]
val_images=train_images[trainingSize:]
val_labels01=train_labels01[trainingSize:]

# Build the model by early stopping.

#np.random.seed(13) #To obtain consistent and reproducible data
inputLayer=Input(shape=(32,32,3)) 
tmp=Flatten()(inputLayer) #Will turn int a 1D array
from keras import regularizers
from functools import partial
regularizedDense = partial(Dense,
                       activation = 'relu',
                       kernel_initializer = 'he_normal',
                       kernel_regularizer=regularizers.l2(0.001)
                       )
#tmp=keras.layers.Concatenate(input,tmp)
tmp=regularizedDense(units=512*3)(tmp)
tmp=regularizedDense(units=512*3)(tmp)
tmp=regularizedDense(units=512*3)(tmp)
#tmp=regularizedDense(units=512*3)(tmp)
#tmp=BatchNormalization()(tmp)
outputLayer=Dense(units=10,activation='softmax')(tmp)

network=Model(inputLayer,outputLayer) #Put the model together

network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])


earlyStoppingCB=keras.callbacks.EarlyStopping(patience=10,restore_best_weights=True)
history=network.fit(train_images_used, train_labels01_used, 
                    validation_data=(val_images,val_labels01),
                    epochs=100, batch_size=128, callbacks=[earlyStoppingCB])

test_loss, test_acc=network.evaluate(test_images, test_labels01)
print('test_acc:',test_acc)

import matplotlib.pyplot as plt
history_dic = history.history
# This line shows history_dic's keys. You can comment it out after
# the first run
print("keys of history.histry:",history_dic.keys())
loss_values=history_dic['loss']
validation_loss_values=history_dic['val_loss']

epochs = range(1,len(loss_values)+1)
plt.plot(epochs, loss_values, 'bo', label="Training loss")
plt.plot(epochs,validation_loss_values,'b',label="validation loss")
plt.title("Trainig and validation loss")
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

#plot training and valuation accuracy:

acc_values=history_dic['accuracy']
validation_acc_values=history_dic['val_accuracy']

plt.plot(epochs,acc_values, 'bo', label="Training acc")
plt.plot(epochs,validation_acc_values, 'b',label="Validation acc") 
plt.ylabel('Loss')
plt.legend()
plt.show()

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