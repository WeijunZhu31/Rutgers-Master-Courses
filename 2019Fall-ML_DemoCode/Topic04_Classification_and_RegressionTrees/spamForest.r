# Libraries needed randomForest naivebayes
#
# In this file we apply the bagging and the random forest approach to the spam data
# 
# We use the spam data in the UC Irvine archive. Go to the site:
# http://archive.ics.uci.edu/ml/machine-learning-databases/spambase/
# to see documentation about this data set. 
#
# First read the data, it is separated by commas and is in csv format, 
# The data contains no headers and read.csv by default will not add any
# headers
website1<-"http://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
spamData<-read.csv(website1)

# The actual headers are in another site in the UCI archive. It
# contains the title of each column, along with some comments. These
# are lines that start with a "|". Please go to the web site and examine its
# content. That way it would be easier to understand the next few lines. 
# 
# Read data from  the website2 and treat lines starting with a '|' as
# comment (check the origin of the file)
# Make sure not to include any line breaks when you cut and paste:
website2<-"http://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.names"
spamHeaders<-read.table(website2, comment.char="|")

# Turn each item in the first column of spamHeaders to a string
# (otherwise they are treated as levels of some factor by R)  Also start from
# row 2, since row 1 does not have data (check the origin of the file)
# paste will create a vector where every item is turned a string (look at
# the documentation of paste, and also paste0)
tmpNames<-paste(spamHeaders[2:nrow(spamHeaders),1])

# Remove the ":" character from the column headers since the 'tree'
# function does not like them (read documentation by typing ?strsplit)
tmpNames<-strsplit(tmpNames,":")
# Assign the strings in the array tmpNames to the headers of the spamData.
# Note that we can simply assign it to the result of colnames function
colnames(spamData)[1:(ncol(spamData))]<- c(paste(tmpNames),"spam")

# Columns 49 through 54 indicate whether characters ';', '(', '[',
# '!', '$' and '#' occur in the e-mail. Since these types of characters
# cannot appear in a tree formula we replace them with words. Check the
# documentation for R's "sub" function. Also, \\; is used to interpret
# ';' as a semicolon and not the end of an R statement. Ditto for other
# characters:
colnames(spamData)[49]<-sub("\\;","semiColon",colnames(spamData)[49])
colnames(spamData)[50]<-sub("\\(","lparen",colnames(spamData)[50])
colnames(spamData)[51]<-sub("\\[","lsqBrac",colnames(spamData)[51])
colnames(spamData)[52]<-sub("\\!","exclam",colnames(spamData)[52])
colnames(spamData)[53]<-sub("\\$","dollar",colnames(spamData)[53])
colnames(spamData)[54]<-sub("\\#","hashtag",colnames(spamData)[54])
# The data frame is now ready for naive Bayes and tree models

# The following line is optional. You could also turn the spam column to
# factor with levels 0 and 1
spamData$spam<-ifelse(spamData$spam==1,"Spam","NoSpam")
spamData$spam<-as.factor(spamData$spam)

# save two copies one where each word is 0-1 variable (spamData) and the other
# where for word frequencies are considered as numerical variables (spamData1)

spamData1<-spamData

# Transform all variables except the last four into 0-1 factors (the
# table contains *proportion* of words not just whether they occur or not)
for(i in 1:(ncol(spamData)-4)){
    spamData[,i]<-ifelse(spamData[,i]>0,1,0)
    spamData[,i]<-factor(spamData[,i],levels=c(0,1))
}

print(" Here is the spamData data frame after turning word variables
into binary form:")
cat('\n')
print(head(spamData))
print(tail(spamData))
readline()

#####################################################################
# Using random forests on the binary keywords
#####################################################################

cat('\n')
readline("Running the random forest model on spam data, treating keywords as 0-1. Hit Enter to continue:")
cat('\n')
library(randomForest)

trainIdx=sample(1:nrow(spamData),200)

# Use randomForest for bagging by allowing all features
readline("generate a bagged model, all features are used in all trees")
spambag<-randomForest(spam~., mtry=length(colnames(spamData))-1,
           importance=T, data=spamData[trainIdx,])
spamBagPred<-predict(spambag, spamData[-trainIdx,])
print("the confusion table for the bagged model:")
print(tblBagged<- table(spamBagPred, spamData[-trainIdx,]$spam))
print(paste("error rate of bagged model: ",(tblBagged[1,2]+tblBagged[2,1])/sum(tblBagged)))

# Now generate the importance plot:
varImpPlot(spambag)
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spambag$importance[,1]),xlab = "NoSpam")
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spambag$importance[,2]), xlab = "Spam")
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spambag$importance[,3]),xlab="MeanDecreaseAccuracy")
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spambag$importance[,4]),xlab = "MeanDecreaseGini")

# Use randomForest for randome forest by allowing sqrt(features)
readline("generate a random forest model, sqrt(features) are used in all trees")
spamForest<-randomForest(spam~., mtry=sqrt(length(colnames(spamData))-1),
                      importance=T, data=spamData[trainIdx,])
spamForestPred<-predict(spamForest, spamData[-trainIdx,])
print("the confusion table for the forest model:")
print(tblFrst<- table(spamForestPred, spamData[-trainIdx,]$spam))
print(paste("error rate of forest model: ",(tblFrst[1,2]+tblFrst[2,1])/sum(tblFrst)))

# Now generate the importance plot:
varImpPlot(spamForest)
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spamForest$importance[,1]),xlab = "NoSpam")
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spamForest$importance[,2]), xlab = "Spam")
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spamForest$importance[,3]),xlab="MeanDecreaseAccuracy")
readline("Examine the importance plot of features and hit Enter:")
barplot(sort(spamForest$importance[,4]),xlab = "MeanDecreaseGini")