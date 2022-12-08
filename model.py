from well import Well
from price import Price

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


number_of_operational_months = 12*30
transition_from_hyperbolic_to_exponential = 200


data_list = []

# building 6 wells in every year at the same time
for i in range(12, 12*6, 12):
    for j in range(0, 6):
        well = Well(end_month=number_of_operational_months, transition_month=transition_from_hyperbolic_to_exponential)
        well_production = well.monthly_volume_production(well_start_month=i)
        data_list.append(well_production)


data = pd.DataFrame(data=data_list)
# print(data)

total_monthly_production = []
for i in range(0, number_of_operational_months+1):
    total_monthly_production.append(data[i].sum())
    
#data.to_csv("data/monthly_production.csv")


print(f"total production: {sum(total_monthly_production)}")

plt.figure(1)
plt.plot(total_monthly_production)
plt.title("Total Monthly Production")
plt.xlabel("Month")
plt.ylabel("Volume (m^3)")
plt.show()

price = Price()
price_forecast = price.get_prediction()

#pd.DataFrame(data=price_forecast).to_csv("data/monthly_price.csv")

##### Monthly Cash Generation

monthly_cash_generation = price_forecast * total_monthly_production
print(f"The total cash generated: {sum(monthly_cash_generation)}")
plt.figure(2)
plt.plot(monthly_cash_generation)
plt.title("Total Monthly Revenue Generation")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.show()

pd.DataFrame(data=monthly_cash_generation).to_csv("data/monthly_cash_generation.csv")