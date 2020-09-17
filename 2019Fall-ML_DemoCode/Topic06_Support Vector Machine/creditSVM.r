# This file works on data available at a well-know repository of data
# hosted by the University of California-Irvine. The website for this
# dataset:
#  http://archive.ics.uci.edu/ml/datasets/Credit+Approval
# 
# The data contains information about individuals and whether they
# were approved  for credit. The problem is that the name of variables
# have been changed for privacy concerns. So we add  our own names.

# The data does not have any headers, so we add generic headers A1 to
# A16.

cat("This file compares many different classification techniques on a
credit approval data set from UCI web site.

We are downloading the data from a web site
Hit Enter to continue\n")
readline()

# This data has some parts missing (indicated by '?'). To tell the data
# frame that this we add na.string="?". Also note that the data is read
# off a web site directly, and not from a local file. Since there
# are no headers, we add headers A1 to A16 using sapply, and paste
# functions
bankData1 <-
   read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data",   na.strings="?",
        col.names=sapply(1:16, function(x){return (paste("A",x,sep=""))}))
cat("\nnorw(bankData) ", nrow(bankData1), "\n")

#Remove rows with <NA> in A2 column. 
bankData <- bankData1[!is.na(bankData1$A2),]# & !is.na(bankData1$A2)&!is.na(bankData1$A16),]
#(You can add A3 and A16 as well)
bankData <- bankData1[!is.na(bankData1$A2)&!is.na(bankData1$A3)&!is.na(bankData1$A16),]

# We can now plot the combinations of A2 and A3 for acceptance (in
# blue) and no acceptance (in red)
cat("\n Hit Enter to see the scatterplot of A2 vs A3 for
acceptance cases:\n")
readline()
# Set up the graphics pane:

cat("\nSetting up the graphics pane:\n")
plot( bankData[bankData$A16=="+","A2"],bankData[bankData$A16=="+", "A3"], 
      col="cornflowerblue",pch=18,xlim=c(min(bankData$A2),max(bankData$A2)),
      ylim=c(min(bankData$A3),max(bankData$A3)),
      main="Scatter plot of bankData, A2 and A3 (orange reject, blue accept)", 
       xlab="A2", ylab="A3")
#readline()
points(bankData[bankData$A16=="+","A2"],
		bankData[bankData$A16=="+", "A3"], col="cornflowerblue",pch=18)
#cat("\nHit Enter to add the non-acceptance points:\n")
#readline()
points(bankData[bankData$A16=="-","A2"],
		bankData[bankData$A16=="-", "A3"], col="orange",pch=20)
####################Now build the svm model#############################

# There are several R packages that implement the SVM model. We use the e1071
# library:

cat("\nNow Running the SVM model, loading the e1071 library\n")
library("e1071")

# We now create a set of points to test the model These new set of points form
# a fine grid in the A2-A3 plane. We collect this data into our test data frame
# called newPts0.
# 
# We next let the user choose $k$ and run the kNN algorithm for that k
# on the bankData data. We test the model on newPts0 data frame to see if the new
# points are classified as accepted for bankData or rejected. Finally we plot the
# newPts0 data juxtaposed on the training data. Those predicted to be accepted
# are colored blue, and those predicted to be rejected are colored red. 


newA2<-seq(mA2<-floor(min(bankData$A2)),MA2<-ceiling(max(bankData$A2)),by=1)
newA3<-seq(mA3<-floor(min(bankData$A3)),MA3<-ceiling(max(bankData$A3)),by=0.5)

# generate the grid using outer product (kronocker)
newPts0<-data.frame(A2=kronecker(newA2, rep(1,length(newA3))), 
                    A3=rep(newA3,length(newA2)))

  cat("\nRunning svm for polynomial kernel, c0=1,degree=3")
   cat("\nHit Enter to see the results:\n")
   d=5
   c0=1
   #title= paste("polynomial SVM, deg=",d)
   #svmModel <- svm(A16 ~ A3 + A2,data=bankData,
  #               kernel="polynomial",degree=d,coef0=c0, probability=T)
   title="radial"
   svmModel <- svm(A16 ~ A3 + A2,data=bankData, gamma=1/5,
                  kernel="radial",probability=T)
   print(summary(svmModel))
   print(svmModel)

   readline("Hit enter to run the prediction")
   svmPred<-predict(svmModel, newdata=newPts0,probability = T)
   newPts<-cbind(newPts0,data.frame(A16=svmPred))

   # Preparing for contour plots. The z matrix will contain predicted
   # probabilities for '-' (credit rejected):

   z=matrix(attr(svmPred,"probabilities")[,2],nrow=length(newA2),
             ncol = length(newA3),byrow = T)
   # Setting up the graphics pane. NewPts is a grid of points on the A2-A3
   # plane and then the knnModel is used to predict (red for predicting to reject 
   # credit, blue for predicting accept credit) We use image and contour to
   # draw the boundary between red and blue regions.  Image makes a bit more
   # resolution and instead of just blue and red, it changes color for larger
   # or smaller probabilities. This is sometimes called "heat map"
   
   
   image(newA2,newA3,z,col=rainbow(20,start=.55, end=.1),main=title)
   # For contour we set levels=0.5 so only the boundary between classes are
   # drawn, add = TRUE so that the contour is added to the existing graph

   contour(newA2,newA3,z,levels=c(0.5),add=TRUE,col="darkgreen", 
            drawlabels=FALSE,lwd=2)
   points(newPts[newPts$A16=='+',"A2"],newPts[newPts$A16=='+',"A3"],
					pch='.',cex=2,col="cornflowerblue")
   points(newPts[newPts$A16=='-',"A2"],newPts[newPts$A16=='-',"A3"],
				pch='.',cex=2,col="orange")
   dev.new()
   # Redraw contour without the image heatmap
   contour(newA2,newA3,z,levels=c(0.5),col="darkgreen",
        drawlabels=FALSE,lwd=2,main=title)
   points(newPts[newPts$A16=='+',"A2"],newPts[newPts$A16=='+',"A3"],
					pch='.',cex=2,col="cornflowerblue")
   points(newPts[newPts$A16=='-',"A2"],newPts[newPts$A16=='-',"A3"],
				pch='.',cex=2,col="orange")
   points(bankData[bankData$A16=="+","A2"],
		bankData[bankData$A16=="+", "A3"], col="cornflowerblue",pch=18)
   points(bankData[bankData$A16=="-","A2"],
		bankData[bankData$A16=="-", "A3"], col="orange",pch=20)
   # set up the confusion matrix:
   svm1Model=svm(formula = A16 ~ A3 + A2, data = bankData,
                 kernel="polynomial",degree=d,coef0=c0, probability=T)
   svm1Model=svm(formula = A16 ~ A3 + A2, data = bankData,
                kernel="radial",gamma=1/5, probability=T)
   C= table(bankData$A16, predict(svm1Model,data=bankData))
   print(C)
   print(paste("Error rate:  ", (C[1,2]+C[2,1])/sum(C)))
