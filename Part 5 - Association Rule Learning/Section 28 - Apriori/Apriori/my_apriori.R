#apriori

library(arules)
dataset = read.csv('Market_Basket_Optimisation.csv', header = FALSE)
dataset = read.transactions('Market_Basket_Optimisation.csv', 
                            sep = ',', 
                            rm.duplicates =TRUE)
itemFrequencyPlot(dataset, topN = 100)

#train model
rules = apriori(data = dataset, 
                parameter = list(support = 0.004, confidence = 0.2))

#Visualise
inspect(sort(rules, by = 'lift' )[1:10])