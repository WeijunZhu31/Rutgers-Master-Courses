library(RWeka)
library(party)
library(partykit)
library(sampling)
library(rpart)
library(rpart.plot)
library(pROC)
library(e1071)
library(corrplot)
library(class)
library(fpc)
library(kknn)
library(adabag)
library(gmodels)
library(boot)
library(stats)
library(ggplot2)
library(factoextra)
library(dplyr)
library(plotly)
library(dplyr)
library(httr)
library(MASS)


                      ############ Part I: Data Preprocessing ############

                          #### Import Database & Observation ####
setwd("C:/Users/zhuwe/")
setwd("C:/Users/zhuwe/Desktop/DM_Project") 
Admission <- read.table("C:/Users/zhuwe/Desktop/DM_Project/Admission_Predict.csv", 
                        header=TRUE, sep=",")
### Summary of database:
head(Admission)
fix(Admission)
str(Admission)
names(Admission)
attach(Admission)
### 查看异常值！！！！也可以检查数据是否是normalization和centralization！！！！
boxplot(GRE.Score, xlab="GRE_Score")
boxplot(TOEFL.Score, xlab="TOEFL_Score")
boxplot(CGPA, xlab="CGPA")
### 根据箱线图可知，数据的分布情况很好，不需要“中心化”和“标准化”！！！



                  ############# Part II: Data Visualization #############

### Delete the Attribute：删除不需要的attribute
?select
Admission <- dplyr::select(Admission, -Serial.No.)
### Handle the NA value：去掉空值
Admission <- na.omit(Admission)

              ### Correlation of Each Attributes ####
### Scatter Plot 散点图
pairs(Admission, main="")
### Correlationship plot
x <- data.matrix(Admission)
data_cor <- cor(x)
corrplot(corr=data_cor, method = 'color', addCoef.col="grey")



              #### Parallel Coordinates Plot ####

#### 
my_colors=colors()[as.numeric(Admission$Chance.of.Admit)*30]
parcoord(Admission[,c(1:7)] , col= my_colors, 
         main="The Chance of Admission Across Variables" )


                  #### 3D Graph####

### 抽取GRE和CGPA
kd <- with(Admission,kde2d(GRE.Score,CGPA,n=50))
p2 <- plot_ly(x=kd$x,y=kd$y,z=kd$z)%>%add_surface()
p2
### 近似于正态分布
### 抽取GRE和TOEFL成绩
kd1 <- with(Admission,kde2d(GRE.Score,TOEFL.Score,n=50))
p21 <- plot_ly(x=kd1$x,y=kd1$y,z=kd1$z)%>%add_surface()
p21
### 近似于正态分布


### 那么SOP和LOR对录取率有什么变化呢？？？






                #### Data Analystics & Linear Regression ####

attach(Admission)
str(Admission)
lm.fit01 <- lm(Chance.of.Admit~., data=Admission)
summary(lm.fit01)
### 逐步回归分析 -- ACI 来减少变量
tstep<-step(lm.fit01)
summary(tstep)
### 逐步回归分析的优化
drop1(tstep)
### 进一步进行多元回归分析
lm.fit01<-lm(Chance.of.Admit~GRE.Score+TOEFL.Score+University.Rating+LOR+CGPA+Research,
             data=Admission)
summary(lm.fit01)
### Regression Function: Chance.of.Admit的线性方程
# Chance.of.Admit=-1.2682451+0.0018145*GRE+0.0028115*TOEFL+0.0058151*University_Rating+0.0188039*LOR+0.1185885*CGPA+0.0242723*Research



                             #### 1: K-Means Algorithm ####
### 
### 聚类
fviz_nbclust(Admission, kmeans, method ="wss")+geom_vline(xintercept=4,linetype=2)
km_Admission <- kmeans(Admission, 4, iter.max=50, nstart=25)
print(km_Admission)
### 聚类中心
aggregate(Admission, by=list(cluster=km_Admission$cluster),mean)
fviz_cluster(km_Admission, data=Admission, frame.type="t", frame.alpha=0.3, frame.level=1.0)
### 这里面有很多outliers


                  #### Training_Set & Testing_Set  ####

### Traning Set: Choose randomly 70% of data set to be the traning data
Admission$Chance.of.Admit
Admission$Chance.of.Admit <- as.numeric(Admission$Chance.of.Admit)
### 找分类的threhold:
### Chance.of.Admit=-1.2682451+0.0018145*GRE+0.0028115*TOEFL+0.0058151*University_Rating+0.0188039*LOR+0.1185885*CGPA+0.0242723*Research
mean(GRE.Score)
mean(TOEFL.Score)
mean(University.Rating)
mean(LOR)
mean(CGPA)
mean(Research)
### 由线性回归方程可得Chance.of.Admit=0.7229057，以他来做threshold

