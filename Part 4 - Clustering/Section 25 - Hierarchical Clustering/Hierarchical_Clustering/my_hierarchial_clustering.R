# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Mall_Customers.csv')
X = dataset[4:5]

#dendro
dendro = hclust(dist(X, method = 'euclidean'),
                method = 'ward.D')
plot(dendro,
     main = paste('dendro'),
     xlab = 'cust',
     ylab = 'Eucl. dist')

y_hc = cutree(dendro, 5)

library(cluster)
clusplot(X, 
         y_hc,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste("clusters"))