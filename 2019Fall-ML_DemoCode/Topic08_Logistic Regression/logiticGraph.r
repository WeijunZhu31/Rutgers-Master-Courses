# In this file we draw graph of the logistic function

#library(ggplot2)
logistic<-function(x){return(1/(1+exp(-x)))}
plot(x=t<-seq(-5,5,by=0.01),y=logistic(t),'l', 
         xlab="x", ylab="logit(x)",lwd=2, col="orange")
lines(x=t, y=logistic(3*t),col="cornflowerblue")
lines(x=t, y=logistic(.333*t),col="cyan")
lines(x=t, y=ifelse(t<0,0,1),col="black")
legend("right",
   c(expression(paste(k==1)),expression(k==3), expression(k==1/3), expression(k==inf)),
   lwd=rep(2,4),col=c("orange","cornflowerblue","cyan","black"),
   bg="grey96")
readline("hit Enter to see the likelihood function of logistic regression")

############Plot the likelihood and Log Likelihood functions########
print("Suppose we have the logisitc model:\n
      log(p/(1-P)) = b_0 + b_1 x, \n
      and our data is:")

# make up a simple data frame
datFrame=data.frame(y=c(0,0,0,0,1,1,1,1),x=c(1,2,3,4,3,4,5,6))
print(datFrame)

# Build a simple model 
modLog<-glm(y~x, data=datFrame, family=binomial)
print(summary(modLog))
# extract the ML coefficients:
print(paste("bhat0 = ", bhat0<-coefficients(modLog)[1]))
print(paste("bhat1 = ", bhat1<-coefficients(modLog)[2]))
readline()
library("rgl")
# First define likelihood and log likelihood functions
loglik<-function(b0,b1){
  return(sum(datFrame$y*(b0 + b1*datFrame$x))-sum(log(exp(b0+b1*datFrame$x)+1)))
}

likelihood<-function(b0,b1){
  #return( prod(exp(datFrame$y)/(1+exp(-b0-b1*datFrame$x) )))
  return( prod(exp(datFrame$y*(b0+b1*datFrame$x))/(1+exp(b0+b1*datFrame$x) )))
}
      
# Now set a range for b0 and b1:
b0=seq(ifelse(bhat0>=0,
     bhat0*(0.2),bhat0*1.5),ifelse(bhat0>=0,bhat0*(1.5),bhat0*0.2),by=0.05)
b1=seq(ifelse(bhat1>=0,
     bhat1*(0.2),bhat1*1.5),ifelse(bhat1>=0,bhat1*(1.5),bhat1*0.2),by=0.05)
# set up the z coordinates:
z1=z=matrix(nrow=length(b0), ncol=length(b1), 0)
for(i in 1:length(b0))
  for (j in 1:length(b1)){
    z[i,j]=loglik(b0[i],b1[j])
    z1[i,j]=likelihood(b0[i],b1[j])
  }

# Plot likelihood first
readline("hit Enter to see the Likelihood function")
persp3d(b0,b1,z1, col="darkgreen",xlab="b0",ylab="b1",zlab="Likelihood")
# Draw a line showing where the maximum likelihood bhat0 and bha1 point
# is:
lines3d(c(bhat0,bhat0), c(bhat1,bhat1),c(0,max(z1)*1.2),
              lwd=2, col="orange")

# Plot log likelihood first
readline("Now hit Enter to see the Log Likelihood function")
open3d()
persp3d(b0,b1,z, col="lightblue",xlab="b0",ylab="b1",zlab="Log LogLik")
# Draw a line showing where the maximum likelihood bhat0 and bha1 point
# is:
lines3d(c(bhat0,bhat0), c(bhat1,bhat1),c(-modLog$deviance,1),lwd=2, col="pink")

