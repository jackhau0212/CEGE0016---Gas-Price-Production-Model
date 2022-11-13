from well import Well
import matplotlib.pyplot as plt
import pandas as pd


number_of_operational_months = 12*30
transition_from_hyperbolic_to_exponential = 200


data_list = []

# building 6 wells in every year at the same time
for i in range(0, 12*6, 12):
    for j in range(0, 6):
        well = Well(end_month=number_of_operational_months, transition_month=transition_from_hyperbolic_to_exponential)
        well_production = well.monthly_volume_production(well_start_month=i)
        data_list.append(well_production)


data = pd.DataFrame(data=data_list)
print(data)

total_monthly_production = []
for i in range(0, number_of_operational_months+1):
    total_monthly_production.append(data[i].sum())
    
plt.plot(total_monthly_production)
plt.title("Total Monthly Production")
plt.xlabel("Month")
plt.ylabel("Volume (m^3)")
plt.show()