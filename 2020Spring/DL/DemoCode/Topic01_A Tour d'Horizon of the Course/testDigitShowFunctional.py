# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:29:27 2020

@author: alizadeh
"""

#This script runs over the test data and one by one draws those hand-
#writing images that were misclassified. (You can change != to == in the 
#if statement to look at those which are correctly classified.)

import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix

pred=network.predict(test_images) #pred contains probabilities of each class

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
for i in range(len(test_images)):
    if test_labels[i]!=np.argmax(pred[i]):
        plt.imshow(test_images[i].reshape(28,28),cmap=plt.cm.binary)
        plt.show()
        print("predicted value of ",i,':', np.argmax(pred[i]), " actual value:", test_labels[i])
        print(pred[i])
        plt.bar(height=pred[i],x=range(10))
        plt.show()
        if input("continue? y/n")=='n':
            break
        