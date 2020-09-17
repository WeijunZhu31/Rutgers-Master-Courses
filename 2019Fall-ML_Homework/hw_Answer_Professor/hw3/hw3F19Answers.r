# Q1a)
print("-----------------Q1a---------------")
#movieDat<-read.csv(unzip("imdb-5000-movie-dataset.zip"),na.string=c("","NA"))
#movieDat<-read.csv(unzip("tmdb-movie-metadata.zip"),na.string=c("","NA"))
movieDat<-read.csv("tmdb_5000_movies.csv",na.string=c("","NA"))

# Important: Movie ID is an integer, but it really is not a real feature. 
# Turn it to a categoriacal data.

movieDat$id <- factor(movieDat$id)
#print(head("movieDat"))
#print(tail("movieDat"))


readline("Data Read. Hit enter to continue:")

#M<-as.matrix(movieDat)

nmovieDat=data.frame(movieDat$revenue)
ncolnames=c("revenue")
for (col in colnames(movieDat))
  if (col!="revenue" & !is.factor(movieDat[,col])){
    ncolnames<-c(ncolnames,col)
    nmovieDat<-cbind(nmovieDat,movieDat[,col])
    #print(col)
  }
colnames(nmovieDat)<-ncolnames

# Imprtant: Under budget and revenue columns there are a lot of 0's. These
# certainly are not real budget or revenue. Treat then as NA. Also, a few vote_average
# vote_count items are zero. They should be turned to NA as well.
nmovieDat$budget<-sapply(nmovieDat$budget, function(x)ifelse(x==0,NA,x))
nmovieDat$revenue<-sapply(nmovieDat$revenue, function(x)ifelse(x==0,NA,x))
nmovieDat$vote_average<-sapply(nmovieDat$vote_average,function(x)ifelse(x==0,NA,x))
nmovieDat$vote_count<-sapply(nmovieDat$vote_count,function(x)ifelse(x==0,NA,x))
nmovieDat<-na.omit(nmovieDat) #Get rid of rows with NA 

print(head(nmovieDat))
print(tail(nmovieDat))


# Q1b)
readline("-----------------Q1b---------------")
print("mean of each feature:")
print(apply(nmovieDat,2, mean))

print("variance of each feature:")
print(apply(nmovieDat,2,var))

print("stdev of each feature:")
print(apply(nmovieDat,2,sd))

# Q1c)
readline("-----------------Q1c---------------")

nmovieDat.pca<-prcomp(~., data=nmovieDat,scale.=T)

print("names of prcomp object:")
print(names(nmovieDat.pca))

print("Centers of principal components:")
print(nmovieDat.pca$center)

print("scales of prcomp object:")
print(nmovieDat.pca$scale)

print("As can be seen, 'center' is the same as 'mean' and 'scale' the same as 'standard deviation' ")
print("prcomp uses means and standard deviation to scale and center the data")
# Q1d
readline("-----------------Q1d---------------")
print("The rotation matrix containing each principal component loadings:")
print(nmovieDat.pca$rotation)

# Q1e
readline("-----------------Q1e---------------")
print("Standard deviation of each principal component (same as singular values of data matrix)")
print(nmovieDat.pca$sdev)

print("variances of each principal component")
print(nmovieDat.pca$sdev^2)

# Connection between PCR and svd:
#
source("normalize.r") # normalize centers columns of a matrix. If the 

# The following function centers columns of M by subtracting average of each 
# column from the corresponding column. If scale=TRUE, then columns are divided 
# by their corresponding standard deviation. By default scale=TRUE

normalize <- function(M, scale=TRUE){
  avg<- matrix(apply(M, 2, mean),ncol=1)
  sig<-matrix(apply(M,2,sd))*sqrt(nrow(M)-1)
  ones<- matrix(rep(1,nrow(M)),ncol=1)
  sig <- ones%*%t(sig)
  avg <- ones%*%t(avg)
  if (!scale) return(M-avg)
  else return ((M-avg)/sig)
}

print("rotation obtained by taking svd of data after re-centering:")



print(svd(normalize(as.matrix(nmovieDat),T))$v)
print("Compare to output of movieDat.pca$rotation above:")
print("Singular values obtained by taking svd of data after re-centering:")
print(svd(normalize(as.matrix(nmovieDat),T))$d)
#print(svd(as.matrix(nmovieDat))$d)
print("Compare to output of variance of each category in the data above:")

# Q1f
readline("-----------------Q1f---------------")
print("percentage contribution of variance each principal component")
print(nmovieDat.pca$sdev^2/sum(nmovieDat.pca$sdev^2))

screeplot(nmovieDat.pca)

# Q1g
readline("-----------------Q1g---------------")
dev.new()
biplot(nmovieDat.pca)

#readline("-----------------Q2---------------")
dev.new()

# Q2a
readline("-----------------Q2a---------------")
set.seed(3)
ssw<-c()
for (i in 2:10){
  km<-kmeans(USArrests, i, nstart=20,iter.max = 100)
  ssw<-c(ssw,km$tot.withinss/km$totss)
}
plot(2:10,ssw, 'b', xlab="k", ylab="within/tot")

# Q2b
readline("-----------------Q2b---------------")
km<-kmeans(USArrests, 3, nstart=20,iter.max = 100)
#print(km$cluster)
#readline()

# Q2c
readline("-----------------Q2c---------------")
color<-c("cornflowerblue", "orange", "maroon")
plot(USArrests[,"Assault"],USArrests[,"Murder"],col=color[km$cluster],pch=20,
     xlab="Assault", ylab="Murder", main="k-means")
text(USArrests[,"Assault"],USArrests[,"Murder"], 
     labels=rownames(USArrests), col=color[km$cluster])

# Q2d
readline("-----------------Q2d---------------")
dev.new()
plot(USArrests[,"Rape"],USArrests[,"Murder"],col=color[km$cluster],pch=20,
     xlab="Rape", ylab="Murder", main="k-means")
text(USArrests[,"Rape"],USArrests[,"Murder"], 
     labels=rownames(USArrests), col=color[km$cluster])

# Q2e
readline("-----------------Q2e---------------")
dev.new()
plot(USArrests[,"Assault"],USArrests[,"Rape"],col=color[km$cluster],pch=20,
     xlab="Assault", ylab="Rape", main="k-means")
text(USArrests[,"Assault"],USArrests[,"Rape"], 
     labels=rownames(USArrests), col=color[km$cluster])

# Q2f
readline("-----------------Q2f---------------")
dev.new()
plot(USArrests[,"UrbanPop"],USArrests[,"Murder"],col=color[km$cluster],pch=20,
     xlab="UrbanPop", ylab="Murder", main="k-means")
text(USArrests[,"UrbanPop"],USArrests[,"Murder"], 
     labels=rownames(USArrests), col=color[km$cluster])

# Q2g
readline("-----------------Q2g---------------")
library("rgl")
plot3d(USArrests[,"Murder"], USArrests[,"Rape"],USArrests[,"Assault"], 
       col=color[km$cluster],xlab="Murder",ylab="Rape",zlab="Assault", main="k-means")
text3d(USArrests[,"Murder"], USArrests[,"Rape"],USArrests[,"Assault"], 
       texts=rownames(USArrests),col=color[km$cluster])


