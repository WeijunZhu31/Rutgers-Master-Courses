# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:27:15 2020

@author: alizadeh
"""


# Tensorflow2
import tensorflow as tf
from tensorflow import  keras 

fashion_mnist = keras.datasets.fashion_mnist

(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

from keras.layers import Input, Flatten, Dense, Conv2D, MaxPool2D, Dropout
from keras.models import Model
from keras import regularizers
from functools import partial

inputLayer=Input(shape=(28,28,1)) 

tmp=Conv2D(64,(7,7),activation='relu', padding='same',input_shape=(28,28,1))(inputLayer)
tmp=MaxPool2D((2,2))(tmp)
tmp=Conv2D(128,(3,3), activation='relu', padding='same')(tmp)
tmp=Conv2D(128,(3,3), activation='relu', padding='same')(tmp)
tmp=MaxPool2D((2,2))(tmp)
tmp=Conv2D(256,(3,3), activation='relu', padding='same')(tmp)
tmp=Conv2D(256,(3,3), activation='relu', padding='same')(tmp)
tmp=MaxPool2D((2,2))(tmp)
tmp=Flatten()(tmp)
tmp=Dense(128,activation='relu')(tmp)
tmp=Dropout(rate=0.5)(tmp)
tmp=Dense(64,activation='relu')(tmp)
tmp=Dropout(rate=0.5)(tmp)
outputLayer=Dense(units=10,activation='softmax')(tmp)

network=Model(inputLayer,outputLayer)

network.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])
#network.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

import numpy as np
X_train_full=X_train_full.reshape((60000,28,28,1))
X_test=X_test.reshape((10000,28,28,1))

perm=np.random.permutation(range(X_train_full.shape[0]))
X_train_full=X_train_full[perm]
y_train_full=y_train_full[perm]
X_train_full=X_train_full.astype('float32')/255
X_test=X_test.astype('float32')/255
from keras.utils import to_categorical
y_train_full01 = to_categorical(y_train_full)
y_test01 = to_categorical(y_test)
trainingSize=55000
X_train_used=X_train_full[:trainingSize]
y_train_full01_used=y_train_full01[:trainingSize]
val_train=X_train_full[trainingSize:]
val_y_train_full01=y_train_full01[trainingSize:]

#earlyStoppingCB=keras.callbacks.EarlyStopping(patience=10,restore_best_weights=True)
history=network.fit(X_train_used, y_train_full01_used, 
                    validation_data=(val_train,val_y_train_full01),
                    epochs=30, batch_size=128,
                    #callbacks=[earlyStoppingCB]
                    )

test_loss, test_acc=network.evaluate(X_test, y_test01)
print('test_acc:',test_acc)

#plot progress of the algorithm

import pandas as pd
import matplotlib.pyplot as plt
#pd.DataFrame(history.history).plot(figsize=(8, 5))
#plt.grid(True)
#plt.gca().set_ylim(0, 1) # set the vertical range to [0-1]
#plt.show()

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

acc_values=history_dic['accuracy'] # for Tensorflow2
#acc_values=history_dic['acc'] #Tensorflow 1.15

validation_acc_values=history_dic['val_accuracy'] # for Tensorflow2
#validation_acc_values=history_dic['val_acc'] #Tensorflow 1.15

plt.plot(epochs,acc_values, 'bo', label="Training acc")
plt.plot(epochs,validation_acc_values, 'b',label="Validation acc") 
plt.ylabel('Loss')
plt.legend()
plt.show()

# Now examine the performance of the model on various inputs if you wish.

if input("Do you wish to see performance on the test set? y/n")=='y':
    names=["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
           "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]
    
    #pred=network.predict_classes(X_test)
    pred=network.predict(X_test) #pred contains probabilities of each class
    from sklearn.metrics import confusion_matrix
    C=confusion_matrix(y_test, list(map(np.argmax,pred)))
    df=pd.DataFrame(data=confusion_matrix(y_test,list(map(np.argmax,pred))),
                    columns=names,index=names)
    
    print("The confustion matrix:\n",C)
    print(df.head(10))
    #print("The confustion matrix:\n",confusion_matrix(y_test, pred))
    #Visualizing the confusion matrix. If all the colors are in the diagonal 
    #it means all were correctly classified. Off diagonal colors indicate 
    #misclassification
    print("The visualization of the confusion matrix:")
    import seaborn as sns
    sns.heatmap(C,cmap="Spectral")
    #sns.heatmap(confusion_matrix(y_test, pred),cmap="Spectral")
    plt.show()
    input("hit enter to see some of misclassfied items:")
    for i in range(len(X_test)):
        
        plt.imshow(X_test[i].reshape(28,28),cmap=plt.cm.binary)
        plt.show()
        print("predicted value of ",i,':', names[np.argmax(pred[i])], " actual value:", names[y_test[i]])
        plt.bar(height=pred[i],x=names)
        plt.xticks(range(len(names)),names, rotation=90) 
        plt.show()
        if input("continue? y/n")=='n':
            break 