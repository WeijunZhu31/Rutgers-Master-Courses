# In this file we use the German credit data and use it to classify with
# trees. We experiment with the A2 and A3 features only.

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
creditData <- creditData[!is.na(creditData$A2) & !is.na(creditData$A2)&!is.na(creditData$A16),]
#cat("Top rows of credit:\n")
#print(head(creditData))
#
#cat("Bottom rows of creditData:\n")
#print(tail(creditData))

############################################################################
# Building the tree model with default parameters
############################################################################

# Load the tree library
library(tree)

d1<-.005
s1<-20
#treeModel<-tree(A16~A2+A3,mindev=d1,minsize=s1,data=creditData) 
treeModel<-tree(A16~A2+A3,data=creditData) #default tree

#plot(treeModel, main="default fit") # This just draws the tree with no labeling
plot(treeModel);text(treeModel,pretty=2)

readline("\nHit Enter to see the summary of the default tree model\n")
# The summary function gives basic information about the tree
print(summary(treeModel))

readline("\n Hit Enter to see the complete information about the default tree\n")
# When printing a tree model the software prints the information about each node
# by indenting it according to level of that node in the tree.
print(treeModel)

readline("Hit Enter to continue\n")

#Building the 2-D grid to experiment:

newA2<-seq(mA2<-floor(min(creditData$A2)),MA2<-ceiling(max(creditData$A2)),by=1)
newA3<-seq(mA3<-floor(min(creditData$A3)),MA3<-ceiling(max(creditData$A3)),by=0.5)

# Creating a grid of points to find their classification under tree
#Ineffcient way:
#newPts0<-data.frame(A2=c(), A3=c())
#for (i in newA2){
#   for (j in newA3){
#      newPts0<-rbind(data.frame(A2=i, A3=j), newPts0)
#   }
#}
#Effcient way using the kronocker function:
newPts0<-data.frame(A2=kronecker(newA2, rep(1,length(newA3))), 
                    A3=rep(newA3,length(newA2)))
treePred<-predict(treeModel,newPts0,type="class")
treePredProb<-predict(treeModel,newPts0)

newPts<-cbind(newPts0,data.frame(A16=treePred))
dev.new()
#Plot the original data set:
plot(creditData[,"A2"], creditData[,"A3"], col="white", main="treeModel",
      xlab="A2",ylab="A3")
points(creditData[creditData$A16=="+","A2"],
		creditData[creditData$A16=="+", "A3"],col="cornflowerblue",pch=18)
points(creditData[creditData$A16=="-","A2"],
		creditData[creditData$A16=="-", "A3"], col="orange",pch=20)

points(newPts[newPts$A16=='+',"A2"],newPts[newPts$A16=='+',"A3"],
					pch='.',cex=2,col="cornflowerblue")
points(newPts[newPts$A16=='-',"A2"],newPts[newPts$A16=='-',"A3"],
					pch='.',cex=2,col="orange")

#Now set up data for to use contour for boundary between accept and not accept 
#z[i,j]=Prob[ the point (A2[i],A3[j]) is accepted]. 
#The infficinet way:
#z<-matrix(nrow=length(newA2),ncol=length(newA3))
#for (i in 1:length(newA2))
# for(j in 1:length(newA3)){
#   # mapping from linear array to matreix
#  z[i,j]=predict(treePredProb[,1],data.frame(A2=newA2[i],A3=newA3[j]),type="vector")[2]
#   }
#The efficient way
z=matrix(treePredProb[,1],nrow=length(newA2), ncol = length(newA3),byrow = T)
#One level contour of boundary 1/2 is the boundary between accept and no accpet
contour(newA2,newA3,z,levels=c(0.5),add=TRUE,col="darkgreen", 
            drawlabels=FALSE,lwd=2)

#Draw the partitioning the of the space by the tree:
partition.tree(treeModel,label="A16",ordvars=c("A2", "A3"), add=T)
dev.new()
partition.tree(treeModel,label="A16",ordvars=c("A2", "A3"))


#compute the confusion matrix and the training error rate: 
predTrain<-predict(treeModel,creditData, type="class")
print("The confusion matrix:")
print(tbl<-table(predTrain,creditData$A16))
print(paste("Training Error Rate: ",errRate<-(tbl[1,2]+tbl[2,1])/sum(tbl) ))
