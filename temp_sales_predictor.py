# library imports
import pandas as pd 
from matplotlib import pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np 

# data set reading
mydata = pd.read_csv("temp_sales.csv")
x = mydata[["X"]]
y = mydata[["Y"]]

# model creation and training
model = LinearRegression()
model.fit(x,y)

cf = model.coef_
print("Coefficient = ", cf)
intercept = model.intercept_
print("Intercept = ", intercept)

# predicting new value
new_sales = model.predict([[160]])
print("Predicted sales = ", new_sales)

# model evaluation
y_pred = model.predict(x)
mse = mean_squared_error(y,y_pred)
print("MSE = ", mse)
rmse = np.sqrt(mse)
print("RMSE = ", rmse)

# visualization
plt.scatter(x,y)
plt.plot(x,y_pred, color = 'red')
plt.show()