#============================================================================
# Regression Trees
# Data Analytics and Visualization--Fall 2019
# Instructor: Debopriya Ghosh
# Author: debopriya.ghosh@rutgers.edu
# Last Modified On:
#============================================================================


# Reading the dataset
# The dataset includes information on the variables using all the block groups in California
# from the 1990 Cens us. In this sample a block group on average includes 1425.5 individuals 
# living in a geographically compact area. Naturally, the geographical area included varies 
# inversely with the population density. The distances among the centroids of each block
# group are measured in latitude and longitude. All the block groups reporting zero 
# entries for the independent and dependent variables were excluded. The final data contained 
# 20,640 observations on 9 variables. The dependent variable is ln(median house value).


# ATTRIBUTE INFORMATION
# median house value, median income, housing median age, total rooms,
# total bedrooms, population, households, latitude, and longitude.

ca.housingdata = read.table("~/Documents/Data Analysis and Visualization -Spring 2018/Datasets/cal_housing.data", sep=",")
dim(ca.housingdata)
 
colnames(ca.housingdata) = c("longitude","latitude","housing_median_age","total_rooms","total_bedrooms","population","households","median_income","median_house_value")

ca.housingdata$bedrooms_per_household = round(ca.housingdata$total_bedrooms/ca.housingdata$households)
ca.housingdata$rooms_per_household = round(ca.housingdata$total_rooms/ca.housingdata$households)
ca.housingdata$population_per_household = round(ca.housingdata$population/ca.housingdata$households)

table(ca.housingdata$bedrooms_per_household)
table(ca.housingdata$rooms_per_household)
table(ca.housingdata$population_per_household)

summary(ca.housingdata)


# building the tree
library(tree)

tree.model <- tree((median_house_value/1000) ~ longitude + latitude, data=ca.housingdata)
plot(tree.model)
text(tree.model, cex=.75)

summary(tree.model)
tree.model

# x_norm = (x - min(x)) / (max(x) - min(x))
# col_fun <- colorRamp(c("blue", "red"))
# rgb_cols <- col_fun(x_norm)
# clrs <- rgb(rgb_cols, maxColorValue = 256)

price.deciles = quantile(ca.housingdata$median_house_value, 0:10/10)
cut.prices    = cut(ca.housingdata$median_house_value, price.deciles, include.lowest=TRUE)
rooms.quartiles = quantile(ca.housingdata$rooms_per_household, type = 4)
cut.rooms = cut(ca.housingdata$rooms_per_household,rooms.quartiles,include.lowest = TRUE)

plot(ca.housingdata$longitude, ca.housingdata$latitude, col=grey(10:2/11)[cut.prices], pch=20, xlab="Longitude",ylab="Latitude") 
#  plot(ca.housingdata$longitude, ca.housingdata$latitude, col=cols[cut.rooms], pch=20, xlab="Longitude",ylab="Latitude")
partition.tree(tree.model, ordvars=c("longitude","latitude"), add=TRUE)


# Including all the variables
tree.model2 <- tree((median_house_value/1000) ~ ., data=ca.housingdata)
plot(tree.model2)
text(tree.model2, cex=.75)

summary(tree.model2)
