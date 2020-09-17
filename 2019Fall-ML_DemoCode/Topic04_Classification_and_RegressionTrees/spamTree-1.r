# Libraries needed klaR naivebayes
#
# In this project we compare several variations of the naive Bayes method and
# the tree partitioning problem on detecting spam e-mails. 
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
# Model 3: Use CART on the binary keywords
#####################################################################

cat('\n')
readline("Running the tree model on spam data, treating keywords as 0-1. Hit Enter to continue:")
cat('\n')
library(tree)

treeSpam<- tree(spam ~ ., data=spamData)
#dev.new()
plot(treeSpam);text(treeSpam, pretty=0);title(main="features treated numerically") # This draws the tree
readline("Examine the tree and then hit Enter to contine:")
print(summary(treeSpam)) # This gives a summary including error rate


cat('\n')
readline("Running the tree model on spam data, using keyword frequency. Hit Enter to continue:")
cat('\n')

treeSpamF<- tree(spam ~ ., data=spamData1)
dev.new()
plot(treeSpamF);text(treeSpamF, pretty=0);title(main="treating features as 0-1 factors") # This draws the tree
print(treeSpamF) # Will show the tree in text format
print(summary(treeSpamF)) # This gives a summary including error rate

#################### Using cross validation ####################
cvSpamTree<-cv.tree(treeSpam, FUN=prune.misclass) #prune.misclass ensure misclassification rate is considered
print("Sizes considered: ")
print(cvSpamTree$size)
print("variaous alphas (k's) considered:  ")
print(cvSpamTree$k)
print("Corresponding misclassification rates:")
print(cvSpamTree$dev)
print("plot of misclassification rate:")
dev.new()
plot.tree.sequence(cvSpamTree)
bestSpamTree<-prune.misclass(treeSpam, best=cvSpamTree$size[which.min(cvSpamTree$dev)])
print(bestSpamTree)
dev.new()
plot(bestSpamTree);text(bestSpamTree);title(main="Best Tree for 0-1 features")

print(summary(bestSpamTree))

print("the confusion matrix for the best tree:")

print(tbl<-table(predict(bestSpamTree,type="class",data=spamData),spamData$spam))

print(paste("Error rate for best tree:  ",(tbl[1,2]+tbl[2,1])/sum(tbl)))

