# In this file we use the German credit data and use it to classify with
# bagging and randome forests The data are the same as the knn.r file we 
# studied earlier

############################################################################
# Reading in the data:
############################################################################

# This data has some parts missing (indicated by '?'). To tell the data
# frame that this we add na.string="?". Also note that the data is read
# off a web site directly, and not from a local file. Also, since there
# are no headers, we add headers A1 to A16 using sapply, and pase
# functions
dataWebSite<-"http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data"
creditData <-  # Note minor simplification compared to before and use of paste0
   read.csv(dataWebSite,na.strings="?",col.names=paste0('A',1:16)) 

#Remove rows with <NA> in A2 A3 and A16 columns. 
#credit <- credit[!is.na(credit$A2) & !is.na(credit$A2)&!is.na(credit$A16),]
#Remove rows with <NA> in any column
creditData<- creditData[sapply(rownames(creditData), function(i){!any(is.na(creditData[i,]))}),]
cat("Top rows of creditData:\n")
print(head(creditData))
#
cat("Bottom rows of creditData:\n")
print(tail(creditData))

############################################################################
# Building the bagged model 
############################################################################

cat('\n')
readline("Running the random forest model on credit data, treating keywords as 0-1. Hit Enter to continue:")
cat('\n')
library(randomForest)

# Use randomForest for bagging by allowing all features
trainIdx=sample(1:nrow(creditData),600) #trainignsample of size 600

##########Bagging with all features#################
readline("Running bagging using all features:")
creditBag<-randomForest(A16~., mtry=length(colnames(creditData))-1,
                      importance=T, data=creditData[trainIdx,])
creditBagPred<-predict(creditBag, creditData[-trainIdx,])
print("the confusion table for the bagged model:")
print(tblCreditBagged<- table(creditBagPred, creditData[-trainIdx,]$A16))
print(paste("error rate of bagged model: ",(tblCreditBagged[1,2]+tblCreditBagged[2,1])/sum(tblCreditBagged)))

# Now generate the importance plot:
varImpPlot(creditBag)
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditBag$importance[,1]),xlab = "NoSpam")
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditBag$importance[,2]), xlab = "Spam")
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditBag$importance[,3]),xlab="MeanDecreaseAccuracy")
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditBag$importance[,4]),xlab = "MeanDecreaseGini")

##################Now using randome forests by adjusting the subsets of features
# The number of features is now the square root of the total features
readline("Hit Enter to see the results for random forest")
creditForest<-randomForest(A16~., mtry=sqrt(length(colnames(creditData))-1),
                        importance=T, data=creditData[trainIdx,])
creditForestPred<-predict(creditForest, creditData[-trainIdx,])
print("the confusion table for the forest model:")
print(tblCreditForest<- table(creditForestPred, creditData[-trainIdx,]$A16))
print(paste("error rate of forest model: ",(tblCreditForest[1,2]+tblCreditForest[2,1])/sum(tblCreditForest)))

# Now generate the importance plot:
varImpPlot(creditForest)
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditForest$importance[,1]),xlab = "NoSpam")
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditForest$importance[,2]), xlab = "Spam")
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditForest$importance[,3]),xlab="MeanDecreaseAccuracy")
readline("Examine the importance plot of features and hot Enter:")
barplot(sort(creditForest$importance[,4]),xlab = "MeanDecreaseGini")