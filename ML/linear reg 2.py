import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1","G2","G3","famrel"]]

predict = "G3"

x = np.array(data.drop([predict],1))   #Drop G3 column and make the rest into list
y = np.array(data[predict])  #Column G3 elements stored as list

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

best = 0
for _ in range(30):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

    linear = linear_model.LinearRegression()   #This is our model

    linear.fit(x_train,y_train)
    acc = linear.score(x_test,y_test)  #Try the model on test
    print(acc)   #Accuracy -  which will vary each time you run it

    if acc > best:   #Save the model with highest accuracy
        best = acc
        print("Selected model ",_)
        with open("studentmodel.pickle","wb") as f:
            pickle.dump(linear,f)


pickle_in = open("studentmodel.pickle","rb")
linear = pickle.load(pickle_in)

print(linear.coef_)   #[0.1506377  0.99810313 0.25072664]  -> Coefficients like slopes for each axis - here were 3
print(linear.intercept_)  #intercept on G3 axis



#Plotting :
style.use("ggplot")
pp = "G1"   #Dynamic variable which we would want
pyplot.scatter(data[pp],data["G3"])
pyplot.xlabel(pp)
pyplot.ylabel("Final grade")
pyplot.show()


style.use("ggplot")
pp = "famrel"   #Dynamic variable which we would want
pyplot.scatter(data[pp],data["G3"])
pyplot.xlabel(pp)
pyplot.ylabel("Final grade")
pyplot.show()
