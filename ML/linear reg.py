import pandas as pd
import numpy as np

print("Already installed sklearn, pandas and numpy in the tensor env")
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
print("Everything imported for linear regression")

data = pd.read_csv("student-mat.csv", sep=";")
#print(data.head())

data = data[["G1","G2","G3","famrel"]]
#print(data.head())
#print(data.tail())

predict = "G3"

x = np.array(data.drop([predict],1))   #Drop G3 column and make the rest into list
y = np.array(data[predict])  #Column G3 elements stored as list
#print(x)
#print(y)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)
print(len(x_train)) #355
print(len(x_test)) #40
print(len(y_train)) #355
print(len(y_test))  #40 ~10 % of training set

linear = linear_model.LinearRegression()   #This is our model
#We are trying to predict final grades G3 based on parameters other than G3 such as G1, G2, famrel
linear.fit(x_train,y_train)
acc = linear.score(x_test,y_test)  #Try the model on test
print(acc)   #Accuracy -  which will vary each time you run it

print(linear.coef_)   #[0.1506377  0.99810313 0.25072664]  -> Coefficients like slopes for each axis - here were 3
print(linear.intercept_)  #intercept on G3 axis

#Try the fit on x_test on which we have NOT trained the fit
predictions  = linear.predict(x_test)
print("Parameters observed    Predicted value from fit     Actual value")

for i in range(len(predictions)):
    print(x_test[i],"\t\t",predictions[i],"\t\t",y_test[i])

"""
Parameters observed    Predicted value from fit     Actual value
[11 13  4]               12.65928221045806               13
[8 8 4]                  7.2461897552490235              10

"""
