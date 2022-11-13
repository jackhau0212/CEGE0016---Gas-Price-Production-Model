from well import Well
import matplotlib.pyplot as plt
import pandas as pd


number_of_operational_months = 100
transition_from_hyperbolic_to_exponential = 60

data_colomns = [x for x in range(0,100+1)]
data_colomns.insert(0,"Well")
data_list = []

# building 1 well a month
for i in range(0, 30):
    well = Well(end_month=number_of_operational_months, transition_month=transition_from_hyperbolic_to_exponential)
    well_production = well.monthly_volume_production(well_start_month=i)
    data_list.append(well_production)


data = pd.DataFrame(data=data_list)
print(data)

total_monthly_production = []
for i in range(0, 100+1):
    total_monthly_production.append(data[i].sum())
    
plt.plot(total_monthly_production)
plt.title("Total Monthly Production")
plt.xlabel("Month")
plt.ylabel("Volume (m^3)")
plt.show()