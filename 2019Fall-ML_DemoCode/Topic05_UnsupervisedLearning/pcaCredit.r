# In this file we use the German credit data and use it to apply PCA on
# numerical features, A2, A3, A8 and A16

############################################################################
# Reading in the data:
############################################################################

# This data has some parts missing (indicated by '?'). To tell the data
# frame that this we add na.string="?". Also note that the data is read
# off a web site directly, and not from a local file. Also, since there
# are no headers, we add headers A1 to A16 using sapply, and pase
# functions
dataWebSite<-"http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data"
credit <-  # Note minor simplification compared to before and use of paste0
  read.csv(dataWebSite,na.strings="?",col.names=paste0('A',1:16)) 

#Remove rows with <NA> in A2 A3 and A15 columns. 
credit <- credit[!is.na(credit$A2) & !is.na(credit$A2)&!is.na(credit$A16),]
print(head(credit))
print(tail(credit))
readline("The top and bottom part of the data")
pairs(credit[,c("A2","A3","A8","A15")])
readline("Pairs function plotting pairs of features against each other")
prcredit<-prcomp(credit[,c("A2","A3","A8","A15")], retx=TRUE)
print(summary(prcredit))
readline("Summary of the pcs w/o scaling")
print(prcredit$rotation)
readline("The rotation matrix of the PCA w/o scaling")
screeplot(prcredit)
readline("The scree plot in order")

prcredit2<-prcomp(credit[,c("A2","A3","A8","A15")], retx=TRUE,scale=TRUE)

print(summary(prcredit2))
print(prcredit2$rotation)
readline("The rotation matrix of the scaled data")

screeplot(prcredit2)
readline("The scree plot in order for the scaled data")

