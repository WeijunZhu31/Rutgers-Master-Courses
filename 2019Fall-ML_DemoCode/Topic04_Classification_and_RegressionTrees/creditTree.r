# In this file we use the German credit data and use it to classify with
# trees. All variales will be used. The data are the same as the knn.r file we studied
# earlier

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
#creditData <- creditData[!is.na(creditData$A2) & !is.na(creditData$A2)&!is.na(creditData$A16),]
#Remove rows with <NA> in any column
creditData<- creditData[sapply(rownames(creditData), function(i){!any(is.na(creditData[i,]))}),]
cat("Top rows of creditData:\n")
print(head(creditData))
#
cat("Bottom rows of creditData:\n")
print(tail(creditData))


############################################################################
# Drawing graphs of error rate vs the Gini index and cross entropy
############################################################################

# Before proceeding, let us plot the functions represeting, error rate,
# Gini Index, and entropy for two class case. As you can see all three
# functions are smallest (that is zero) at 0 and 1, and largest at 0.5:

readline("\nPlotting the entropy (green), GINI (blue), and error rate
(red) for two class case. Hit Enter to see\n")

x<-seq(0,1,by=0.01)
plot(x,
    sapply(x,function(y){ifelse((y==0)||(y==1),0,(-y*log(y)-(1-y)*log(1-y))/log(2))}),
    'l',xlab="p", ylab="impurity",col="green")

lines(x,2*x*(1-x), col="blue")
lines(x,sapply(x,function(z){1-max(z,1-z)}),col="red")

############################################################################
# Building the tree model with default parameters
############################################################################

# Load the tree library
library(tree)

# Unlike previous example for kNN where we only used A2 and A3, here we are
# using *all* variables (A1-A15) to classify A16 (approved for credit
# card is+, not approved is -)
# First set aside a train and test set:
trainIdx<-sample(1:nrow(creditData),500)
treeModel<-tree(A16~., data=creditData[trainIdx,]) #A16~. formula means use all variables (A1-A15)

dev.new() #open a new graphics panel
#plot(treeModel, main="default fit") # This just draws the tree with no labeling
plot(treeModel);text(treeModel,pretty=0); title(main="The default fit")
readline("\nHit Enter to see the summary of the default tree model\n")
# The summary function gives basic information about the tree
print(summary(treeModel))
readline("\n Hit Enter to see the complete information about the default tree\n")
# When printing a tree model the software prints the information about each node
# by indenting it according to level of that node in the tree.
print(treeModel)

print("the confusion matrix for the default tree:")
print(tbl1<-table(predict(treeModel,type="class",newdata=creditData[-trainIdx,]),creditData[-trainIdx,]$A16))
print(paste("Error rate for best tree:  ",(tbl1[1,2]+tbl1[2,1])/sum(tbl1)))
readline("Hit Enter to continue\n")

# We now experiment with different values of mindev and minsize (as in
# regression case). Feel free to experiment with different values and
# see how the tree grows or shrinks:
d1<-0
s1<-2
print(paste("Minsize set to ",d1, " and mindev set to ",s1,"\n"))
treeModel1<-tree(A16~., mindev=d1, minsize=s1, data=creditData[trainIdx,])
dev.new()
readline("Hit Enter to see the complete tree without labels\n")
#plot(treeModel1, main=paste0("perfect fit: mindev=", d1, ", minsize=",s1))
plot(treeModel1);text(treeModel,pretty=0); title(main="The complete tree")
readline("\nHit Enter to see the summary of complete (overfitted) Tree Model\n")
print(summary(treeModel1))
readline("Hit Enter to see the complete information about the tree nodes\n")
print(treeModel1)
print("the confusion matrix for the full tree:")
print(tbl2<-table(predict(treeModel1,type="class",newdata=creditData[-trainIdx,]),creditData[-trainIdx,]$A16))
print(paste("Error rate for full tree:  ",(tbl2[1,2]+tbl2[2,1])/sum(tbl2)))
######################Using Cross validation to find the best tree####################
readline("Now we run the `cost-complexity pruning' techniqe to find a good tree:")
cvTree<-cv.tree(treeModel, FUN=prune.misclass) #prune.misclass ensure misclassification rate is considered
dev.new()
plot(bestTree);text(bestTree,pretty=0);title(main="Best tree by cost-complexity pruning")
print("Sizes considered: ")
print(cvTree$size)
print("variaous alphas (k's) considered:  ")
print(cvTree$k)
print("Corresponding misclassification rates:")
print(cvTree$dev)
print("plot of misclassification rate:")
dev.new()
plot.tree.sequence(cvTree)
bestTree<-prune.misclass(treeModel, best=cvTree$size[which.min(cvTree$dev)])
print(bestTree);text(bestTree)
readline("This is the best tree under cost-complexity pruning:")
print(summary(bestTree))

print("the confusion matrix for the best tree:")
print(tbl<-table(predict(bestTree,type="class",newdata=creditData[-trainIdx,]),creditData[-trainIdx,]$A16))
print(paste("Error rate for best tree:  ",(tbl[1,2]+tbl[2,1])/sum(tbl)))
