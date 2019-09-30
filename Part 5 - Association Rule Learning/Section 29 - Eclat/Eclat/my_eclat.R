# Eclat

# Data Preprocessing
# install.packages('arules')
library(arules)
dataset = read.csv('Market_Basket_Optimisation.csv')
dataset = read.transactions('Market_Basket_Optimisation.csv', sep = ',', rm.duplicates = TRUE)
dataset = dataset[,10:119]
summary(dataset)
itemFrequencyPlot(dataset, topN = 20)

# Training Eclat on the dataset
rules = eclat(data = dataset, parameter = list(support = 0.009, minlen = 2))

# Visualising the results
inspect(sort(rules, by = 'support')[1:3])