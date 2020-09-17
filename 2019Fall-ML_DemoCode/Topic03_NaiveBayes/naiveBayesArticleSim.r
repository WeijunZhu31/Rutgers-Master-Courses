#Packages needed: naivebaye
#
# In this program we create a simulation to see if an article published in 2016
# is  about presidential primaries or not. Since this is only a simulation, we 
# generate a set of data first, and then build  the Naive Bayes model. 

# The data from article.csv is simulated
#
# This version use the naive Bayes implementation in the "haivebayes" package
#
#
articleData<-read.csv("article.csv")
print(head(articleData))
print(tail(articleData))
# Turn all the column into categorical (factors):
for (i in colnames(articleData)){
  articleData[,i]=as.factor(articleData[,i])
}
readline()
colNames=colnames(articleData)
# Check see if any of the Yes class has 0 occurrence of some variables:
cat("\n number of 1's in each column for priamry = yes:\n")
for (s in colnames(articleData))
   if(s !="primary") cat(", ",s,
      ": ",sum(articleData[articleData$primary=="Yes",s]==1),'\n')
# Check see if any of the No class has 0 occurrence of some variables:
cat("\n number of 1's in each column for primary = no:\n")
for (s in colnames(articleData))
   if(s !="primary")cat(", ",s,
      ": ",sum(articleData[articleData$primary=="No",s]==1),'\n')

# Check see if any of the Yes class has all ones for some variables:
cat("\n number of 0's in each column for priamry = yes:\n")
for (s in colnames(articleData))
   if(s !="primary") cat(", ",s,
      ":",sum(1-(articleData[articleData$primary=="Yes",s]==1)),'\n')
# Check see if any of the Yes class has all ones for some variables:
cat("\n number of 0's in each column for priamry = no:\n")
for (s in colnames(articleData))
   if(s !="primary") cat(",",s,
      ":",sum(1-(articleData[articleData$primary=="No",s]==1)),'\n')

readline()
# run  Naive  Bayes:

# Generate some test data. These are a bunch of arbitrary data for imaginary articles,
# indicating whether each word in the list occurs or does not occur in it: 
dat<-matrix(nrow=7,ncol=length(colNames)-1)
dat[1,]<-rep(1, ncol(dat)) # All words occur
dat[2,]<-rep(0, ncol(dat)) # None of the words occur
dat[3,]<-c(1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,0) #All candidate names occur
dat[4,]<-c(0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0) #No candidate name occur
dat[5,]<-c(0,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1) #Data with non-primary words but has Kasich 
dat[6,]<-c(1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0) #Data with lots of primary words but no Kasich
# Totally random article:
dat[7,]<-sapply(runif(length(colNames)-1),function(x){ifelse(x<0.5,1,0)}) #random choice
testDat<-data.frame(dat)
colnames(testDat)<-colNames[2:length(colNames)]
for (i in colnames(testDat)){
  testDat[,i]=as.factor(testDat[,i])
}

cat("Here is a list 5 test articles data:")
testDat<-data.frame(data=dat)
colnames(testDat)<-colNames[2:length(colNames)]
print(testDat)
cat("hit Enter to continue")
readline()

#######################################################
# Running Naive Bayes 
#######################################################

# Load the klaR library
# library("klaR")
# Load the naivebyes library
library("naivebayes")

# Build the model:
# naiveModel<-NaiveBayes(primary ~ ., data=articleData)
naiveModel1<-naive_bayes(primary ~ ., data=articleData)

# Run the model on the test data frame without any smoothing
predArticle1<-predict(naiveModel1, testDat,type="prob")

print(summary(naiveModel1))
cat("\nResults with no Laplace correction (naiveModel and predArticle):\n")
# print(predArticle1)

# Now build another Naive Bayes model with smoothing alpha=1 beta=10:
naiveModel2 <-naive_bayes(primary ~ ., laplace = 2, data=articleData)
# print(summary(naiveModel2))
cat("\nResults with Laplace correction alpha=1, beta=2 (naiveModel2 and
predArticle2):\n")
predArticle2<-predict(naiveModel2, testDat,type="prob")
# print(predArticle2)
print(cbind(testDat,primary1=predArticle1,primary2=predArticle2,PnoL=predict(naiveModel1,testDat),PL=predict(naiveModel2,testDat)))
readline("Hit Enter to see training set error rate")
print("The error rate for the training data")

# Now check the error rate on the training data:

predTrain1<-predict(naiveModel1,articleData)
print(tbl1<-table(predTrain1, articleData$primary))
print(paste("Error rate w/o Laplace smoothing: ",(tbl1[1,2]+tbl1[2,1])/sum(tbl1) ))

predTrain2<-predict(naiveModel2,articleData)
print(tbl2<-table(predTrain2, articleData$primary))
print(paste("Error rate with Laplace smoothing: ",(tbl2[1,2]+tbl2[2,1])/sum(tbl2) ))

