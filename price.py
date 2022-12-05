import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import math


class Price:
    def __init__(self):
        pass
    
    def get_prediction(self):
        # reading the csv data file
        historic_gas_data = pd.read_csv("data/data.csv")

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
        price_forecast_deterministic = price_model.predict(t) + historic_gas_data['Price'].iat[-1] - price_model.predict(t)[0] - 4

        # Sstochastic differential equation
        price_forecast = np.zeros(12*30+1) + price_forecast_deterministic[0]
        sigma = pre_rise_data[:147]['Price'].std() # Standard deviation.


        for i in range(1, 12*30):
            price_forecast[i + 1] = price_forecast_deterministic[i] * 1 + (0.5 * sigma * 1 * np.random.normal(0,1))
        
        month =["11/2022", "12/2022"]
        
        for i in range(2023,2053):
            for j in range(1,13):
                if j < 10:  
                    month.append("0" + str(j) + "/"  + str(i))
                else:
                    month.append(str(j) + "/"  + str(i))
                
        plt.figure(1)
        plt.plot((month[:-1]), price_forecast)
        plt.title('Gas Price Forecast from November 2022')
        plt.xlabel('Months into the Future')
        plt.xticks(np.arange(0,len(month[:-1]),36))
        plt.ylabel('Gas Price (£/m^3)')


        plt.figure(2)
        plt.plot(pre_rise_data['Time'].values, y, color = 'red', label='Actual Gas Price')
        plt.plot(pre_rise_data['Time'].values, price_model.predict(x), color = 'blue', label="Linear Regression Model")
        plt.title("Gas Price Pre Russion-Ukraine War")
        plt.legend()
        plt.xlabel('Month')
        plt.xticks(np.arange(0,len(pre_rise_data['Time'].values),20))
        plt.ylabel('Gas Price (£/m^3)')


        plt.figure(3)
        total_gas_price = np.append(historic_gas_data['Price'].values.reshape(
            len(historic_gas_data['Price']), 1), price_forecast)

        total_month = np.append( np.array([x[3:] for x in historic_gas_data['Time']]), np.array(month[:-1]))

        plt.plot(total_month, total_gas_price, color='black')
        plt.title('Gas Price from 2009 to 2052 (30 Years from Present)')
        plt.ylabel("Gas Price (£/m^3)")
        plt.xlabel("Month")
        plt.xticks(np.arange(0,len(total_month),12*5))
        plt.show()
        
        
    
        return price_forecast


