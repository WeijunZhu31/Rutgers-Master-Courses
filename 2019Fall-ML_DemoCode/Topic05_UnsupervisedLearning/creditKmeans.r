# In this file we use the German credit data and use it to apply PCA on
# numerical features, A2, A3, A8 and A16

############################################################################
# Reading in the data:
############################################################################

# This data has some parts missing (indicated by '?'). To tell the data
# frame that this we add na.string="?". Also note that the data is read
# off a web site directly, and not from a local file. Also, since there
# are no headers, we add headers A1 to A16 using sapply, and pase
# functions
dataWebSite<-"http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data"
credit <-  # Note minor simplification compared to before and use of paste0
   read.csv(dataWebSite,na.strings="?",col.names=paste0('A',1:16)) 

#Remove rows with <NA> in A2 A3 and A15 columns. 
credit <- credit[!is.na(credit$A2) & !is.na(credit$A2)&!is.na(credit$A16),]
print(head(credit))
print(tail(credit))
readline("The top and bottom part of the data")
pairs(credit[,c("A2","A3","A8","A15")])
readline("Pairs function plotting pairs of features against each other")

# Collect the numerical features in a matrix
M<-matrix(c(credit$A2,credit$A3,credit$A8,credit$A15),nrow=nrow(credit),ncol=4)
# Set maximum number of classes (k) in k-means
n1=1
n=20
# Run k means for k=2:n
km=kmTotss=kmBetweenss=kmWithinss=c()
for (i in n1:n){
  km1<-kmeans(M,i,iter.max=1000)
  kmTotss=c(kmTotss,km1$totss)
  kmWithinss=c(kmWithinss,sum(km1$withinss))
  kmBetweenss=c(kmBetweenss,km1$betweenss)
  km<-c(km,km1)
}
# Plot the relative between sum of square, within and total distance, on the
# same graph
#plot(n1:n, kmWithinss/sum(kmWithinss), "b", col="orange",pch=20)
plot(n1:n, kmBetweenss/sum(kmBetweenss), "b", col="blue",pch=20,xlab="k", ylab="SS err")
#lines(n1:n, kmBetweenss/sum(kmBetweenss), "b", col="blue",pch=20)
lines(n1:n, kmWithinss/sum(kmWithinss), "b", col="orange",pch=20)
lines(n1:n, kmTotss/sum(kmTotss), "b", col="red",pch=20)
print("Showing in between class and sum of within class sum of squares of distances for various values of k")

