#dat<-read.csv("in.csv",sep=" ")
dat<-read.csv("blueOrangeIn.csv")
library(kknn)

print(head(dat))
readline()
plot(dat[dat$Y=="Blue","X1"], dat[dat$Y=="Blue","X2"], col="blue",
                      xlim=c(min(dat$X1),max(dat$X1)),
                      ylim=c(min(dat$X2),max(dat$X2)),
                      xlab="X1", ylab="X2", pch=20,
                      main="combined scattered plot")
points(dat[dat$Y=="Orange","X1"], dat[dat$Y=="Orange","X2"], 
                   col="orange", pch=20)

cat("when done looking at the data, press enter\n")
readline()

plot(dat[dat$Y=="Blue","X1"], dat[dat$Y=="Blue","X2"], col="blue",
                      xlim=c(min(dat$X1),max(dat$X1)),
                      ylim=c(min(dat$X2),max(dat$X2)),
                      xlab="X1", ylab="X2", pch=20,
                      main="combined scattered plot")
points(dat[dat$Y=="Orange","X1"], dat[dat$Y=="Orange","X2"], 
                   col="orange", pch=20)

N=50
by1=(max(dat$X1)-min(dat$X1))/N
by2=(max(dat$X2)-min(dat$X2))/N

#newX1<-seq(mX1<-floor(min(dat$X1)),MX1<-ceiling(max(dat$X1)),by=by1)
#newX2<-seq(mX2<-floor(min(dat$X2)),MX2<-ceiling(max(dat$X2)),by=by2)
newX1<-seq(mX1<-(min(dat$X1)),MX1<-(max(dat$X1)),by=by1)
newX2<-seq(mX2<-(min(dat$X2)),MX2<-(max(dat$X2)),by=by2)

# Creating a grid of points to find their classification under kNN
newPts0<-data.frame(X1=c(), X2=c())
for (i in newX1){
   for (j in newX2){
      newPts0<-rbind(data.frame(X1=i, X2=j), newPts0)
   }
}
# Initialize:
#readline("newPts0 set")
kList<-c()
minusList<-c()
plusList<-c()
totalList<-c()
kLow=1; kHigh=900; jump=100
n<-10
library(kknn)
for (k in seq(kLow,kHigh,by=jump)){ # testing for each k
     #cat("\nRunning kNN for k=",k,"\n")
     #initialize error rates:
     knnMinusErrorRate<-0
     knnPlusErrorRate<-0
     knnErrorRate<-0
     for (i in 1:n){ # take n samples as training set
       samp<-sample(1:nrow(dat),1000)# 80% training 20% test
       datTrain<-dat[samp,]
       datTest<-dat[-samp,]
       #knnModel <- sknn(Y ~ X2 + X1, k=k, data=datTrain)
       #knnPred<-predict(knnModel, data=datTest)
       #knnConfusion<-table(datTest$Y, knnPred$class)
       knnModel <- kknn(Y ~ X2 + X1, k=k,train=datTrain,
                               test=datTest,kernel="rectangular")
       # predict class of the test data
       knnPred<-predict(knnModel, data=datTest)
       # using the table function (run ?table for documentation) count the
       # misclassified items in the test data
       knnConfusion<-table(datTest$Y, knnPred)
       # update the error rates for this run 
       knnMinusErrorRate<-knnMinusErrorRate+
                knnConfusion[1,2]/sum(knnConfusion[1,])
       knnPlusErrorRate<-knnPlusErrorRate+
                knnConfusion[2,1]/sum(knnConfusion[2,])
       knnErrorRate<-knnErrorRate+
                (knnConfusion[1,2]+knnConfusion[2,1])/sum(knnConfusion)
       } #end inner for loop
     # compute the average of error rate over n test runs
     knnMinusErrorRate<-knnMinusErrorRate/n
     knnPlusErrorRate<-knnPlusErrorRate/n
     knnErrorRate<-knnErrorRate/n
     # add the error rates for current value of k to the lists:
     kList<-c(kList,k) #attach k to the list
     minusList<-c(minusList,knnMinusErrorRate)
     plusList<-c(plusList,knnPlusErrorRate)
     totalList<-c(totalList,knnErrorRate)
     #cat("\nError rate for '-':\n",knnMinusErrorRate,"\n")
     #cat("\nError rate for '+'\n",knnPlusErrorRate,"\n")
     #cat("\nError rate knn where k = ",k, ": ",knnErrorRate,"\n")
   } #end outer for loop


