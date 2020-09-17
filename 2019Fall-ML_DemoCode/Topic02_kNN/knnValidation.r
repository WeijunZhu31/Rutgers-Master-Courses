#Libraries needed: kknn
#
# Running the kNN on the UCI credit data by using validation technique to find
# the optimal k:

#
# This file works on data available at a well-know repository of data
# histed by University of California-Irvine. The website for this
# dataset:
#  http://archive.ics.uci.edu/ml/datasets/Credit+Approval
# 
# The data contains information about individuals and whether they
# were approved  for credit. The problem is that the name of variables
# have been changed for privacy concerns. So we add 

# The reading and setting up of the data is identical to the knn.r file Refer
# to that file for detailed information.

#cat("This file compares many different classification techniques on a
#credit approval data set from UCI web site.
#
#We are downloading the data from a web site
#Hit Enter to continue\n")
#readline()

# This data has some parts missing (indicated by '?'). To tell the data
# frame that this we add na.string="?". Also note that the data is read
# off a web site directly, and not from a local file. Since there
# are no headers, we add headers A1 to A16 using sapply, and paste
# functions
bankData <-
    read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data",   na.strings="?",
        col.names=sapply(1:16, function(x){return (paste("A",x,sep=""))}))
cat("\nnorw(bankData) ", nrow(bankData), "\n")
#readline()

#Remove rows with <NA> in A2 column. 
bankData <- bankData[!is.na(bankData$A2),]# & !is.na(bankData$A2)&!is.na(bankData$A16),]
#(You can add A3 and A16 as well)
#bankData <- bankData[!is.na(bankData$A2) & !is.na(bankData$A2)&!is.na(bankData$A16),]

#########################################################################
# Running the validation technique to find the best k in kNN  method   #
#########################################################################

cat("\nRunning the validation test to determine the best k for the kNN
   method:\n")
n<-20 #Number of times a random sample is taken for each possible k 

# The following list will have the values of k tested in kList, along with the
# misclassification error. The minusList will contain percentage of those
# rejected that should not have been, plusList contains percentage of 
# those who were accepted and should not have been, and totalList
# contains the percentage of all misclassified items

# Initialize:
kList01<-c()
minusList01<-c()
plusList01<-c()
totalList01<-c()

   # Set the smallest and the largest  k to be testes, and step size between
   # them:
   lowKey=1; highKey=500; stepKey=10
   library("kknn")
   for (k in seq(lowKey,highKey,by=stepKey)){ # testing for each k
     kList01<-c(kList01,k) #attach k to the list
     #cat("\nRunning kNN for k=",k,"\n")
     #initialize error rates:
     knnMinusErrorRate<-0
     knnPlusErrorRate<-0
     knnErrorRate<-0
     for (i in 1:n){ # take n samples as training set
       samp<-sample(1:nrow(bankData),floor(0.8*nrow(bankData)))# 80% training 20% test
       bankDataTrain<-bankData[samp,]
       bankDataTest<-bankData[-samp,]
       #knnModel <- sknn(A16 ~ A3 + A2, k=k, data=bankDataTrain)
       #knnPred<-predict(knnModel, data=bankDataTest)
       #knnConfusion<-table(bankDataTest$A16, knnPred$class)
       knnModel <- kknn(A16 ~ A3 + A2, k=k,train=bankDataTrain,
                               test=bankDataTest,kernel="rectangular")
       # predict class of the test data
       knnPred<-predict(knnModel, data=bankDataTest)
       # using the table function (run ?table for documentation) count the
       # misclassified items in the test data
       knnConfusion<-table(bankDataTest$A16, knnPred)
       # update the error rates for this run 
       knnMinusErrorRate<-knnMinusErrorRate+
                knnConfusion[1,2]/sum(knnConfusion[1,])
       knnPlusErrorRate<-knnPlusErrorRate+
                knnConfusion[2,1]/sum(knnConfusion[2,])
       knnErrorRate<-knnErrorRate+
                (knnConfusion[1,2]+knnConfusion[2,1])/sum(knnConfusion)
       } #end inner for loop
     # compute the average of error rate over n test runs
     knnMinusErrorRate<-knnMinusErrorRate/n
     knnPlusErrorRate<-knnPlusErrorRate/n
     knnErrorRate<-knnErrorRate/n
     # add the error rates for current value of k to the lists:
     minusList01<-c(minusList01,knnMinusErrorRate)
     plusList01<-c(plusList01,knnPlusErrorRate)
     totalList01<-c(totalList01,knnErrorRate)
     #cat("\nError rate for '-':\n",knnMinusErrorRate,"\n")
     #cat("\nError rate for '+'\n",knnPlusErrorRate,"\n")
     #cat("\nError rate knn where k = ",k, ": ",knnErrorRate,"\n")
   } #end outer for loop


# Find the lowest total error rate and the k at which it is attained
bestError=min(totalList);
bestK=kList[which.min(totalList)]

# Plot k versus both positive and negative error rates and the total error rate
plot(kList,totalList, 'l',ylim=c(0,1),
         main=paste("Error rate as a function of k\noptimal k=",bestK))
lines(kList,minusList,col="red")
lines(kList,plusList,col="blue")
print(paste("Optimal k is:" , bestK," results in ",
     min(totalList), " error rate"))

dev.new()
plot(kList,totalList, main="Error rate as a function of k")
# Since the scatter plot is up and down, we smooth it by polynomial
# regression:
lines(kList,predict(lm(totalList~poly(kList,4),
                      data=data.frame(kList=kList,totalList=totalList)),
               data.frame(kList=kList)))

