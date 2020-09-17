

#===============================================================================================================================
# Multinomial Regression
# Data Analytics and Visualization--Fall 2019
# Instructor: Debopriya Ghosh
# Author: debopriya.ghosh@rutgers.edu
# Last Modified On:
#===============================================================================================================================
Diabetes =read.csv("~/Documents/Data Analysis and Visualization -Spring 2018/Datasets/diabetic_data.csv",na.strings = '?')
dim(Diabetes)
summary(Diabetes)
colnames(Diabetes)

cols = colnames(Diabetes)[colSums(is.na(Diabetes))>0]

Diabetes = Diabetes[,!(colnames(Diabetes)%in% cols)]
dim(Diabetes)

#checks for complete cases to verify no missing values present
Diabetes.complete = Diabetes[complete.cases(Diabetes),]
dim(Diabetes.complete)



#building multinomial model
install.packages("foreign")
install.packages("nnet")
install.packages("ggplot2")
install.packages("reshape2")


require(foreign)
require(nnet)
require(ggplot2)
require(reshape2)

colnames(Diabetes)
temp = Diabetes.complete[,-c(1,2,33,34)]
temp$readmitted1 = relevel(temp$readmitted, ref = "NO")
multinom.fit = multinom(readmitted1 ~ A1Cresult + insulin ,data =temp,family = "multinomial")
summary(multinom.fit)
table(Diabetes$readmitted)


# computing coeff, std error, z valu, and p-values and tabulating the results
z=  summary(multinom.fit)$coefficients/summary(multinom.fit)$standard.errors
p = (1-pnorm(abs(z),0,1))*2
coeff = summary(multinom.fit)$coefficients
std.err = summary(multinom.fit)$standard.errors
t = cbind(t(coeff),t(std.err),t(z),t(p))
t= unique(t)
write.csv(t,"C:\\Users\\Debopriya\\Dropbox\\Spring 2017- ML for Data Science\\Datasets\\dataset_diabetes\\dataset_diabetes\\results_multinom.csv")

test = Diabetes.complete[100:350,-c(1,2,33,34)]
pred = predict(multinom.fit,test[,-39], type = "class")
table(pred, test$readmitted)
