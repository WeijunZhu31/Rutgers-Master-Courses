# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:36:11 2020

@author: Weijun
"""
#%%
import tensorflow as tf
from tensorflow import keras
print("tesnorflow version:", tf.__version__, "Keras version:",keras.__version__)
from keras.datasets import fashion_mnist
from keras import models
from keras import layers
from keras.layers import Input, Flatten, Dense
from keras.models import Model
from keras.utils import to_categorical
import numpy as np
np.random.seed(9)

#%%
(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()

#%%
# Shuffle the training data
temp_trainIM = list(enumerate(train_images))
temp_trainLB_1 = list(enumerate(train_labels))
np.random.shuffle(temp_trainIM)

temp_trainLB = []
for i in temp_trainIM:
    temp_trainLB.append(temp_trainLB_1[i[0]])

train_images = []
train_labels = []
for i in temp_trainIM:
    train_images.append(i[1])
for i in temp_trainLB:
    train_labels.append(i[1])
train_images = np.array(train_images)
train_labels = np.array(train_labels)

#%%
# Split the training and validation sets
training_images = train_images[:50000,]
training_labels = train_labels[:50000,]
# Set the validation set
validation_images = train_images[:-50000,]
validation_labels = train_labels[:-50000,]
# display(training_images.shape, training_labels.shape, validation_images.shape, validation_labels.shape,
#        test_images.shape, test_labels.shape)

#%%
training_images = training_images.astype("float32")/255
validation_images = validation_images.astype("float")/255
test_images = test_images.astype("float")/255

training_labels01 = to_categorical(training_labels)
validation_labels01 = to_categorical(validation_labels)
test_labels01 = to_categorical(test_labels)

#%%
# Use EarlyStopping instead of norm regularization
from keras import regularizers

inputLayer = Input(shape=(28,28))
tmp = Flatten()(inputLayer)
tmp = Dense(units=512, activation="relu")(tmp)
outputLayer = Dense(units=10, activation="softmax")(tmp)

network = Model(inputLayer, outputLayer)
network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])
# Early Stopping
earlyStoppingCB = keras.callbacks.EarlyStopping(patience=10,restore_best_weights=True)
history = network.fit(training_images,training_labels01, epochs=100, batch_size=128,
                      validation_data=(validation_images,validation_labels01),
                      callbacks=[earlyStoppingCB])

test_loss, test_acc = network.evaluate(test_images,test_labels01)
print("test loss:", test_loss, "test accuracy:", test_acc)

#%%
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

#%%
# Confusion Matrix
import numpy as np
from sklearn.metrics import confusion_matrix

pred = network.predict(test_images)
# We can not use "test_labels" because it handles after "to_categorical" method !
confusionMatrix = confusion_matrix(test_labels, list(map(np.argmax,pred)))
print("The confustion matrix:\n", confusionMatrix)

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
          "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

plt.figure(figsize = (20,17))
ax= plt.subplot()
sns.heatmap(confusionMatrix, annot=True, ax = ax, fmt='g'); #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix when epochs=5' )
ax.xaxis.set_ticklabels(names); ax.yaxis.set_ticklabels(names)

b, t = plt.ylim()  # discover the values for bottom and top
b += 0.5  # Add 0.5 to the bottom
t -= 0.5  # Subtract 0.5 from the top
plt.ylim(b, t)  # update the ylim(bottom, top) values
plt.show()


"""
Conslusion: This model is better than the model which was built by homework 1.
    
"""
