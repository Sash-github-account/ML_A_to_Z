# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Salary_Data.csv')
#dataset = dataset[,2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


# Feature Scaling
# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])
regressor = lm(formula = Salary ~ YearsExperience, training_set)

y_pred = predict(regressor, newdata = test_set)

#install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y =training_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience, y = predict(regressor, newdata = training_set)),
            colour = 'blue') + 
  ggtitle('Salary vs exp (training)') +
  xlab('years of exp')+
  ylab('Salary')

ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y =test_set$Salary),
             colour = 'red') + 
  geom_line(aes(x = test_set$YearsExperience, y = predict(regressor, newdata = test_set)),
            colour = 'blue') + 
  ggtitle('Salary vs exp (test)') +
  xlab('years of exp')+
  ylab('Salary')