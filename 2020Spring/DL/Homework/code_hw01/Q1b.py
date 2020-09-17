# -*- coding: utf-8 -*-
"""
Spyder Editor

Title: Homework01-01-b
"""
#%%
from keras.datasets import fashion_mnist

from keras.layers import Input, Flatten, Dense
from keras.models import Model

import numpy as np
np.random.seed(9)

#%%
inputLayer = Input(shape=(28,28))
tmp = Flatten()(inputLayer)
tmp = Dense(units=512, activation="relu")(tmp)
outputLayer = Dense(units=10, activation="softmax")(tmp)

#%%
network = Model(inputLayer, outputLayer)

network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

#%%
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images.astype("float32")/255
test_images = test_images.astype("float")/255

#%%
# epochs = 5
from keras.utils import to_categorical

train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)
network.fit(train_images, train_labels01, epochs=5, batch_size=128)
# network.fit(train_images, train_labels, epochs=20, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels01)
print("test accuracy:{}".format(test_acc))

#%%
# Confusion Matrix when epochs = 5
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

#%%
# epochs = 20
from keras.utils import to_categorical

train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)
network.fit(train_images, train_labels01, epochs=20, batch_size=128)
# network.fit(train_images, train_labels, epochs=20, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels01)
print("test accuracy:{}".format(test_acc))

#%%
# Confusion Matrix when epochs = 20
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
ax.set_title('Confusion Matrix when epochs=20')
ax.xaxis.set_ticklabels(names)
ax.yaxis.set_ticklabels(names)

b, t = plt.ylim()  # discover the values for bottom and top
b += 0.5  # Add 0.5 to the bottom
t -= 0.5  # Subtract 0.5 from the top
plt.ylim(b, t)  # update the ylim(bottom, top) values
plt.show()

