# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:43:43 2020

@author: naina
"""

import matplotlib.pyplot as plt
import numpy as np

secondprob = []
name = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat","Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
def check(test_images,test_labels ,pred, predicted_labels, flag):
    for i in range(len(test_images)):
        if test_labels[i]!=predicted_labels[i]:
            if not flag:
                plt.imshow(test_images[i].reshape(28,28),cmap=plt.cm.binary)
                plt.show()
            else:
                plt.imshow(test_images[i],cmap=plt.cm.binary)
                plt.show()
           # print("predicted value of ",' : ', name[predicted_labels[i]], " actual value: ", name[test_labels[i]])
            
    
    for i in range(len(pred)):
        fmax = max(pred[i])
        smax = 0
        pos = -1
        for j in range(10):
            if pred[i][j] == fmax:
                continue
            elif pred[i][j] > smax:
                smax = pred[i][j]
                pos = j
        secondprob.append(pos)
    
    count = 0
    for i in range(len(test_labels)):
        if test_labels[i] == secondprob[i]:
            count+=  1
    second_acc_rate = count/len(test_labels)
    print("second_acc_rate ", second_acc_rate)
    
            




def print_cm(cm, labels, hide_zeroes=False, hide_diagonal=False, hide_threshold=None):
    columnwidth = max([len(x) for x in labels] + [5])  # 5 is value length
    empty_cell = " " * columnwidth
    print("    " + empty_cell, end=" ")
    for label in labels:
        print("%{0}s".format(columnwidth) % label, end=" ")
    print()
    for i, label1 in enumerate(labels):
        print("    %{0}s".format(columnwidth) % label1, end=" ")
        for j in range(len(labels)):
            cell = "%{0}i".format(columnwidth) % cm[i, j]
            if hide_zeroes:
                cell = cell if float(cm[i, j]) != 0 else empty_cell
            if hide_diagonal:
                cell = cell if i != j else empty_cell
            if hide_threshold:
                cell = cell if cm[i, j] > hide_threshold else empty_cell
            print(cell, end=" ")
        print()