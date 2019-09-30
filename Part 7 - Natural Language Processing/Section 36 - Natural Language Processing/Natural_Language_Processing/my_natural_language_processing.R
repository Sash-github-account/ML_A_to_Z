#dataset
dataset_orig = read.delim('Restaurant_Reviews.tsv', quote = '', stringsAsFactors = FALSE)

#clean data
#install.packages('tm')
library(SnowballC)
library(tm)
corpus = VCorpus(VectorSource(dataset_orig$Review))
corpus = tm_map(corpus, content_transformer(tolower))
corpus = tm_map(corpus, removeNumbers)
corpus = tm_map(corpus, removePunctuation)
corpus = tm_map(corpus, removeWords, stopwords())
corpus = tm_map(corpus, stemDocument)
corpus = tm_map(corpus, stripWhitespace)

#bag of words
dtm = DocumentTermMatrix(corpus)
dtm = removeSparseTerms(dtm, sparse = 0.999)
dataset = as.data.frame(as.matrix(dtm))
dataset$Liked = dataset_orig$Liked

dataset$Liked = factor(dataset$Liked, levels =  c(0,1))

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Liked, SplitRatio = 0.75)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)


# Fitting classifier to the Training set
# Create your classifier here
library(randomForest)
classifier = randomForest(x = training_set[-692], 
                          y = training_set$Liked,
                          n_trees = 20)
# Predicting the Test set results
y_pred = predict(classifier, newdata = test_set[-692])

# Making the Confusion Matrix
cm = table(test_set[, 692], y_pred)