import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import math
from joblib import dump

class Price:
    def __init__(self):
        pass
    
    def get_prediction(self):
        # reading the csv data file
        historic_gas_data = pd.read_csv("data/gas-prices-day-ahead-converted_unit.csv")

        historic_gas_data['Month'] = historic_gas_data.index

        # the pre rise data is the data before the russia-ukraine war
        pre_rise_data = historic_gas_data[:147]

        y = pre_rise_data['Price'].values
        x = pre_rise_data['Month'].values

        x = x.reshape(len(x), 1)
        y = y.reshape(len(y), 1)

        price_model = LinearRegression().fit(x,y)

        # we are forecasting from 0th month to 360th month (30 years)
        t = np.array([x for x in range(0, 12*30+1)])
        t = t.reshape(len(t), 1)

        '''
        the deterministic forecast will be the linear regression model + the last
        available value from the data
        similar to y = mx + c
        '''
        price_forecast_deterministic = price_model.predict(t) + historic_gas_data['Price'].iat[-1] - price_model.predict(t)[0] - 3.5

        # Sstochastic differential equation
        price_forecast = np.zeros(12*30+1) + price_forecast_deterministic[0]
        sigma = pre_rise_data[:147]['Price'].std() # Standard deviation.


        for i in range(1, 12*30):
            price_forecast[i + 1] = price_forecast_deterministic[i] * 1 + (0.5*sigma * 1 * np.random.normal(0,1))
        
        plt.figure(1)
        plt.plot(t, price_forecast)
        plt.title('Gas Price Forecast from November 2022')
        plt.xlabel('Number of Months into the Future')
        plt.ylabel('Gas Price (£/m^3)')


        plt.figure(2)
        plt.plot(pre_rise_data['Time'].values, y, color = 'red', label='Actual Gas Price')
        plt.plot(pre_rise_data['Time'].values, price_model.predict(x), color = 'blue', label="Linear Regression Model")
        plt.title("Gas Price Pre Russion-Ukraine War")
        plt.legend()
        plt.xlabel('Month')
        plt.xticks(range(1, 147, 25))
        plt.ylabel('Gas Price (£/m^3)')


        plt.figure(3)
        total_gas_price = np.append(historic_gas_data['Price'].values.reshape(
            len(historic_gas_data['Price']), 1), price_forecast)

        plt.plot(np.array([x for x in range(0, 12*30+157+1)]),
                total_gas_price, color='black')
        plt.title('Gas Price from 2009 to 30 Years from Now')
        plt.ylabel("Gas Price (£/m^3)")
        plt.xlabel("Month")
        plt.show()    
    
        return price_forecast

