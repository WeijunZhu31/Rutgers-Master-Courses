# -*- coding: utf-8 -*-
""" 
Spyder Editor

Title: Homework01-01-c
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

train_labels01 = to_categorical(train_labels)
test_labels01 = to_categorical(test_labels)


#%%
network.fit(train_images, train_labels01, epochs=5, batch_size=128)

test_loss, test_acc = network.evaluate(test_images, test_labels01)
print("test accuarcy: {}".format(test_acc))


#%%
def class_name(label_num):
    label = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    names=["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
           "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    dictionary = dict(zip(label, names))
    return dictionary[label_num]

while True:
    test_label = int(input("type the index of the label which you want to check: "))
    print("label of this images:", class_name(test_label))
    if input("continue? y/n： ") == "n":
        break


#%%
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


#%%
pred = network.predict(test_images)
for i in range(len(test_images)):
    if test_labels[i] != np.argmax(pred[i]):
        plt.imshow(test_images[i].reshape(28,28), cmap=plt.cm.binary)
        plt.show()
        print("Predicted value of {0} : {1}, \nactural value is : {2}" \
              .format(i, class_name(np.argmax(pred[i])), class_name(test_labels[i])))
        # The second choice
        print("The second choice is : {}".format(class_name(np.argsort(pred[i])[-2])))
        plt.bar(names, pred[i])
        plt.title("The probability of each label")
        plt.show()
        if np.argsort(pred[i])[-2] == test_labels[i]:
            print("The second choice is correct!")
        else:
            print("The second choice is incorrect!")
        if input("continue? y/n: ")=='n':
            break
        
        

