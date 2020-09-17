# Libraries needed rgl
# 
# Plot of principal components of a set of data with three normally
# distributed features.

# Simulate the data first two sets of independent normal variates using
# the standard normal distribution
#library(scatterplot3d)
x1<-rnorm(100,0,1)
x2<-rnorm(100,0,1)
x3<-rnorm(100,0,1)

# Generate a linear transformation and transform the data
M<-matrix(c(2,4,1,3,50,-1,-40,2,1),nrow=3)%*%matrix(c(x1,x2,x2), nrow=3)
# Shift the data: After this, M will have two columns following normal
# distribute with some correlation
M[1,]=M[1,]+15
M[2,]<-M[2,]+200
M[3,]<-M[3,]-100

# See the Scatter plot set xlimit so that the scales of X1 and X2 are
# the same

library(rgl)
open3d()
plot3d(x=M[1,],y=M[2,],z=M[3,], pch=20, xlab="X1", ylab="X2", zlab="X3")
    
readline("showing the scatter plot of data and the rotation matrix")

# Compute the PCA w/o scaling with the transformed data also returned
pr<-prcomp(t(M), retx=TRUE)

print(summary(pr))
print(pr$rotation)
# Draw the first principal component through the center of the data
lines3d(c(mean(M[1,]),mean(M[1,])+200*pr$rotation[1,1]),
        c(mean(M[2,]),mean(M[2,])+200*pr$rotation[2,1]), 
        c(mean(M[3,]),mean(M[3,])+200*pr$rotation[3,1]),col="red")
lines3d(c(mean(M[1,]),mean(M[1,])-200*pr$rotation[1,1]),
        c(mean(M[2,]),mean(M[2,])-200*pr$rotation[2,1]), 
        c(mean(M[3,]),mean(M[3,])-200*pr$rotation[3,1]),col="red")

readline("The line shows the direction of most variance through the center of data")
# Draw the second principal component  
lines3d(c(mean(M[1,]),mean(M[1,])+100*pr$rotation[1,2]),
        c(mean(M[2,]),mean(M[2,])+100*pr$rotation[2,2]), 
        c(mean(M[3,]),mean(M[3,])+100*pr$rotation[3,2]),col="blue")
lines3d(c(mean(M[1,]),mean(M[1,])-100*pr$rotation[1,2]),
        c(mean(M[2,]),mean(M[2,])-100*pr$rotation[2,2]), 
        c(mean(M[3,]),mean(M[3,])-100*pr$rotation[3,2]),col="blue")

readline("The blue line is the second principal component, and is supposed to be perpendicular to the red one, but since the axes are not scaled they don't appear orthogonal") 
lines3d(c(mean(M[1,]),mean(M[1,])+2*pr$rotation[1,3]),
        c(mean(M[2,]),mean(M[2,])+2*pr$rotation[2,3]), 
        c(mean(M[3,]),mean(M[3,])+2*pr$rotation[3,3]),col="orange")
lines3d(c(mean(M[1,]),mean(M[1,])-2*pr$rotation[1,3]),
        c(mean(M[2,]),mean(M[2,])-2*pr$rotation[2,3]), 
        c(mean(M[3,]),mean(M[3,])-2*pr$rotation[3,3]),col="orange")


readline("The orange line is the third Principal component") 

open3d()
plot3d(pr$x[,1], pr$x[,2], pr$x[,3], pch=20, xlab="Q1", ylab="Q2",zlab="Q3")
readline("The rotated data")

# Now repeat but with scaled data, the plots depict the scaled data as
# well
readline("Now compute the principal components after scaling the data") 
prs<-prcomp(t(M), retx=TRUE, scale=TRUE)
print(summary(prs))
print(prs$rotation)

open3d()
plot3d(M[1,]/sqrt(var(M[1,])),M[2,]/sqrt(var(M[2,])), M[3,]/sqrt(var(M[3,])), 
         pch=20, xlab="X1", ylab="X2",)
readline("showing the scatter plot of data and the rotation matrix for scaled data")

lines3d(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))+
   6*prs$rotation[1,1]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))+
   6*prs$rotation[2,1]),
      c(mean(M[3,])/sqrt(var(M[3,])),mean(M[3,])/sqrt(var(M[3,]))+
   6*prs$rotation[3,1]), col="red",)
lines3d(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))-
   6*prs$rotation[1,1]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))-
   6*prs$rotation[2,1]),
      c(mean(M[3,])/sqrt(var(M[3,])),mean(M[3,])/sqrt(var(M[3,]))-
   6*prs$rotation[3,1]), col="red")
readline("First principal component in scaled data")

lines3d(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))+
   6*prs$rotation[1,2]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))+
   6*prs$rotation[2,2]), 
      c(mean(M[3,])/sqrt(var(M[3,])),mean(M[3,])/sqrt(var(M[3,]))+
   6*prs$rotation[3,2]), col="blue")
lines3d(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))-
   6*prs$rotation[1,2]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))-
   6*prs$rotation[2,2]),
      c(mean(M[3,])/sqrt(var(M[3,])),mean(M[3,])/sqrt(var(M[3,]))-
   6*prs$rotation[3,2]), col="blue")
readline("Second principal component in scaled data")

lines3d(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))+
   6*prs$rotation[1,3]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))+
   6*prs$rotation[2,3]),
      c(mean(M[3,])/sqrt(var(M[3,])),mean(M[3,])/sqrt(var(M[3,]))+
   6*prs$rotation[3,3]), col="orange")

lines3d(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))-
   6*prs$rotation[1,3]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))-
   6*prs$rotation[2,3]), 
      c(mean(M[3,])/sqrt(var(M[3,])),mean(M[3,])/sqrt(var(M[3,]))-
   6*prs$rotation[3,3]), col="orange")
readline("Third principal component in scaled data")


open3d()
plot3d(prs$x[,1], prs$x[,2], prs$x[,3], pch=20, xlab="Q1", ylab="Q2", zlab="Q3")
readline("The rotated and scaled data")
