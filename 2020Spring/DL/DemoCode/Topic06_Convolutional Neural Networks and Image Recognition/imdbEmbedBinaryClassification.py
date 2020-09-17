# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:38:55 2020

@author: alizadeh
"""
# In this script we revisit the imbd data that comes with keras. Howebver,
# instead of instead of vectorizing by using 0-1 indicator vectors (that is
# "one-hotting",) we use the "embedding" technique. That is we select a 
# k-dimensional real space, and assign each word to a point in this Euclidean 
# space. The idea is that the coordinates of the words assigned points are 
# learned by the "Embedding" layer, which should be right after the input
# layer. See DLP Ch. 6 for details. In DLP, they download the original data 
# from its webiste and process it. We use the keras data, which represents
# each word with an iteger.
from keras.datasets import imdb
from keras import preprocessing
import numpy as np


maxWords=10000 #Only the maxWords most common words are considered
maxLen=100 # the maximum length sequence, rest will be cut off

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=maxWords)

# Pre-process sequences, by padding if the length (# tokens) is less than 
# maxLen:
x_train = preprocessing.sequence.pad_sequences(train_data, maxLen)
x_test = preprocessing.sequence.pad_sequences(test_data, maxLen)
# Also vectorize the labels which are 0-1 sequences
y_train=np.asarray(train_labels).astype('float32')
y_test=np.asarray(test_labels).astype('float32')
# Now we insert an embedding layer and then use desne layers to classify

from keras.layers import Input, Dense, Embedding, Flatten
from keras.models import Model
from keras import regularizers

#inputLayer=Input(shape=(maxWords,))
inputLayer=Input(shape=(maxLen,), dtype='int32', name='main_input')

#Embedding(output_dim=512, input_dim=10000, input_length=100)(main_input)

embeddingDim=8 # Set the dimension of s[ace in which embedding is done
tmp = Embedding(input_dim=maxWords, output_dim=embeddingDim, input_length=maxLen)(inputLayer)
tmp=Flatten()(tmp)
from functools import partial
regularizedDense = partial(Dense,
                       activation = 'relu',
                       #kernel_initializer = 'he_normal',
                       kernel_regularizer=regularizers.l1(0.001)
                       )
units1=16
tmp=regularizedDense(units=units1)(tmp)
#tmp=Dense(units=units1, activation='relu',kernel_regularizer=regularizers.l2(.01))(inputLayer)

# Experiment with different values of units set units2 = 4 and then = 64
# and compare the results by looking at the training and validation loss
# and accuracy graphs. 
units2=16
tmp=regularizedDense(units=units2)(tmp)
#tmp=Dense(units=units2, activation='relu',kernel_regularizer=regularizers.l2(.01))(tmp)

outputLayer=Dense(units=1,activation='sigmoid')(tmp)

network=Model(inputLayer,outputLayer)

network.compile(optimizer='rmsprop', loss='binary_crossentropy',metrics=['accuracy'])

# When fitting the model, we assign the result to the object "history".
# This object retains all the intermediate values of weights. We can use
# it to plot the progress of the algorithm, both for training and validation
# data.
# Also, notice that here we do not need to explicitly break the training 
# data to train and validation, Setting validation_split ratio, the fit 
# function will do it for us:
history = network.fit(x_train,y_train, epochs=20, batch_size=512,
                      #validation_data=(x_validation,y_validation)
                      validation_split=.1 
                      )

test_loss, test_acc=network.evaluate(x_test,y_test)
print("test loss:", test_loss, "test accuracy:", test_acc)

# plot training and validation losses
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
plt.xlabel('Epochs')
plt.ylabel('accuracy')
plt.legend()
plt.show()
