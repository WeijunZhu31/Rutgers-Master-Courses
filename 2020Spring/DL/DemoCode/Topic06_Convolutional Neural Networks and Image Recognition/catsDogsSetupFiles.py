# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:54:17 2020

@author: alizadeh
"""

def processCatsDogsData(baseDir,trainDir,testDir,perm1,perm2):
    import os, shutil
        
    trainCatDir=os.path.join(trainDir,'cats')
    trainDogDir=os.path.join(trainDir,'dogs')
    
    testCatDir=os.path.join(testDir,'cats')
    testDogDir=os.path.join(testDir,'dogs')
    valDir=os.path.join(baseDir,'val_set')
    valCatDir=os.path.join(valDir,'cats')
    valDogDir=os.path.join(valDir,'dogs')

    if 'val_set' not in os.listdir(baseDir):
        os.mkdir(valDir)
        os.mkdir(valCatDir)
        os.mkdir(valDogDir)
        catnames=['cat.{}.jpg'.format(i) for i in perm1[:1000]]
        print(catnames[0:5])
        print(perm1[range(5)])
        for cat in catnames:
            src=os.path.join(trainCatDir, cat)
            dst=os.path.join(valCatDir, cat)
            shutil.copyfile(src, dst)
        dogNames=['dog.{}.jpg'.format(i) for i in perm2[:1000]]
        print(dogNames[0:5])
        print(perm2[range(5)])
        for dog in dogNames:
            src=os.path.join(trainDogDir, dog)
            dst=os.path.join(valDogDir,dog)
            shutil.copyfile(src,dst)
            
            
    trainDirUsed=os.path.join(baseDir,'trainUsed')
    trainUsedCatDir=os.path.join(trainDirUsed,'cats')
    trainUsedDogDir=os.path.join(trainDirUsed,'dogs')
    if 'trainUsed' not in os.listdir(baseDir):
        os.mkdir(trainDirUsed)
        os.mkdir(trainUsedCatDir)
        os.mkdir(trainUsedDogDir)
        catnames=['cat.{}.jpg'.format(i) for i in perm1[1000:]]
        for cat in catnames:
            src=os.path.join(trainCatDir, cat)
            dst=os.path.join(trainUsedCatDir, cat)
            shutil.copyfile(src, dst)
        dogNames=['dog.{}.jpg'.format(i) for i in perm2[1000:]]
        for dog in dogNames:
            src=os.path.join(trainDogDir, dog)
            dst=os.path.join(trainUsedDogDir,dog)
            shutil.copyfile(src,dst)
        
    from keras.preprocessing.image import ImageDataGenerator
    
    # Note: The following is a Python iterator object. It outputs an object
    # that everytime it is called, it generates a new object. Useful for 
    # loops. Here we want to generate the pictures in the directories above 
    # and process them and turn into tensors, so we can feed them to NN

    trainDataGen=ImageDataGenerator(rescale=1.0/255)
    testDataGen=ImageDataGenerator(rescale=1.0/255)
    validDataGen=ImageDataGenerator(rescale=1.0/255)

    
    trainDataGen= trainDataGen.flow_from_directory(
       trainDir,
       target_size=(150,150), #all jpeg pics regardless of size are compressed to 150x150
       batch_size=20,
       class_mode='binary')
    
    valiDataGen=validDataGen.flow_from_directory(
        valDir,
        target_size=(150,150),
        batch_size=20,
        class_mode='binary')
    
    testDataGen=testDataGen.flow_from_directory(
        testDir,
        target_size=(150,150),
        batch_size=20,
        class_mode='binary')
    return trainDataGen, valiDataGen, testDataGen, valDir, trainDirUsed

import os, shutil
import numpy as np


baseDir='datasets/dataset'
trainDir=os.path.join(baseDir, 'training_set')
testDir=os.path.join(baseDir, 'test_set')

perm1=np.random.permutation(len(os.listdir(os.path.join(trainDir,'cats'))))+1
perm2=np.random.permutation(len(os.listdir(os.path.join(trainDir,'dogs'))))+1

trainDataGen, valiDataGen, testDataGen, valDir,trainDirUsed = processCatsDogsData(
    baseDir,trainDir,testDir,perm1,perm2)

import matplotlib.pyplot as plt

for data_batch, label_batch in trainDataGen:
    print('data batch shape:', data_batch.shape)
    print('label batch shape:', label_batch.shape)
    for i in range(data_batch.shape[0]):
        plt.imshow(data_batch[i])
        plt.show()
    if input('more? y/n')=='n':
        break


# Note: trainDataGen and valiDataGen are Python generators which will iterate
# over the pictures in the training set and validations set

# Build the DNN model:


from keras.layers import Input, Flatten, Dense, Conv2D,MaxPool2D, Dropout
from keras.models import Model


import numpy as np

from functools import partial
inputLayer=Input(shape=(150,150,3)) 

from keras import regularizers

ConvLayer=partial(Conv2D,activation='relu', 
                  kernel_initializer='he_uniform', 
                  kernel_regularizer=regularizers.l2(0.001),
                  strides=1,
                  padding='same')
# First set of two Conv2D and one MaxPool2D layer
# Run this first
tmp=ConvLayer(filters=32,kernel_size=(3,3))(inputLayer)
tmp=ConvLayer(filters=32,kernel_size=(3,3))(tmp)
tmp=MaxPool2D((2,2))(tmp)
#tmp=Dropout(0.2)(tmp)
# Second set of two Conv2D and one MaxPool2D layer
# Run this Next and observe how much better the test error get, if any
tmp=ConvLayer(filters=64,kernel_size=(3,3))(tmp)
tmp=ConvLayer(filters=64,kernel_size=(3,3))(tmp)
tmp=MaxPool2D((2,2))(tmp)
#tmp=Dropout(0.2)(tmp)
# Third set of two Conv2D and one MaxPool2D layer
# Run this Next and observe how much better the test error get, if any
tmp=ConvLayer(filters=128,kernel_size=(3,3))(tmp)
tmp=ConvLayer(filters=128,kernel_size=(3,3))(tmp)
tmp=MaxPool2D((2,2))(tmp)
#tmp=Dropout(0.2)(tmp)

tmp=Flatten()(tmp)
tmp=Dense(128,activation='relu',kernel_initializer='he_uniform')(tmp)
#tmp=Dropout(0.2)(tmp)
outputLayer=Dense(units=1,activation='sigmoid')(tmp)

network=Model(inputLayer,outputLayer)

network.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])

history = network.fit_generator(
    trainDataGen,
    steps_per_epoch=100,
    epochs=20,
    validation_data=valiDataGen,
    validation_steps=50)

test_loss, test_acc=network.evaluate_generator(testDataGen) # test set is also geenrated
print("test loss:", test_loss, "test accuracy:", test_acc)
network.summary()


from sklearn.metrics import confusion_matrix

pred=network.predict_generator(testDataGen) #pred contains probabilities of each class

names=['dogs','cats']
#print("The confustion matrix:\n",confusion_matrix(test_labels, list(map(np.argmax,pred))))

#Visualizing the confusion matrix. If all the colors are in the diagonal 
#it means all were correctly classified. Off diagonal colors indicate 
#misclassification
#print("The visualization of the confusion matrix:")
#import seaborn as sns
#sns.heatmap(confusion_matrix(test_labels, list(map(np.argmax,pred))),cmap="Spectral")
#plt.show()


#Now running over misclassified data, printing the real abd predicted
#values, showin gthe actual image, and printing and showing the bar
#graph of probability assigned to each class 
# Now examine the performance of the model on various inputs if you wish.

if input("Do you wish to see performance on the test set? y/n")=='y':
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

    acc_values=history_dic['accuracy'] #Use this for Tensorflow 2.x
    #acc_values=history_dic['acc']  #Use this for Tensorflow 1.1x

    validation_acc_values=history_dic['val_accuracy']
    #validation_acc_values=history_dic['val_acc']

    plt.plot(epochs,acc_values, 'bo', label="Training acc")
    plt.plot(epochs,validation_acc_values, 'b',label="Validation acc")
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

   # for i in testDataGen():
   #     #pred=pred[i]
   #     if test_labels[i]!=np.argmax(pred[i]):
   #         print("ERROR PREDICTION")
   #     plt.imshow(test_images[i])
   #     plt.show()
   #     print("predicted value of data item ",i,':', names[np.argmax(pred[i])], " actual value:", names[test_labels[i][0]])
   #     print(pred[i])
   #     plt.bar(height=pred[i],x=range(10))
   #     plt.xticks(range(len(names)),names, rotation=90)
   #     plt.show()
   #     if input("continue? y/n")=='n':
   #         break




#input('about to remove allnew directories')
#shutil.rmtree(valDir)  # clean up
#shutil.rmtree((trainDirUsed))
