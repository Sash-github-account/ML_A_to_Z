# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')

set.seed(6)
wcss <- vector()
for (i in 1:10) {
  wcss [i] <-sum(kmeans(X,i)$withinss)
}
plot(1:10,wcss,type = 'b', main =paste("clusters"))

set.seed(29)
kmeans <- kmeans(X, 5, iter.max = 300, nstart = 10)

#visualize
library(cluster)
clusplot(X, 
         kmeans$cluster,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste("clusters"))