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
lin_reg = lm(formula = Salary ~ .,
             data = dataset)


dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,
              data = dataset)

#visualise
library(ggplot2)
ggplot() + 
  geom_point(aes(x=dataset$Level, y=dataset$Salary),
             colour = 'red') +
  geom_line(aes(x=dataset$Level, y=predict(lin_reg, newdata = dataset)),
            colour = 'blue') +
  geom_line(aes(x=dataset$Level, y=predict(poly_reg, newdata = dataset)),
            colour = 'dark green') +
  ggtitle('Linear(blue) and Polynomial(green) model') +
  xlab('level') +
  ylab('salary')


#predict lin
y_pred_lin = predict(lin_reg, data.frame(Level = 6.5))

#predict poly
y_pred_poly = predict(poly_reg, data.frame(Level = 6.5, Level2 = 6.5^2, Level3 = 6.5^3, Level4=6.5^4))