### P(x>=3)
1-pbinom(3, 6,prob = 0.72) # Prob=0.52822 When we choose 6 colleges
1-pbinom(2, 6,prob = 0.72)
1-pbinom(1, 6,prob = 0.72)
### 分training set 和 test set,training set占百分之70
Admission$Chance.of.Admit[Admission$Chance.of.Admit > 0.72] <- "Big Chance"
Admission$Chance.of.Admit[Admission$Chance.of.Admit <= 0.72] <- "Small Chance"

Admission$Chance.of.Admit <- factor(Admission$Chance.of.Admit)

train_sub <- sample(nrow(Admission), 0.7*nrow(Admission))
train_set <- Admission[train_sub,]  # Traning Set
test_set <- Admission[-train_sub,]  # Test Set

set.seed(1234)




                    ########### Part III: Data Mining ##############

                              #### 2: CART Algorithm #### 
### Cart算法：Gini
### Decision Tree
tree_train_set <- rpart(train_set$Chance.of.Admit~.,
                        data = train_set, method = "class", 
                        parms=list(split="gini"))
tree_train_set

### Pruning the Tree
tree_train_set$cptable # Before the Pruning 
### 剪枝pruning
tree_prune<- prune(tree_train_set,cp=0.01774194)  ## Set the threhold=
tree_prune$cptable # After the Pruning

### Draw the Decision Tree by using rpart.plot()
opar<-par(no.readonly = T)
par(mfrow=c(1,2))
rpart.plot(tree_train_set,branch=1,type=2, fallen.leaves=T,cex=0.8, 
           sub="Before Pruning")
rpart.plot(tree_prune,branch=1, type=3,fallen.leaves=T,cex=0.8, 
           sub="After Pruning")

### Predict Model & Bulit Confusion Matrix
### Training Set
predtree<-predict(tree_train_set,newdata=train_set,type="class")
confusion_train_set <- table(train_set$Chance.of.Admit,predtree,
                             dnn=c("True_Value","Predict_Value")) 
accuracy_train_set=sum(diag(confusion_train_set))/sum(confusion_train_set)
accuracy_train_set # Precision of Training Set=0.83
### Test Set
?table
predtree<-predict(tree_prune,newdata=test_set,type="class")
confusion_test_set <- table(test_set$Chance.of.Admit,predtree,
                            dnn=c("True_Value","Predict_Value")) 
confusion_test_set 
accuracy_test_set=sum(diag(confusion_test_set))/sum(confusion_test_set)
accuracy_test_set 

### ROC Curve
decisiontree_cart <- roc(test_set$Chance.of.Admit,
                           as.numeric(predtree))

plot(decisiontree_cart, print.auc=TRUE, auc.polygon=TRUE, 
     grid=c(0.1, 0.2), grid.col=c("green", "red"), max.auc.polygon=TRUE,
     auc.polygon.col="skyblue", print.thres=TRUE,
     main='The ROC Curve of Cart',
     xlab="FPR", ylab="TPR")
### AUC 的取值范围在[0,1]，越接近1，model越好


                    #### 3: C4.5 Algorithm ####

Admission$Chance.of.Admit <- factor(Admission$Chance.of.Admit)

ctrain_set <- J48(train_set$Chance.of.Admit~.,
                  data=train_set)
print(ctrain_set)
plot(ctrain_set)
### Training Set
cpretree1 <- predict(ctrain_set,newdata = train_set, type="class")
conf_matrix1 <- table(train_set$Chance.of.Admit,cpretree1,
                      dnn=c("True_Value","Predict_Value")) #Precision of Train Set=0.88
conf_matrix1
accuracy_train_matrix=sum(diag(conf_matrix1))/sum(conf_matrix1)
accuracy_train_matrix
### Test Set
cpretree2 <- predict(ctrain_set,newdata = test_set, type="class")
conf_matrix2 <- table(test_set$Chance.of.Admit,cpretree2,
                      dnn=c("True_Value","Predict_Value")) #Precision of Test Set=0.81
conf_matrix2
accuracy_test_matrix=sum(diag(conf_matrix2))/sum(conf_matrix2)
accuracy_test_matrix

### ROC Curve
decisiontree_c45 <- roc(test_set$Chance.of.Admit,
                         as.numeric(cpretree2))

plot(decisiontree_c45, print.auc=TRUE, auc.polygon=TRUE, 
     grid=c(0.1, 0.2), grid.col=c("green", "red"), max.auc.polygon=TRUE,
     auc.polygon.col="skyblue", print.thres=TRUE,
     main='The ROC Curve of C4.5',
     xlab="FPR", ylab="TPR")


                    #### 4: Support Vector Machine (SVM) Algorithm ####

