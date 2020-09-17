library(tidyverse)
library(naivebayes)
library(e1071)
library(caret)
library(kknn)


set.seed(9)
              ######### Part I: Create the data #########
# A. Generate 600 independent numbers normally distributed with mean 0 and standard deviation 1.
raw_data <- rnorm(600, mean=0, sd=1)
raw_data

# B. Organize these numbers into a 2 * 300 matrix, called data.
data <- matrix(raw_data, nrow=2, ncol=300)
# dim(data)

# C. 
sigmaR <- matrix(c(149,-47,-47,209), ncol=2, nrow=2)
# sigmaR <- matrix(c(149,-47,-47,209), ncol=2, nrow=2)
data <- t(data) %*% sigmaR

# D.
muR <- c(680,700)
data_R <- data + muR
data_R <- data.frame(data_R)

# Repeat C & D to generate the blue points
sigmaB <- matrix(c(200,15,15,250), ncol=2, nrow=2)
data <- matrix(raw_data, nrow=2, ncol=300)
data <- t(data) %*% sigmaB

muB <- c(10,550)
data_B <- data + muB
data_B <- data.frame(data_B)


                ######### Part II #########
# 3b).
# dim(data_R)
# class(data_R)

data_B[,3] <- 'blue' 
data_B
data_R[,3] <- 'red'
data_R

simData <- rbind(data_B,data_R)
names(simData) <- c("X1", "X2", "Y")
simData


# 3c). Plot the simData
simData$Y <- as.factor(simData$Y)
simData$Y

plot01 <- ggplot(data = simData, mapping = aes(x = X1, y = X2, color = Y)) + 
  geom_point() + 
  scale_color_manual(breaks = c('0','1'), values = c('blue','red'))
plot01

# 3d). Create the test set named testDF
raw_data_test <- rnorm(400, mean=0, sd=1)
data_test <- matrix(raw_data_test, nrow=2, ncol=200)
dim(data_test)
sigmaR <- matrix(c(149,-47,-47,209), ncol=2, nrow=2)
data_test <- t(data_test) %*% sigmaR
muR <- c(680,700)
data_R_test <- data_test + muR
data_R_test <- data.frame(data_R_test)

sigmaB <- matrix(c(200,15,15,250), ncol=2, nrow=2)
data_test <- matrix(raw_data_test, nrow=2, ncol=200)
data_test <- t(data_test) %*% sigmaB

muB <- c(10,550)
data_B_test <- data_test + muB
data_B_test <- data.frame(data_B_test)

data_B_test[,3] <- 'blue' 
data_B_test
data_R_test[,3] <- 'red'
data_R_test

testDF <- rbind(data_B_test,data_R_test)
names(testDF) <- c("X1", "X2", "Y")
testDF
testDF$Y <- as.factor(testDF$Y)


########################################################################################
# 3e). Bayes Decision Rule
# PDF of Bayes Decision Rule:
simData_1 <- simData[,1:2]
bayes_decision_PDF <- function(x, sigma, mu){
  log((1/(2*pi*(det(sigma^2)))) * 
        exp((-1/2)*(t(x - mu)) %*% solve(sigma^2) %*% (x - mu)))
}

prob_blue <- c()
prob_red <- c()
for (x in seq(1, ncol(t(simData_1)))){
  red_prob = bayes_decision_PDF(as.numeric(t(simData_1)[1:2,x]), sigmaR, muR)
  prob_red[x] <- red_prob 
  blue_prob = bayes_decision_PDF(as.numeric(t(simData_1)[1:2,x]), sigmaB, muB)
  prob_blue[x] <- blue_prob 
  if (red_prob>=blue_prob){
    simData_1[x,3] <- 'red'
  } else {
    simData_1[x,3] <- 'blue'
  }
}

correct_num_1 = 0
for (i in 1:nrow(simData_1)) {
  if (simData_1[i,3] == simData[i,3]){
    correct_num_1 = correct_num_1 + 1
  }
}

cat('The error rate of the Bayes Decision Rule for the simData is: ', 1-correct_num_1/600)


prob_matrix <- rbind(prob_blue, prob_red)
# prob_matrix <- t(prob_matrix) # 600 2



# plot the grid plot
# x1 <- seq(floor(min(simData[1])), ceiling(max(simData[1])), by = 1)
# y1 <- seq(floor(min(simData[2])), ceiling(max(simData[2])), by = 1)
z1 <- matrix(prob_matrix, nrow = 200,
             ncol = 200, byrow = T)

contour(x1=1:200, y1=1:200, z1, levels = c(0.5), col = 'maroon', drawlabels = FALSE,
        lwd = 2, main = 'Boundary of Bayes Decision')
points(simData[simData$Y == 'red', 1], simData[simData$Y == 'red', 2],
       pch='.',cex=2,col="red")
points(simData[simData$Y == 'blue', 1], simData[simData$Y == 'blue', 2],
       pch='.',cex=2,col="blue")


