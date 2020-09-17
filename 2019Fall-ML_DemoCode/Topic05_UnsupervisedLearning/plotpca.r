# Plot of principal components of a set of data with two normally
# distributed features.

# Simulate the data first two sets of independent normal variates using
# the standard normal distribution
x1<-rnorm(100,0,1)
x2<-rnorm(100,0,1)
# Generate a linear transformation and transform the data
M<-matrix(c(2,4,3,50),nrow=2)%*%matrix(c(x1,x2), nrow=2)
# Shift the data: After this, M will have two columns following normal
# distribute with some correlation
M[1,]=M[1,]+15
M[2,]<-M[2,]+200


# See the Scatter plot set xlimit so that the scales of X1 and X2 are
# the same
plot(M[1,],M[2,], pch=20, xlab="X1", ylab="X2",xlim=c(0,350), ylim=c(0,350))
# Draw the average (center of gravity) of points
points(mean(M[1,]),mean(M[2,]), pch=18, col="red")
readline("showing the scatter plot of data and the rotation matrix")

# Compute the PCA w/o scaling with the transformed data also returned
pr<-prcomp(t(M), retx=TRUE)

print(summary(pr))
print(pr$rotation)
# Draw the first principal component through the center of the data
lines(c(mean(M[1,]),mean(M[1,])+600*pr$rotation[1,1]),c(mean(M[2,]),mean(M[2,])+600*pr$rotation[2,1]), col="red")
lines(c(mean(M[1,]),mean(M[1,])-600*pr$rotation[1,1]),c(mean(M[2,]),mean(M[2,])-600*pr$rotation[2,1]), col="red")

readline("The line shows the direction of most variance through the center of data")
# Draw the second principal component  
lines(c(mean(M[1,]),mean(M[1,])+600*pr$rotation[2,1]),c(mean(M[2,]),mean(M[2,])+600*pr$rotation[2,2]), col="blue")
lines(c(mean(M[1,]),mean(M[1,])-600*pr$rotation[2,1]),c(mean(M[2,]),mean(M[2,])-600*pr$rotation[2,2]), col="blue")
readline("The blue line is supposed to be perpendicular to the red one, but since the axes are not scaled they don't appear orthogonal") 

plot(pr$x[,1], pr$x[,2], pch=20, xlab="Q1", ylab="Q2", ylim=c(-100,100))
readline("The rotated data")

# Now repeat but with scaled data, the plots depict the scaled data as
# well
readline("Now compute the principal components after scaling the data") 
prs<-prcomp(t(M), retx=TRUE, scale=TRUE)
print(summary(prs))
print(prs$rotation)

plot(M[1,]/sqrt(var(M[1,])),M[2,]/sqrt(var(M[2,])), pch=20, xlab="X1", ylab="X2",)
readline("showing the scatter plot of data and the rotation matrix for scaled data")
lines(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))+
   6*prs$rotation[1,1]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))+
   6*prs$rotation[2,1]), col="red")

lines(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))-
   6*prs$rotation[1,1]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))-
   6*prs$rotation[2,1]), col="red")

lines(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))+
   6*prs$rotation[1,2]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))+
   6*prs$rotation[2,2]), col="blue")

lines(c(mean(M[1,])/sqrt(var(M[1,])),mean(M[1,])/sqrt(var(M[1,]))-
   6*prs$rotation[1,2]),
      c(mean(M[2,])/sqrt(var(M[2,])),mean(M[2,])/sqrt(var(M[2,]))-
   6*prs$rotation[2,2]), col="blue")

readline("And the direction of most variance through the center of scaled data")

plot(prs$x[,1], prs$x[,2], pch=20, xlab="Q1", ylab="Q2",ylim=c(-3,3))
readline("The rotated and scaled data")