# Find the lowest total error rate and the k at which it is attained
readline("Loop done.")
bestError=min(totalList);
bestK=kList[which.min(totalList)]

# Plot k versus both positive and negative error rates and the total error rate
plot(kList,totalList, 'b',ylim=c(0,1), xlab="k", ylab="errors",
         main=paste("Error rate as a function of k\noptimal k=",bestK))
lines(kList,minusList,col="orange")
lines(kList,plusList,col="blue")
legend("topleft",
   c(expression(paste("total")),expression(paste("blue as orng")),expression(paste("orng as blue"))),
   lwd=rep(2,3),col=c("black","orange","blue"),
   bg="grey96")

print(paste("Optimal k is:" , bestK," results in ",
     min(totalList), " error rate"))

knnModel <- kknn(Y ~ X2 + X1, k=bestK,train=datTrain,
                 test=newPts0,kernel="rectangular")
knnPred<-predict(knnModel, data=newPts0)
dev.new()
plot(dat[,"X1"], dat[,"X2"], col="white", xlab="X1",ylab="X2", main=paste(bestK,"NN"))
points(dat[dat$Y=="Blue","X1"],
		dat[dat$Y=="Blue", "X2"], col="blue",pch=20)
points(dat[dat$Y=="Orange","X1"],
		dat[dat$Y=="Orange", "X2"], col="orange",pch=20)

newPts<-cbind(newPts0,data.frame(Y=knnPred))
points(newPts[newPts$Y=="Blue","X1"],newPts[newPts$Y=="Blue","X2"],
					pch='.',cex=2,col="blue")
points(newPts[newPts$Y=="Orange","X1"],newPts[newPts$Y=="Orange","X2"],
					pch='.',cex=2,col="orange")
cat("Drawing contours\n")
z<-matrix(nrow=length(newX1),ncol=length(newX2))
for (i in 1:length(newX1))
  for(j in 1:length(newX2)){
   # mapping from linear array to matreix
   z[i,j]=knnModel$prob[j+(i-1)*length(newX2)]
  }
z=z[nrow(z):1,ncol(z):1]
# Contour draws backward so flip z:
# Redraw contour without the image heatmap
contour(newX1,newX2,z,levels=c(0.5),col="darkgreen", add=TRUE,
     drawlabels=FALSE,lwd=2,main=paste(k,"NN"))
cat("Hit Enter to see the heat map:\n")
readline()
dev.new()
image(newX1,newX2,z,col=rainbow(10,start=.1, end=.55),main=paste(bestK,"NN"))
points(newPts[newPts$Y=='Blue',"X1"],newPts[newPts$Y=='Blue',"X2"],
	pch='.',cex=2,col="blue")
points(newPts[newPts$Y=='Orange',"X1"],newPts[newPts$Y=='Orange',"X2"],
		pch='.',cex=2,col="orange")
points(dat[dat$Y=="Blue","X1"],
	dat[dat$Y=="Blue", "X2"], col="blue",pch=20)
points(dat[dat$Y=="Orange","X1"],
	dat[dat$Y=="Orange", "X2"], col="orange",pch=20)

# For contour we set levels=0.5 so only the boundary between classes are
# drawn, add = TRUE so that the contour is added to the existing graph

contour(newX1,newX2,z,levels=c(0.5),add=TRUE,col="darkgreen", 
         drawlabels=FALSE,lwd=2)
points(newPts[newPts$Y=='Blue',"X1"],newPts[newPts$Y=='Blue',"X2"],
			pch='.',cex=2,col="blue")
points(newPts[newPts$Y=='Orange',"X1"],newPts[newPts$Y=='Orange',"X2"],
				pch='.',cex=2,col="orange")