# 3f). Bayes Decision Rule for testDF: 
testDF_1 <- testDF[,1:2]
for (x in seq(1, ncol(t(testDF_1)))){

  red_prob = bayes_decision_PDF(as.numeric(t(testDF_1)[1:2,x]), sigmaR, muR)
  blue_prob = bayes_decision_PDF(as.numeric(t(testDF_1)[1:2,x]), sigmaB, muB)
  
  if (red_prob>=blue_prob){
    testDF_1[x,3] <- 'red'
  } else {
    testDF_1[x,3] <- 'blue'
  }
}


correct_num = 0
for (i in 1:nrow(testDF)) {
  if (testDF[i,3] == testDF_1[i,3]){
    correct_num = correct_num + 1
  }
}

cat('The error rate of the Bayes Decision Rule for the testDF is: ', 1-correct_num/400)

########################################################################################

              ######### Part III: Learning Step #########
# 3g).
# shuffle and sampling the simData & testDF
simData_shuffle <- sample(nrow(simData))
simData <- simData[simData_shuffle,]
rownames(simData) <- 1:nrow(simData)
# simData

testDF_shuffle <- sample(nrow(testDF))
testDF <- testDF[testDF_shuffle,]
rownames(testDF) <- 1:nrow(testDF)
# testDF


####### 1-folding Cross Validation 
n <- 20

# Initialize:
kList<-c()
minusList<-c()
plusList<-c()
totalList<-c()

lowKey=1; highKey=500; stepKey=10


for (k in seq(lowKey,highKey,by=stepKey)){
  kList<-c(kList,k)
  knnMinusErrorRate<-0
  knnPlusErrorRate<-0
  knnErrorRate<-0

  for (i in 1:n){
    simData_shuffle <- sample(nrow(simData))
    testDF_shuffle <- sample(nrow(testDF))
    
    knnModel <- kknn(Y ~., k = k, train = simData, test = testDF, kernel = "rectangular")
    knnPred <- predict(knnModel, data = testDF)
    knnConfusion <- table(testDF$Y, knnPred)

    knnMinusErrorRate <- knnMinusErrorRate+
      knnConfusion[1,2]/sum(knnConfusion[1,])
    knnPlusErrorRate<-knnPlusErrorRate+
      knnConfusion[2,1]/sum(knnConfusion[2,])
    knnErrorRate<-knnErrorRate+
      (knnConfusion[1,2] + knnConfusion[2,1])/sum(knnConfusion)
  }

  knnMinusErrorRate <- knnMinusErrorRate/n
  knnPlusErrorRate <- knnPlusErrorRate/n
  knnErrorRate <- knnErrorRate/n

  minusList <- c(minusList, knnMinusErrorRate)
  plusList <- c(plusList, knnPlusErrorRate)
  totalList <- c(totalList, knnErrorRate)
}

# 
bestError=min(totalList)
bestK=kList[which.min(totalList)]


# Plot k versus both positive and negative error rates and the total error rate
kList <- kList
plot(kList,totalList, 'l',ylim=c(0,1),
     main=paste("Error rate as a function of k\noptimal k=",bestK))
lines(kList,minusList,col="red")
lines(kList,plusList,col="blue")
print(paste("Optimal k is:" , bestK," results in ",
            min(totalList), " error rate"))
      
dev.new()
plot(kList,totalList, main="Error rate as a function of k")
# Since the scatter plot is up and down, we smooth it by polynomial
# regression:
lines(kList,predict(lm(totalList~poly(kList,4),
                       data=data.frame(kList=kList,totalList=totalList)),
                    data.frame(kList=kList)))

cat('Error rate as a function of k, optimal k = ', bestK)

# Simulate in the testDF
knnModel <- kknn(Y ~., k = k, train = simData,  test = testDF, 
                 distance = bestK, kernel = "rectangular")
knnPred <- predict(knnModel, data = testDF)
knnConfusion <- table(testDF$Y, knnPred)
knnConfusion

cat('the accuarcy of the KNN is: ')
sum(diag(knnConfusion))/sum(knnConfusion)

########################################################################################

# 3h). Scatter plot about testDF
# Scatter Plot
plot02 <- ggplot(data = testDF, mapping = aes(x = X1, y = X2, color = Y)) +
  geom_point() +
  scale_color_manual(breaks = c('0','1'), values = c('blue','red'))
plot02


newA2 <- seq(floor(min(testDF$X1)), ceiling(max(testDF$X1)), by = 1)
newA3 <- seq(floor(min(testDF$X2)), ceiling(max(testDF$X2)), by = 1)
newPts0 <- data.frame(X1=kronecker(newA2, rep(1, length(newA3))),
                      X2=rep(newA3, length(newA2)))
knnModel <- kknn(Y ~., k = k, train = simData,  test = testDF,
                 distance = bestK, kernel = "rectangular")
knnPred <- predict(knnModel, data = newPts0)

newPts <- cbind(newPts0, knnPred)
z <- matrix(knnModel$prob, nrow = length(newA2),
            ncol = length(newA3), byrow=T)
dev.new()
contour(newA2, newA3, z, levels = c(0.5), col = 'maroon',
        drawlabels = FALSE, lwd = 2)
points(newPts[testDF$Y=='red',"X1"],newPts[testDF$Y=='red',"X2"],
       pch='.',cex=2,col="red")

points(newPts[testDF$Y=='blue',"X1"],newPts[testDF$Y=='blue',"X2"],
       pch='.',cex=2,col="blue")






