# This is a simulated one dimensional mixed Gaussian model using the EM
# algorithm. In this file no package is used, and the algorithm is
# directly implemented.

# Simulate

n1=20  #Two groups, number of items in each
n2=30
realmu1=2 #mean of each group
realmu2=6
realvar1=2.8  #variance of each group
realvar2=2.8
x=rnorm(n1, realmu1, sqrt(realvar1))  #Simulating data
x=c(x, rnorm(n2, realmu2,sqrt(realvar2)))
# shuffle 
x=x[s<-sample(1:length(x),length(x))]

plot(x,rep(1,length(x)),pch=20,col="blue",xlab=x,ylab="")
readline()
# Initialization:
# choose initial values for parameters
mu1=mean(x[samp<-sample(1:length(x),floor(length(x)/2))])
#mu1=mean(x[samp])
var1=var(x[samp])
mu2=mean(x[-samp])
var2=var(x[-samp])
p1=rep(.5,length(x))
p2=1-p1
print("x:")
print(x)

# set initial value for the latent 0-1 variables z indicating which group
# each point belongs to
z=rep(0,length(x))
z[-samp]=1
tau2=sum(z)/length(z) # initial estimate of probability of each group
tau1=1-tau2
count=0
print("Initial grouping:")
print(paste("mu1= ",mu1," mu2= ", mu2, " var1= ", var1, " var2=", var2, " tau1= ",tau1))
print("population 1:")
print(x[z==0])
print("population 2:")
print(x[z==1])
print(z)

# find inverse permuation:
sinv<-function(s)return(sapply(1:length(s), function(x)return(which(s==x))))
while (count<100) {
  # Plot and color current clusters
  plot(x[z==0],rep(1,length(x[z==0])),pch=20,col="blue",xlab=x,ylab="",
       xlim=c(min(x)-1,max(x)+1),ylim=c(0,3))
  points(x[z==1],rep(1,length(x[z==1])),pch=20,col="red")
  points(x[sinv(s)][1:n1],rep(2,n1),col="blue")
  points(x[sinv(s)][(n1+1):(n1+n2)],rep(2,n2),col="red")
  # Expectation step: uses Bayes decision rule to assign groups based on
  # current estimate of parameters (mu1,mu2, sigma1, sigma2, tau1)
  count=count+1
  newz=rep(0,length(x))
  for (i in 1:length(x)){
     posterior1= dnorm(x[i],mu1,sqrt(var1))*tau1
     posterior2= dnorm(x[i],mu2,sqrt(var2))*tau2
     p1[i]=posterior1/(posterior1+posterior2)
     newz[i]=ifelse(posterior1<posterior2, 1,0)
  }
  if(sum(newz-z)==0) # check convergence 
     {print("breaking");break}
  z=newz
  p2=1-p1

  # Maximization (Use current probabilities p1, p2 to find ML estimate of
  # parameters
  tau2=sum(z)/length(z)
  tau1=1-tau2
  mu1<-sum(x[z==0]*p1[z==0])/sum(p1[z==0]) #weighted mean
  mu2<-sum(x[z==1]*p2[z==1])/sum(p2[z==1])

  var1<-sum((x[z==0]-mu1)^2*p1[z==0])/sum(p1[z==0]) #weighted variance
  var2<-sum((x[z==1]-mu2)^2*p2[z==1])/sum(p2[z==1])
   
  print("===================================")
  print(paste("Round ", count,": "))
  print(paste("mu1= ",mu1," mu2= ", mu2, " var1= ", var1, " var2=", var2, " tau1= ",tau1))
  #flag=as.numeric(readline("Hit enter to continue, 0 to stop"))
  #print("population 1:")
  #print(x[z==0])
  #print("population 2:")
  #print(x[z>0])
  print("p1:")
  print(p1)
  print("z:")
  print(z)
  #if (flag==0) break
  readline()
}
 
print("real values: realmu1, realmu2,realvar1,realvar2")
print(paste(realmu1, realmu2,realvar1,realvar2))

print("EM values: mu1, mu2,var1,var2")
print(paste(mu1, mu2,var1,var2))



# plot clusters found by EM and compare to the original clusters:
plot(x[z==0],rep(1,length(x[z==0])),pch=20,col="blue",xlab=x,ylab="",xlim=c(min(x)-1,max(x)+1),ylim=c(0,3))
points(x[z==1],rep(1,length(x[z==1])),pch=20,col="red")
points(x[sinv(s)][1:n1],rep(2,n1),col="blue")
points(x[sinv(s)][(n1+1):(n1+n2)],rep(2,n2),col="red")
