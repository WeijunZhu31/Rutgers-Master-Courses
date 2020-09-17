# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:36:14 2019

@author: alizadeh
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:11:46 2019

@author: farid alizadeh
"""

# In this script we work on the credit approval rating data based on
# only two features. The kNN method is used. We use the validation 
# technique to find a good value of k
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

# load the splitting code
runfile('splitTrainTest.py')

#plot the scatter plot of data
print('Distribution of accpeted (blue) and rejected (orange) with A2 and A3 features:')

pd.Categorical(trainDat['A16'],categories=['+','-'])

sb.relplot(x="A2", y="A3", hue="A16", data=trainDat)
plt.show()

#input('hit enter when done')

####################Now build the knn model#############################

from sklearn.neighbors import KNeighborsClassifier
# we keep track of all k's, and the average error rates for each:
#minusList is for only error in predicting rejection
#plusList is the 
kList=[]
minusList=[]
plusList=[]
totalList=[]
lowKey=1
highKey=501
Step=5 #Number of different k's to test
n=20 #Number of times for each k to generate train/test sets
p=0.2 #fraction of data set aside for test set
runfile('splitTrainTest.py') #load split 

for k in range(lowKey, highKey,Step):
    kList.append(k)
    knnMinusErrorRate=0
    knnPlusErrorRate=0
    knnErrorRate=0
    for i in range(1,n):
        trainDat,testDat=split_train_test(bankData, p) #split data
        classifier = KNeighborsClassifier(n_neighbors=k)
        X=trainDat.iloc[:,[1,2]]
        classifier.fit(X, trainDat.A16)
        yPred=classifier.predict(testDat[['A2','A3']])
        yPredP=classifier.predict_proba(testDat[['A2','A3']])
        C=confusion_matrix(testDat.A16, yPred)
        knnMinusErrorRate+=C[0,1]/(C[0,0]+C[0,1])
        knnPlusErrorRate+=C[1,0]/(C[1,0]+C[1,1])
        knnErrorRate+=(C[1,0]+C[0,1])/sum(sum(C))
    #end inner for
    knnMinusErrorRate/=n #find the avg error over n tests
    knnPlusErrorRate/=n
    knnErrorRate/=n
    minusList.append(knnMinusErrorRate) #store for graphing
    plusList.append(knnPlusErrorRate)
    totalList.append(knnErrorRate)
#end for

bestErrRate=min(totalList)
bestK=kList[np.argmin(totalList)]

classifier=KNeighborsClassifier(n_neighbors=bestK)
X=trainDat.iloc[:,[1,2]]
classifier.fit(X, trainDat.A16)

from sklearn.metrics import classification_report, confusion_matrix  
yTestPred=classifier.predict(testDat.iloc[:,[1,2]])
yTestPredP=classifier.predict_proba(testDat.iloc[:,[1,2]])
C=confusion_matrix(testDat.A16,yTestPred)

   
s='Error rate for k={0:d} is {1:.3f}'
print(s.format(bestK, bestErrRate))
print('confusion matrix:')
print(C)
print(classification_report(testDat.A16,yTestPred))

plt.scatter(kList,totalList,c="green")
plt.show()
plt.scatter(kList,plusList,c="navy")
plt.show()
plt.scatter(kList,minusList,c="orange")
plt.show()

#plot the regions for best k
N=50
x_new=np.linspace(min(bankData.A2),max(bankData.A2),N)
y_new=np.linspace(min(bankData.A3),max(bankData.A3),N)
newPts=pd.DataFrame(columns=(['A2','A3']))
for i in x_new:
    for j in y_new:
        newPts=newPts.append(pd.DataFrame([[i,j]],columns=['A2','A3']))

yPred=classifier.predict(newPts)
yPredP=classifier.predict_proba(newPts)   
newPts["A16"]=yPred
newPts["A16Prob"]=yPredP[:,0]

sb.set()
plt.scatter(newPts.A2[yPred=='+'],newPts.A3[yPred=='+'],c='cornflowerblue', marker='.')
plt.scatter(newPts.A2[yPred=='-'],newPts.A3[yPred=='-'],c='orange', marker='.')
plt.scatter(bankData.A2[bankData.A16=="+"], bankData.A3[bankData.A16=="+"], c='cornflowerblue')
plt.scatter(bankData.A2[bankData.A16=="-"], bankData.A3[bankData.A16=="-"], c='orange',marker='.')

print("plotting new points")
sb.relplot(x="A2",y="A3", hue='A16', data=newPts)

z=np.zeros([len(x_new),len(y_new)])
for i in range(len(x_new)):
    for j in range(len(y_new)):
        z[i,j]=yPredP[i*len(x_new)+j,0]
      
#z=z[:,list(range(z.shape[1]-1,0,-1))] #reverse columns to get correct form
z=z[list(range(z.shape[0]-1,0,-1)),:] #reverse columns to get correct form

print("plotting heatmap")
sb.heatmap(z,cmap="Spectral")
plt.show()
