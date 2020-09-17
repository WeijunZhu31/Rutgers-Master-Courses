# Libraries needed:none
#
# In this simple script we use the simulated file in.csv which we used
# earlier for the kNN problem. Recall that the data where generated from
# four different bivariate  Gaussian  distributions with four centers
# and four covaraince matrices, see sim.r file. Here we use the
# generated file to test the k-means method for k=4. The resulting fours
# classes are then plotted.
dat<-read.csv("in2.csv",header=TRUE)
mod<-kmeans(cbind(dat$X1, dat$X2), 4)
dat<- cbind(dat, cluster=mod$cluster)
plot(dat$X1,dat$X2, col="blue",xlab="X1", ylab="X2",pch=20)
readline("Original data")
dev.new()
plot(dat$X1,dat$X2, col="white",xlab="X1", ylab="X2", main="clustered data")
points(dat[dat$cluster==1,"X1"],dat[dat$cluster==1,"X2"], col="cornflowerblue",
         pch=20)
points(dat[dat$cluster==2,"X1"],dat[dat$cluster==2,"X2"], col="orange",pch=20)
points(dat[dat$cluster==3,"X1"],dat[dat$cluster==3,"X2"], col="green",pch=20)
points(dat[dat$cluster==4,"X1"],dat[dat$cluster==4,"X2"], col="red",pch=20)
readline("clustered data")
# Draw the original clusters:
dev.new()
plot(dat$X1,dat$X2, col="white",xlab="X1", ylab="X2", main="original clusters")
n=nrow(dat)
points(dat[1:(n/4),"X1"],dat[1:(n/4),"X2"], col="cornflowerblue",pch=20)
points(dat[(n/4+1):(n/2),"X1"],dat[(n/4+1):(n/2),"X2"], col="orange",pch=20)
points(dat[(n/2+1):(3*n/4),"X1"],dat[(n/2+1):(3*n/4),"X2"], col="green",pch=20)
points(dat[(3*n/4+1):n,"X1"],dat[(3*n/4+1):n,"X2"], col="red",pch=20)
print("Original clusters")
