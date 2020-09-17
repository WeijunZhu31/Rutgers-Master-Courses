# packages needed: EMCluster
# This script generates a d-dimensional k-class mixed Gaussian data, and
# then uses the EMCluster package to estimate group membership and the
# parameters of each group. 
# Simulate

# library(expm)
library(EMCluster)
d=2 #dimension and number of classes
k=3
n1=20 #number of points in each group
n2=30
n3=30
n=n1+n2+n3
realmu=matrix(0,nrow=d,ncol=k) #vector of centes
realmu[,1]=c(2,2)
realmu[,2]=c(-2,2)
realmu[,3]=c(0,-3)
realvar1=matrix(c(1,0,0,1),nrow=d,ncol=d)  # list of covariance matrices
realvar2=matrix(c(1,1,1,1.5),nrow=d,ncol=d)
realvar3=matrix(c(1.2,-.09,-.09,1.2),nrow=d,ncol=d)

x=rnorm(n1, 0, 1) #generate iid standard normal points
x=c(x, rnorm(n2, 0,1))
x=c(x, rnorm(n3, 0,1))
y=rnorm(n1, 0, 1)
y=c(y, rnorm(n2, 0,1))
y=c(y, rnorm(n3, 0,1))
dataM<-matrix(c(x,y),byrow=TRUE,nrow=2) #transform to the specified mean and var
dataM[,1:n1]<-(realvar1)%*%dataM[,1:n1]
dataM[,(n1+1):(n1+n2)]<-(realvar2)%*%dataM[,(n1+1):(n1+n2)]
dataM[,(n1+n2+1):(n1+n2+n3)]<-(realvar3)%*%dataM[,(n1+n2+1):(n1+n2+n3)]
dataM[,1:n1]<-dataM[,1:n1]+matrix(realmu[,1],ncol=1)%*%matrix(rep(1,n1),nrow=1)
dataM[,(n1+1):(n1+n2)]<-dataM[,(n1+1):(n1+n2)]+matrix(realmu[,2],ncol=1)%*%matrix(rep(1,n2),nrow=1)
dataM[,(n1+n2+1):(n1+n2+n3)]<-dataM[,(n1+n2+1):(n1+n2+n3)]+
         matrix(realmu[,3],ncol=1)%*%matrix(rep(1,n3),nrow=1)

# Plot the original data
plot(dataM[1,1:n1],dataM[2,1:n1],pch=20,xlab="x",ylab="y",
      xlim=c(min(dataM[1,])-0.5,max(dataM[1,])+0.5),
      ylim=c(min(dataM[2,])-0.5,max(dataM[2,])+0.5),col="blue")
points(dataM[1,(n1+1):(n1+n2)],dataM[2,(n1+1):(n1+n2)],pch=17,col="blue",xlab=x,ylab="y")
points(dataM[1,(n1+n2+1):(n1+n2+n3)],dataM[2,(n1+n2+1):(n1+n2+n3)],pch=15,col="blue",xlab=x,ylab="y")
readline()
# shuffle
dataM<-dataM[,s<-sample(1:n,n)]

# choose initial values for parameters
readline()
mu1<-mean(dataM[1,samp1<-sample(1:n,floor(n/3))])
mu1<-c(mu1, mean(dataM[2,samp1]))
#mu1=mean(x[samp])
#The following is doen by EMCluster, and are not needed
#var1=cov(t(dataM[,samp1]))
#mu2=mean(dataM[samp2<-sample((1:n)[-samp1],floor(n/3))])
#mu2=c(mu2,mean(dataM[2,samp2]))
#var2=cov(t(dataM[,samp2]))
#mu3<-mean(dataM[1,samp3<-sample((1:n)[-c(samp1,samp2)],
#                   ncol(dataM)-length(samp2)-length(samp1))])
#mu3<-c(mu3,mean(dataM[,samp3]))
#var3<-cov(t(dataM[,samp3]))
#
#p3<-p2<-p1<-rep(1/3,n)
#
#z=rep(0,n)
#z[samp1]=1
#z[samp2]=2
#z[samp3]=3
#tau1=sum(z[z==1])/n
#tau2=sum(z[z==2])/n
#tau3=sum(z[z==3])/n
#count=0
# initialize the EM
em1<-init.EM(t(dataM),nclass=3)
# run EM
em<-emcluster(t(dataM),em1)
# extract each cluster (using Bayes decision rule):
c<-assign.class(t(dataM),em)
plot(dataM[1,c$class==1],dataM[2,c$class==1],pch=20,col="blue",
          xlab="x",ylab="y", 
          xlim=c(min(dataM[1,]),max(dataM[1,])),
          ylim=c(min(dataM[2,]),max(dataM[2,])))
points(dataM[1,c$class==2],dataM[2,c$class==2],pch=20,col="red")
points(dataM[1,c$class==3],dataM[2,c$class==3],pch=20,col="maroon")

