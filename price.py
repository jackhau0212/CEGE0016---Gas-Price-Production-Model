import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from joblib import dump

historic_gas_data = pd.read_csv("data/gas-prices-day-ahead-con.csv")

historic_gas_data['Month'] = historic_gas_data.index

pre_rise_data = historic_gas_data[:147]

y = pre_rise_data['Price'].values
x = pre_rise_data['Month'].values
t = pre_rise_data['Time']

x = x.reshape(len(x), 1)
y = y.reshape(len(y), 1)

price_model = LinearRegression().fit(x,y)

plt.plot(t, y, color = 'red', label='Actual Gas Price')
plt.plot(t, price_model.predict(x), color = 'blue', label="Linear Regression Model")
plt.title("Linear Regression Model for Pre Russion-Ukraine War")
plt.legend()
plt.xlabel('Month')
plt.xticks(range(1, 147, 25))
plt.ylabel('Gas Price')
plt.show()

dump(price_model, "price_model.joblib")