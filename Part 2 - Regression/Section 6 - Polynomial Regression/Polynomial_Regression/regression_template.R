# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[,2:3]

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)
# set.seed(123)
# split = sample.split(dataset$Salary, SplitRatio = 0.8)
# training_set = subset(dataset, split == TRUE)
# test_set = subset(dataset, split == FALSE)

#fit model
#regressor = lm(formula = ,
#              data = dataset)

#visualise
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)

ggplot() + 
  geom_point(aes(x=dataset$, y=dataset$),
             colour = 'red') +
  geom_line(aes(x=x_grid, y=predict(regressor, newdata = data.frame(Level = x_grid))),
            colour = 'dark green') +
  ggtitle('regression model') +
  xlab('tit1') +
  ylab('tit2')


#predict poly
y_pred = predict(regressor, data.frame(Level = 6.5 ))

