# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:11:46 2019

@author: farid alizadeh
"""

# In this file we use the a cresdit approval data and two numerical featuers
# and run the knn algorithm. The value of k is determined by the user. 
# You can try different values and see the effect on error rate
#
# This file works on data available at a well-know repository of data
# hosted by the University of California-Irvine. The website for this
# dataset:
#  http://archive.ics.uci.edu/ml/datasets/Credit+Approval
# 
# The data contains information about individuals and whether they
# were approved  for credit. The problem is that the name of variables
# have been changed for privacy concerns. So we add  our own names.



#Libraries needed are sklearn's KNeighborClassifier numpy pandas matplot and 
#seaborn (for nicer plotting)
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

#In Python data can be downloaded directly from a website
url="http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data"

#In this particular data set missing values are given by a '?' symbol (see the
#data documentation)
bankData=pd.read_csv(url,na_values="?",header=None)
#Make up column titles A1-A16. A16 is the target value: '+' means approved
#and '-' rejected for credit
bankData.columns=list(map(lambda x: 'A'+str(x+1),range(len(bankData.columns))))

#Remove all rows with a null (missing) vlaue
bankData=bankData.dropna()
print(bankData.head())
input('Hit Enter to continue')

# load the splitting code
runfile('splitTrainTest.py')

#split (no need for this script)
#trainDat,testDat=split_train_test(bankData, 0.2)

print('box plots showing dependence of credit approval to A2 and A3 variables:')

bankData.boxplot(column=['A2','A3'],by='A16')
plt.show()

print('Distribution of accpeted (blue) and rejected (orange) with A2 and A3 features:')

pd.Categorical(bankData['A16'],categories=['+','-'])

sb.relplot(x="A2", y="A3", hue="A16", data=bankData)
plt.show()

input('hit enter when done')

#Generate a grid of new data in XY plane and predict:
N=50
x_new=np.linspace(min(bankData.A2),max(bankData.A2),N)
y_new=np.linspace(min(bankData.A3),max(bankData.A3),N)
newPts=pd.DataFrame(columns=(['A2','A3']))

# The following double loop is natural, but for a script language
# like Python  it is very slow. I will shortly replace a 'vectorized'
# version 
for i in x_new:
    for j in y_new:
        newPts=newPts.append(pd.DataFrame([[i,j]],columns=['A2','A3']), ignore_index=True)
 
       
#newPts=newPts.reset_index()


####################Now build the knn model#############################

# The relevant library for knn classification:
from sklearn.neighbors import KNeighborsClassifier

# The user is expected enter a value of k and then we build 
# a knn model

k=int(input('Enter k (0 to end)'))

while (k>0):
   classifier = KNeighborsClassifier(n_neighbors=k)
   X=bankData.iloc[:,[1,2]] #extract columns 1&2 for 'A2' and 'A3'
   classifier.fit(X, bankData.A16) #build the model
   
   yPred=classifier.predict(newPts) #use the model to predict class
   yPredP=classifier.predict_proba(newPts) #and to predict probability
   newPts["A16"]=yPred #Add the predictions to the newPts data
   newPts["A16Prob"]=yPredP[:,0]

   print("plotting new points")
   sb.set()
   plt.scatter(newPts.A2[yPred=='+'],newPts.A3[yPred=='+'],c='cornflowerblue', marker='.')
   plt.scatter(newPts.A2[yPred=='-'],newPts.A3[yPred=='-'],c='orange', marker='.')
   plt.scatter(bankData.A2[bankData.A16=="+"], bankData.A3[bankData.A16=="+"], c='cornflowerblue')
   plt.scatter(bankData.A2[bankData.A16=="-"], bankData.A3[bankData.A16=="-"], c='orange',marker='.')
   #Uncomment to use seaborn software instead
   #sb.relplot(x="A2",y="A3", hue='A16', hue_order=['+','-'],marker='.', data=newPts)
   #sb.scatterplot(x=bankData[bankData.A16=='-'].A2,y=bankData[bankData=='-'].A3,c='orange')
   #sb.scatterplot(x=bankData[bankData.A16=='+'].A2,y=bankData[bankData=='+'].A3,c='cornflowerblue')
   
   xx,yy=np.meshgrid(x_new,y_new)
   zz=yPredP[:,0].reshape(len(xx),len(yy),order='F')#order F means column by column
   plt.contour(xx,yy,zz,levels=[0.5],colors='black')#contour for when prob=1/2
   plt.show()
   input('hit Enter to see the heat map')
  
   plt.contour(xx,yy,zz,levels=[0.5],colors='black')
   # For the heatmap we need to read the rows from bottom to top
   plt.imshow(zz[range(zz.shape[0]-1,0,-1),:],cmap="Spectral",extent=(min(x_new),max(x_new),min(y_new),max(y_new)))
   plt.colorbar()
   
   plt.show()

   
   from sklearn.metrics import classification_report, confusion_matrix
   yTrainPred=classifier.predict(bankData.iloc[:,[1,2]])
   yTrainPredP=classifier.predict_proba(bankData.iloc[:,[1,2]])
   C=confusion_matrix(bankData.A16, yTrainPred)
   s='Error rate for k={0:d} is {1:.3f}'
   print(s.format(k, 1-sum(C.diagonal())/C.sum()))

   print('confusion matrix:')
   print(C)
   print(classification_report(bankData.A16, yTrainPred))
   k=int(input("enter k, (0 to end):"))
   if k != 0:
       newPts=newPts.drop(["A16","A16Prob"],axis=1)
#end of while



