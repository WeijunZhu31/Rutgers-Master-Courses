#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 14:52:19 2020

@author: gwt
"""

from keras.datasets import fashion_mnist

from keras.layers import Input, Flatten, Dense
from keras.models import Model
from keras import regularizers
import numpy as np

(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()
train_images=train_images.astype('float32')/255
test_images=test_images.astype('float32')/255

#shuffle the training data
perm=np.random.permutation(range(train_images.shape[0]))
train_images=train_images[perm]
train_labels=train_labels[perm]

from keras.utils import to_categorical

train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)

#separate to training and validation set
trainingSize=50000
train_images_used=train_images[:trainingSize]
train_labels01_used=train_labels01[:trainingSize]
val_images=train_images[trainingSize:]
val_labels01=train_labels01[trainingSize:]

#input a tensor
inputLayer=Input(shape=(28,28))
tmp=Flatten()(inputLayer)

#different combinations of regularization
tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l1_l2(l1=0.01, l2=0.001))(tmp)
#tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l1_l2(l1=0.001, l2=0.01))(tmp)
#tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l1_l2(l1=0.01, l2=0.01))(tmp)
#tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l1_l2(l1=0.001, l2=0.001))(tmp)
#tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l1(0.01))(tmp)
#tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l1(0.001))(tmp)
#tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l2(0.01))(tmp)
#tmp=Dense(units=512, activation='relu',kernel_regularizer=regularizers.l2(0.001))(tmp)
outputLayer=Dense(units=10,activation='softmax')(tmp)

network=Model(inputLayer,outputLayer)

network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

history=network.fit(train_images_used, train_labels01_used, 
                validation_data=(val_images,val_labels01),
                epochs=20, batch_size=128)

test_loss, test_acc=network.evaluate(test_images, test_labels01)
print('test_acc:',test_acc)
    
import matplotlib.pyplot as plt
history_dic = history.history

print("keys of history.histry:",history_dic.keys())
#graph the loss
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

#graph the accuracy
acc_values=history_dic['acc']
validation_acc_values=history_dic['val_acc']

plt.plot(epochs,acc_values, 'bo', label="Training acc")
plt.plot(epochs,validation_acc_values, 'b',label="Validation acc") 
plt.ylabel('Loss')
plt.legend()
plt.show()

from sklearn.metrics import confusion_matrix

#show the confusion matrix
pred=network.predict(test_images)

print("The confustion matrix:\n",confusion_matrix(test_labels, list(map(np.argmax,pred))))

print("The visualization of the confusion matrix:")
import seaborn as sns
sns.heatmap(confusion_matrix(test_labels, list(map(np.argmax,pred))),cmap="Spectral")
plt.show()