### SVM of Training Set
svm.model<-svm(train_set$Chance.of.Admit~., train_set)
summary(svm.model)
### Confusion Matrix of Training Set
confusion.train.svm=table(train_set$Chance.of.Admit,predict(svm.model,train_set,type="class"))
accuracy.train.svm=sum(diag(confusion.train.svm))/sum(confusion.train.svm)
confusion.train.svm
accuracy.train.svm
### Test Set: SVM & Confusion Matrix
pred_svm <- predict(svm.model,test_set,type="class")
pred_svm
confusion.test.svm=table(test_set$Chance.of.Admit,predict(svm.model,test_set,type="class"))
accuracy.test.svm=sum(diag(confusion.test.svm))/sum(confusion.test.svm)
confusion.test.svm
accuracy.test.svm
### ROC CUrve
decisiontree_roc <- roc(test_set$Chance.of.Admit,
                           as.numeric(pred_svm))

plot(decisiontree_roc, print.auc=TRUE, auc.polygon=TRUE, 
     grid=c(0.1, 0.2), grid.col=c("green", "red"), max.auc.polygon=TRUE,
     auc.polygon.col="skyblue", print.thres=TRUE,
     main='The ROC Curve of SVM',
     xlab="FPR", ylab="TPR")


                      #### 5: K-NN Algorithm ####
### K-NN
?knn
knn_Admission <- kknn(train_set$Chance.of.Admit~., train_set, test_set,
                      distance = 1, kernel = "triangular")
fit <- fitted(knn_Admission)
fit
confusion.test.knn <- table(test_set$Chance.of.Admit,fit)
confusion.test.knn
accuracy.confusion.test.knn=sum(diag(confusion.test.knn))/sum(confusion.test.knn)
accuracy.confusion.test.knn

### ROC Curve 画不出来！！！！
decisiontree_rrtain <- roc(test_set$Chance.of.Admit,
                           as.numeric(rrpred))

plot(decisiontree_rrtain, print.auc=TRUE, auc.polygon=TRUE, 
     grid=c(0.1, 0.2), grid.col=c("green", "red"), max.auc.polygon=TRUE,
     auc.polygon.col="skyblue", print.thres=TRUE,
     main='The ROC Curve of KNN',
     xlab="FPR", ylab="TPR")


                      #### 6: Adaboost Alorithm ####
### Ensemable
### 默认迭代次数为100，运行速度慢
?boosting
ada.test.set <- boosting(Chance.of.Admit~.,
                         data = train_set, mfinal=100)  # 100 iteration - 迭代次数越多，准确率越高
### Importance of every attributes
barplot(ada.test.set$importance,main="Importantce of Each Attribute") 
### Compute Error
error <- errorevol(ada.test.set,train_set)
### 对误差演变进行画图
plot(error$error,type="l",
     main="AdaBoost error VS number of trees")

### Confusion Matrix
pre_decisiontree_ada <- predict(ada.test.set,newdata = test_set)$class
pre_decisiontree_ada
### 查看pre_decsisontree_ada是什么类型
class(pre_decisiontree_ada)
pre_decisiontree_ada <- factor(pre_decisiontree_ada)
obs_p_decision_ada= data.frame(prob=pre_decisiontree_ada,
                               obs=test_set$Chance.of.Admit)
ada_table <- table(test_set$Chance.of.Admit,
                   pre_decisiontree_ada,
                   dnn=c("True_Value","Predict_Value"))
adatable_test <- table(test_set$Chance.of.Admit, pre_decisiontree_ada)
adatable_test
accuracy.adatable_table=sum(diag(adatable_test))/sum(adatable_test)
accuracy.adatable_table

### ROC Curve
roc_ada <- roc(test_set$Chance.of.Admit, 
               as.numeric(pre_decisiontree_ada)) 

plot(roc_ada, print.auc=TRUE, auc.polygon=TRUE, 
     grid=c(0.1, 0.2), grid.col=c("green", "red"), max.auc.polygon=TRUE, 
     auc.polygon.col="skyblue", print.thres=TRUE, 
     main='The ROC Curve of Adaboost',
     xlab="FPR", ylab="TPR")
### 在训练集测试中 AUC=1.0 --- 是一种完美的情况
### AUC 的取值范围在[0,1]，越接近1，model越好；AUC = accuracy


                      #### 7: RIPPER Algorithm ####
### 
rrtrain <- JRip(Chance.of.Admit~., data=train_set)
rrtrain   # We can see the rules after using RIPPER
rrpred <- predict(rrtrain, test_set)
rrpred

### Table & Accuracy
rrtable_test <- table(test_set$Chance.of.Admit,rrpred)
rrtable_test
accuracy.rrtable_table=sum(diag(rrtable_test))/sum(rrtable_test)
accuracy.rrtable_table

### ROC Curve
decisiontree_rrtain <- roc(test_set$Chance.of.Admit,
                           as.numeric(rrpred))

plot(decisiontree_rrtain, print.auc=TRUE, auc.polygon=TRUE, 
     grid=c(0.1, 0.2), grid.col=c("green", "red"), max.auc.polygon=TRUE,
     auc.polygon.col="skyblue", print.thres=TRUE,
     main='The ROC Curve of RIPPER',
     xlab="FPR", ylab="TPR")



