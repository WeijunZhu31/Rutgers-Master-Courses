# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:23:18 2020

@author: -
"""
#%%
# This script, adopted from DLP, examines the Dropout method
# for neural networks. We use the IMDB data that comes with keras. Read the 
# description of this data in DLP:
from keras.datasets import imdb

import numpy as np

#%%
# Code needed to fix an incompatibilty bug in keras data loads. Keras uses
# the np.load function in numpy. The latest version is incompatible with
# keras load_data in that the allow_picke flag is turned off. We modify
# this temporarily:old = np.load
# old = np.load
# np.load = lambda *a,**k: old(*a,**k,allow_pickle=True)

maxWords=10000
(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=maxWords)

# np.load = old
# del(old)

print("Since only ", maxWords," words used, wor indices will not exceed ",maxWords)

print("max sequence: ", max([max(sequence) for sequence in train_data]))

# Need to turn list data (which is a list of word indices occurring in the review)
# into 0,1 "tensors"

#%%
def vectorize_sequences (sequences, dimension=10000): 
    results=np.zeros((len(sequences),dimension)) # create a matrix of zeros
    for i,sequence in enumerate(sequences): #set specific indices to 1
        results[i,sequence] = 1
    return(results)

        
#%%
x_train=vectorize_sequences(train_data)
x_test=vectorize_sequences(test_data)

#%%
# Also vectorize the labels whih are 0-1 sequences
y_train=np.asarray(train_labels).astype('float32')
y_test=np.asarray(test_labels).astype('float32')

#%%
# Shuffle the data set aside a validation set and the real training set
xy_train=np.append(x_train,y_train.reshape(len(y_train),1), axis=1)
np.random.shuffle(xy_train)
x_train=xy_train[:,:10000]
y_train=xy_train[:,10000]


#%%
# set aside a validation set and the real training set
x_validation=x_train[:10000]
y_validation=y_train[:10000]
x_train_partial=x_train[10000:]
y_train_partial=y_train[10000:]

#%%
# Experiment with different values of units set units2 = 4 and then = 64
# and compare the results units1=16. And include Dropout layers
# and observe the effect on the accuracy for both the validation and 
# the the test sets:
from keras.layers import Input, Flatten, Dense, Dropout
from keras.models import Model
#from keras import regularizers

#%%
inputLayer=Input(shape=(maxWords,)) 
#tmp=Flatten()(inputLayer) #Will turn int a 1D array
units1=16
tmp=Dense(units=units1, activation='relu')(inputLayer)
tmp=Dropout(rate=0.2)(tmp)
#tmp=Dense(units=units1, activation='relu',kernel_regularizer=regularizers.l2(.001))(inputLayer)

units2=16
tmp=Dense(units=units2, activation='relu')(tmp)
tmp=Dropout(rate=0.5)(tmp)
#tmp=Dense(units=units2, activation='relu',kernel_regularizer=regularizers.l2(.001))(tmp)

outputLayer=Dense(units=1,activation='sigmoid')(tmp)

network=Model(inputLayer,outputLayer)

network.compile(optimizer='rmsprop', loss='binary_crossentropy',metrics=['accuracy'])

history = network.fit(x_train_partial,y_train_partial, epochs=20, batch_size=512,
                      validation_data=(x_validation,y_validation))


test_loss, test_acc=network.evaluate(x_test,y_test)
print("test loss:", test_loss, "test accuracy:", test_acc)

#%%
# plot training and validation losses
import matplotlib.pyplot as plt
history_dic = history.history
history_dic.keys()
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

#%%
#plot training and valuation accuracy:

acc_values=history_dic['accuracy']
validation_acc_values=history_dic['val_accuracy']

plt.plot(epochs,acc_values, 'bo', label="Training acc")
plt.plot(epochs,validation_acc_values, 'b',label="Validation acc") 
plt.ylabel('Loss')
plt.legend()
plt.show()

