#Q1A part a)
#library(islR)
library(kknn)

# Q3a)
Q3dat<-read.csv("blueOrangeIn.csv")

print(head(Q3dat))
print(tail(Q3dat))
readline()

# Q3b)

N=40
# The grid may not be strictly 40x40 but that's OK as long as it is
# close.
by1=(max(Q3dat$X1)-min(Q3dat$X1))/N
by2=(max(Q3dat$X2)-min(Q3dat$X2))/N


# Set up the grid
newX1<-seq(mX1<-(min(Q3dat$X1)),MX1<-(max(Q3dat$X1)),by=by1)
newX2<-seq(mX2<-(min(Q3dat$X2)),MX2<-(max(Q3dat$X2)),by=by2)

# Creating a grid of points to find their classification under kNN
newPts0<-data.frame(X1=c(), X2=c())
for (i in newX1){
   for (j in newX2){
      newPts0<-rbind(newPts0,data.frame(X1=i, X2=j))
   }
}

for (k in c(1, 10,100,1000,2500, 3500)){
   print(paste("Running kNN for k=",k))
   # make sure to set kernel="rectangular" to avoid different kind of
   # knn
   knnModel <- kknn(Y ~ X2 + X1, k=k,train=Q3dat,
                   test=newPts0,kernel="rectangular")
   knnPred<-predict(knnModel, Q3data=newPts0)
   newPts<-cbind(newPts0,data.frame(Y=knnPred))

   dev.new()
   plot(Q3dat[,"X1"], Q3dat[,"X2"], col="white", main=paste(k,"NN"))
   points(Q3dat[Q3dat$Y=="Blue","X1"],
		Q3dat[Q3dat$Y=="Blue", "X2"], col="blue",pch=20)
   points(Q3dat[Q3dat$Y=="Orange","X1"],
		Q3dat[Q3dat$Y=="Orange", "X2"], col="orange",pch=20)

   points(newPts[newPts$Y=="Blue","X1"],newPts[newPts$Y=="Blue","X2"],
					pch='.',cex=2,col="blue")
   points(newPts[newPts$Y=="Orange","X1"],newPts[newPts$Y=="Orange","X2"],
					pch='.',cex=2,col="orange")
   print("Drawing contours")
   z<-matrix(nrow=length(newX1),ncol=length(newX2))
   for (i in 1:length(newX1))
     for(j in 1:length(newX2)){
      # mapping from linear array to matreix
      z[i,j]=knnModel$prob[j+(i-1)*length(newX2)]
      }
   contour(newX1,newX2,z,levels=c(0.5),col="darkgreen", add=TRUE,
        drawlabels=FALSE,lwd=2,main=paste(k,"NN"))
   cat("Hit Enter to see the heat map:")
   readline()
   dev.new()
   image(newX1,newX2,z,col=rainbow(10,start=.1, end=.55),main=paste(k,"NN"))

   # For contour we set levels=0.5 so only the boundary between classes are
   # drawn, add = TRUE so that the contour is added to the existing graph

   contour(newX1,newX2,z,levels=c(0.5),add=TRUE,col="darkgreen", 
            drawlabels=FALSE,lwd=2)
   points(newPts[newPts$Y=='+',"X1"],newPts[newPts$Y=='+',"X2"],
					pch='.',cex=2,col="blue")
   points(newPts[newPts$Y=='-',"X1"],newPts[newPts$Y=='-',"X2"],
				pch='.',cex=2,col="orange")

}
