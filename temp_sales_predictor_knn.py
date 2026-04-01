# library imports
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

# data set reading
mydata = pd.read_csv("temp_sales.csv")
x = mydata[["X"]]
y = mydata[["Y"]]

# finding best k value

rmse_values = []

for i in range(2,100):
    model = KNeighborsRegressor(n_neighbors = i)
    model.fit(x,y)
    y_pred = model.predict(x)
    mse = mean_squared_error(y,y_pred)
    rmse = np.sqrt(mse)
    rmse_values.append(rmse)

best_k = range(2,100) [np.argmin(rmse_values)]
print("Best K = ", best_k)

# model creation
model = KNeighborsRegressor(n_neighbors = best_k)
model.fit(x,y)

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