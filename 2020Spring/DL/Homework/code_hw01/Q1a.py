# -*- coding: utf-8 -*-
"""
Spyder Editor

Title: Homework01-01-a
"""
#%%
from keras.datasets import fashion_mnist

from keras import models
from keras import layers

#%%
# split training and test data
(train_images,train_labels),(test_images,test_labels) = fashion_mnist.load_data()

#%%
network = models.Sequential()

network.add(layers.Dense(512, activation="relu", input_shape=(28*28,)))
network.add(layers.Dense(10, activation="softmax"))

#%%
network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

#%%
train_images = train_images.reshape(60000, 28*28)
train_images = train_images.astype("float32")/255

test_images = test_images.reshape(10000, 28*28)
test_images = test_images.astype("float")/255

#%%
from keras.utils import to_categorical

# Make labels from multi-dimensonials to a vector !
train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)

#%%
network.fit(train_images, train_labels01, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels01)
print("test accuarcy: {}".format(test_acc))

#%%
# Confusion Matrix
import numpy as np
from sklearn.metrics import confusion_matrix

pred = network.predict(test_images)
# We can not use "test_labels01" because it handles after "to_categorical" method ! 
# So we use "test_labels".
confusionMatrix = confusion_matrix(test_labels, list(map(np.argmax,pred)))
print("The confustion matrix:\n", confusionMatrix)

#%%
# Heatmap of confusion matrix
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
          "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

fig, ax = plt.subplots(figsize=(20, 17))
sns.heatmap(confusionMatrix, annot=True, ax = ax, fmt='g'); #annot=True to annotate cells

# labels, title and ticks
ax.set_xlabel('Predicted labels')
ax.set_ylabel('True labels')
ax.set_title('Confusion Matrix')
ax.xaxis.set_ticklabels(names, rotation=30)
ax.yaxis.set_ticklabels(names, rotation=30)

b, t = plt.ylim()  # discover the values for bottom and top
b += 0.5  # Add 0.5 to the bottom
t -= 0.5  # Subtract 0.5 from the top
plt.ylim(b, t)  # update the ylim(bottom, top) values
plt.show()


