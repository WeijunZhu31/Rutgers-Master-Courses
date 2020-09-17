# In this script we produce non-parametric logistic regression models and
# compare them to the straight line model. To keep thing at the same level,
# we only include the quantitative variables A2 and A3 as our features.
# We experiment with linear model with boundary expressed as 
#              b0+b1*A2+b1*A2+b2*A3=0
# The polynomial model (chosen as the best among all polynomials of degree
# upto 4 in A2 times polynomials of degree up to 4 for A3. We also
# experiment with B-spline with df=4 for A2 and A3.
#
###########Read the data and setup###############
# This file works on data available at a well-know repository of data
# histed by University of California-Irvine. The website for this
# dataset:
#  http://archive.ics.uci.edu/ml/datasets/Credit+Approval
# 
# The data contains information about individuals and whether they
# were approved  for credit. The problem is that the name of variables
# have been changed for privacy concerns. So we add 

# The data does not have any headers, so we add generic headers A1 to
# A16.

readline("In this file we compare various non-parametric different classification 
techniques on a credit approval data set from UCI web site.

We are downloading the data from a web site
Hit Enter to continue\n")

# This data has some parts missing (indicated by '?'). To tell the data
# frame that this we add na.string="?". Also note that the data is read
# off a web site directly, and not from a local file. Also, since there
# are no headers, we add headers A1 to A16 using sapply, and pase
# functions
credit <-
read.csv("http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data",
   na.strings="?",
   col.names=sapply(1:16, function(x){return (paste("A",x,sep=""))}))
#cat("\nnorw(credit) ", nrow(credit), "\n")
#readline()

#Remove rows with <NA> in A2 column. 
credit <- credit[!is.na(credit$A2),]# & !is.na(credit$A2)&!is.na(credit$A16),]
#(You can add A3 and A16 as well)
#credit <- credit[!is.na(credit$A2) & !is.na(credit$A2)&!is.na(credit$A16),]
cat("Top rows of credit:\n")
print(head(credit))
readline()

cat("Bottom rows of credit:\n")
print(tail(credit))
readline()



# We plot the combinations of A2 and A3 for acceptance (in
# blue) and no acceptance (in red)
readline("\n Hit Enter to see the scatterplot of A2 vs A3 for
acceptance cases:\n")
# Set up the graphics pane:

cat("\nSetting up the graphics pane:\n")
plot(credit[,"A2"], credit[,"A3"], col="white",xlab="A2", ylab="A3",
      main="Linear Logistic")

#readline()
points(credit[credit$A16=="+","A2"],
		credit[credit$A16=="+", "A3"], col="cornflowerblue",pch=18)
cat("\nHit Enter to add the non-acceptance points:\n")
#readline()
points(credit[credit$A16=="-","A2"],
		credit[credit$A16=="-", "A3"], col="orange",pch=20)
x<-sort(credit$A2)
####################Build the Linear Logistic regression#############
cat("\nApplying the logistic regression to the credit data.\n")

logitModel <- glm(A16 ~ A2 + A3, family=binomial, data=credit)
print("summary of logitModel")
print(summary(logitModel))
print(summary(logitModel))
print("Drawing the boundary by logistic regression (dark green)")
print("Note that this exactly the equation bhat0+bhat1*A2+ bhat2*A3=0")
print(paste(logitModel$coefficients[1],"+ ",
            logitModel$coefficients[2]," * A2 + ",
            logitModel$coefficients[3]," * A3 = 0"))
#readline()
# Draw the boundary line: a=intercept=-coeff[1]/coeff[3]
#                         b=slope=-coeff[2]/coeff[3]
abline(a=-logitModel$coefficients[1]/logitModel$coefficients[3],
       b=-logitModel$coefficients[2]/logitModel$coefficients[3],
       lwd=2,col="darkgreen")
newA2<-seq(mA2<-floor(min(credit$A2)),MA2<-ceiling(max(credit$A2)),by=1)
newA3<-seq(mA3<-floor(min(credit$A3)),MA3<-ceiling(max(credit$A3)),by=1/2)
newPts<-data.frame(A2=c(), A3=c())
for (i in newA2){
   for (j in newA3){
      newPts<-rbind(newPts,data.frame(A2=i, A3=j)) #add rows
   }
}
logitPred<-predict(logitModel, newPts, type="response")
newPts<-cbind(newPts,data.frame(A16=ifelse(logitPred>0.5,'+','-')))
points(newPts[newPts$A16=='+',"A2"],newPts[newPts$A16=='+',"A3"],
		pch='.',cex=2,col="cornflowerblue")
points(newPts[newPts$A16=='-',"A2"],newPts[newPts$A16=='-',"A3"],
	pch='.',cex=2,col="orange")
points(credit[credit$A16=="+","A2"],
		credit[credit$A16=="+", "A3"], col="cornflowerblue",pch=20)
points(credit[credit$A16=="-","A2"],
		credit[credit$A16=="-", "A3"], col="orange",pch=20)
print("We now generate a \"heat map\"")
print("The orange areas corresponds to high probability of '-'")
print("The blue areas corresponds to high probability of '+'")
print("The other areas correspond to probabilities to more modest probabilites")
readline("Hit Enter to see the heat map")

dev.new()
# image function creates a "heat map" that is for the range of
# values z (here z=Pr[y=1]). We specify the range of colors from
# red (code 0) to blue (code 2/3=0.67) and in 20 levels. 
z<-matrix(nrow=length(newA2),ncol=length(newA3))
for (i in 1:length(newA2))
  for(j in 1:length(newA3)){
   # mapping from linear array to matreix
   z[i,j]=logitPred[j+(i-1)*length(newA3)]
   }
image(newA2,newA3,z,col=rainbow(20,start=0.09, end=0.67),
       main=paste("Linear Logistic"))
# For contour we set levels=0.5 so only the boundary between classes are
# drawn, add = TRUE so that the contour is added to the existing graph
# Note that this contour is exactly the line bhat0+bhat1*A2+bhat2*A3=0

#contour(newA2,newA3,z,levels=c(0.5),add=TRUE,col="darkgreen", 
#         drawlabels=FALSE,lwd=2)
abline(a=-logitModel$coefficients[1]/logitModel$coefficients[3],
       b=-logitModel$coefficients[2]/logitModel$coefficients[3],
       lwd=2,col="darkgreen")
points(newPts[newPts$A16=='+',"A2"],newPts[newPts$A16=='+',"A3"],
		pch='.',cex=2,col="cornflowerblue")
points(newPts[newPts$A16=='-',"A2"],newPts[newPts$A16=='-',"A3"],
	pch='.',cex=2,col="orange")


##################Now build the Nonparametric logistic model#########
library(splines)
d<-4
#nlogitModel <- glm(A16 ~ (A2+I(A2^2) +I(A2^3))*(A3+I(A3^2)+I(A3^3)), family=binomial,data=credit)
#nlogitModel <- glm(A16 ~ poly(A2,d)*poly(A3,d), family=binomial,data=credit)
#type<-"polynomial"
nlogitModel <- glm(A16 ~bs(A2,df=d)*bs(A3,df=d) , family=binomial, data=credit)
type<-"B-spline"
#nlogitModel <- glm(A16 ~ns(A2,df=d)*ns(A3,df=d) , family=binomial, data=credit)
#type<-"Natural-spline"
print(paste("Developing the nonparametric logistic Model ",type," Hit Enter:"))
print(summary(nlogitModel))

# For graphics drawing we generate a grid of data and put them on the
# data frame newPts. NewA2 and newA3 are the A2 and A3 coordinates of
# new points ranging from smallest to largest A2 (A3), and with
# increments of 1 (0.5 for A3):

#Now set up the newPts data frame:
newPts<-data.frame(A2=c(), A3=c())
for (i in newA2){
   for (j in newA3){
      newPts<-rbind(newPts,data.frame(A2=i, A3=j)) #add rows
   }
}
# build the predictor for all the new points
nlogitPred<-predict(nlogitModel, newPts, type="response")

# Add the classification for all the new points made by QDA
newPts<-cbind(newPts,data.frame(A16=ifelse(nlogitPred>0.5,'+','-')))


type<-"B Spline"
d<-extractAIC(nlogitModel)[1]
z<-matrix(nrow=length(newA2),ncol=length(newA3))
for (i in 1:length(newA2))
  for(j in 1:length(newA3)){
   # mapping from linear array to matreix
   z[i,j]=nlogitPred[j+(i-1)*length(newA3)]
   }
# Redraw contour without the image heatmap
print("We now show the orange (predict rejection) and blue (predict acceptance")
readline("Hit Enter to see")

dev.new()
contour(newA2,newA3,z,levels=c(0.5),col="darkgreen",
     drawlabels=FALSE,lwd=2,
     main=paste("nonparametric logistic, degree=",d,", type= ", type))
points(newPts[newPts$A16=='+',"A2"],newPts[newPts$A16=='+',"A3"],
		pch='.',cex=2,col="cornflowerblue")
points(newPts[newPts$A16=='-',"A2"],newPts[newPts$A16=='-',"A3"],
	pch='.',cex=2,col="orange")
points(credit[credit$A16=="+","A2"],
		credit[credit$A16=="+", "A3"], col="cornflowerblue",pch=20)
points(credit[credit$A16=="-","A2"],
		credit[credit$A16=="-", "A3"], col="orange",pch=20)


print("We now generate a \"heat map\"")
print("The orange areas corresponds to high probability of '-'")
print("The blue areas corresponds to high probability of '+'")
print("The other areas correspond to more modest probabilites")
readline("Hit Enter to see the heat map")

dev.new()
# image function creates a "heat map" that is for the range of
# values z (here z=Pr[y=1]). We specify the range of colors from
# red (code 0) to blue (code 2/3=0.67) and in 20 levels. 
image(newA2,newA3,z,col=rainbow(20,start=0.09, end=0.67),
       main=paste("nonparametric logistic, df=",d,", type= ", type))
# For contour we set levels=0.5 so only the boundary between classes are
# drawn, add = TRUE so that the contour is added to the existing graph


contour(newA2,newA3,z,levels=c(0.5),add=TRUE,col="darkgreen", 
         drawlabels=FALSE,lwd=2)
points(newPts[newPts$A16=='+',"A2"],newPts[newPts$A16=='+',"A3"],
		pch='.',cex=2,col="cornflowerblue")
points(newPts[newPts$A16=='-',"A2"],newPts[newPts$A16=='-',"A3"],
	pch='.',cex=2,col="orange")
