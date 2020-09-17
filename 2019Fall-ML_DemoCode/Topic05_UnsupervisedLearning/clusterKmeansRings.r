# Libraries needed: none
#
# In this simple script we use the simulated file in.csv which we used
# earlier for the kNN problem. Recall that the data where generated from
# four different bivariate  Gaussian  distributions with four centers
# and four covaraince matrices, see sim.r file. Here we use the
# generated file to test the k-means method for k=4. The resulting fours
# classes are then plotted.
X1=runif(100,-2,2)
X2=runif(100,-2,-1.5)
X1<-c(X1,runif(100,1.5,2))
X2<-c(X2,runif(100,-2,2))
X1<-c(X1,runif(100,-2,2))
X2<-c(X2,runif(100,1.5,2))
X1<-c(X1,runif(100,-2,-1.5))
X2<-c(X2,runif(100,-2,2))

X1<-c(X1,runif(100,-6,6))
X2<-c(X2,runif(100,-6,-5.5))
X1<-c(X1,runif(100,5.5,6))
X2<-c(X2,runif(100,-6,6))
X1<-c(X1,runif(100,-6,6))
X2<-c(X2,runif(100,5.5,6))
X1<-c(X1,runif(100,-6,-5.5))
X2<-c(X2,runif(100,-6,6))

# plot(X1,X2, col="blue",xlab="X1", ylab="X2",pch=20)
# readline("Original data")
mod<-kmeans(cbind(X1, X2), 2)
dev.copy2pdf()
plot(X1,X2, col="white",xlab="X1", ylab="X2", main="clustered data")
points(X1[mod$cluster==1],X2[mod$cluster==1], col="cornflowerblue",
         pch=20)
points(X1[mod$cluster==2],X2[mod$cluster==2], col="orange",pch=20)
# points(dat[dat$cluster==3,"X1"],dat[dat$cluster==3,"X2"], col="red",pch=20)
# points(dat[dat$cluster==4,"X1"],dat[dat$cluster==4,"X2"], col="green",pch=20)
readline("clustered data")
