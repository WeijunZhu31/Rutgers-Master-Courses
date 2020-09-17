# This is answer to Q1. Though we don't need  to write it in R, it is a bit quicker
# this way.
#dat<-read.csv("nbTwitter.csv") # The table is read
dat<-read.csv("twitData.csv") # The table is read
fUp1=c()  # distribution of 1 for Up class for each word
fDown1=c()  # distribution of 1 for Down class for each word
fUp0=c()  # distribution of 0 for Up class for each word
fDown0=c()  # distribution of 0 for Down class for each word
N=nrow(dat)
numUp=sum(dat[,"SP500"]=="Up"); priorUp=numUp/N
numDown=sum(dat[,"SP500"]=="Down"); priorDown=numDown/N
#alpha=0; beta=0 #Adjust the value of alpha and beta.
#ab=ifelse(beta==0,0,alpha/beta)
for (i in colnames(dat))
  if(i != "SP500"){
    fUp1<-c(fUp1,sum(dat[dat$SP500=="Up",i])/numUp)
    fUp0<-c(fUp0,sum(1-dat[dat$SP500=="Up",i])/numUp)
    fDown1<-c(fDown1,sum(dat[dat$SP500=="Down",i])/numDown)
    fDown0<-c(fDown0,sum(1-dat[dat$SP500=="Down",i])/numDown)
}
Q1aDat<-dat[0,]
Q1aDat<-rbind(c(fUp1,priorUp),c(fUp0,priorUp),c(fDown1,priorDown),c(fDown0,priorDown))
colnames(Q1aDat)<-colnames(dat)
rownames(Q1aDat)<-c("f(1|Up)","f(0|Up)","f(1|Down)","f(0|Down)")
print("Q1a) The calculated probabilities without Lapalce smoothing:  ")
print(Q1aDat)
newDat=c(1,0,0,1,0,0,1)
#newDat=c(1,0,1,0,1,0,1)
#newDat=c(1,0,0,1,0,1,0)
#newDat=c(0,1,1,0,1,0,1)
pUp=priorUp*prod(newDat*fUp1+(1-newDat)*fUp0)
pDown=priorDown*prod((1-newDat)*fDown0+newDat*fDown1)

print("pUp=priorUp*prod(newDat*fUp1+(1-newDat)*fUp0)")
print("pDown=priorDown*prod((1-newDat)*fUp1+newDat*fUp0)")
print("Q1b) for new data containing Buy, inflation_down and recession: ")
print(newDat)
print(paste0("Estimated Posterior Prob of Up w/o Laplace smoothing: ",format(pUp,digits=3)))
print(paste0("Estimated Posterior Prob of Down w/o Laplace smoothing:  ", pDown))

alpha=1; beta=2 #Adjust the value of alpha and beta.
#ab=ifelse(beta==0,0,alpha/beta) #not needed
fUp1=c()  # distribution of 1 for Up class for each word
fDown1=c()  # distribution of 1 for Down class for each word
fUp0=c()  # distribution of 0 for Up class for each word
fDown0=c()  # distribution of 0 for Down class for each word
for (i in colnames(dat))
  if(i != "SP500"){
    fUp1<-c(fUp1,(sum(dat[dat$SP500=="Up",i])+alpha)/(numUp+beta))
    fUp0<-c(fUp0,(sum(1-dat[dat$SP500=="Up",i])+alpha)/(numUp+beta))
    fDown1<-c(fDown1,(sum(dat[dat$SP500=="Down",i])+alpha)/(numDown+beta))
    fDown0<-c(fDown0,(sum(1-dat[dat$SP500=="Down",i])+alpha)/(numDown+beta))
}
Q1cDat<-dat[0,]
Q1cDat<-rbind(c(fUp1,priorUp),c(fUp0,priorUp),c(fDown1,priorDown),c(fDown0,priorDown))
colnames(Q1cDat)<-colnames(dat)
rownames(Q1cDat)<-c("f(1|Up)","f(0|Up)","f(1|Down)","f(0|Down)")
print("Q1c) The calculated probabilities with Lapalce smoothing:  ")
print(format(Q1cDat, digits=3))
newDat=c(0,0,0,1,0,1,0)
#newDat=c(1,0,1,0,1,0,1)
#newDat=c(1,0,0,1,0,1,0)
#newDat=c(0,1,1,0,1,0,1)
pUp=priorUp*prod(newDat*fUp1+(1-newDat)*fUp0)
pDown=priorDown*prod((1-newDat)*fDown0+newDat*fDown1)

print("pUp=priorUp*prod(newDat*fUp1+(1-newDat)*fUp0)")
print("pDown=priorDown*prod((1-newDat)*fUp1+newDat*fUp0)")
print("Q1b) for new data containing Buy, inflation_down and recession: ")
print(newDat)
print(paste0("Estimated Posterior Prob of Up with Laplace smoothing:  ",format(pUp,digits=3)))
print(paste0("Estimated Posterior Prob of Down with Laplace smoothing:  ", format(pDown,digits=3)))

