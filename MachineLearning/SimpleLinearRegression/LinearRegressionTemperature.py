import sklearn
from sklearn import model_selection
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np
import random

# y = mx+c
# F = 1.8*C+32


x = list(range(0,10))           #C
y = [1.8*F+32 for F in x]       #F
#y = [1.8*F+32 + random.randint(-3,3) for F in x]
# print(f'X:{x}')
# print(f'Y:{y}')

#ploting data on the graph
plt.plot(x,y,'-*b')
plt.show()

#Reshapeing data

x = np.array(x).reshape(-1,1)
y = np.array(y).reshape(-1,1)

xTrain, xTest, yTrain, yTest = model_selection.train_test_split(x, y, test_size=0.2)

# print(xTrain.shape)
model = linear_model.LinearRegression()
model.fit(xTrain,yTrain)
print(f'Cofficient:{model.coef_}')
print(f'Intercept:{model.intercept_}')


accuracy = model.score(xTest,yTest)
print(f'Accuracy:{round(accuracy*100,2)}')











