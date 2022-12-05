import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

class Well:
    def __init__(self, end_month, transition_month):
        self.end_month = end_month
        self.transition_month = transition_month
        
    def daily_volume_production(self, well_start_month):
        '''
        phase 1: hyperbolic decline function
        phase 2: exponential decline function
        '''
        # hyperbolic decline function constants
        q_1 = 537442/30
        b = 2
        D_i = 0.1

        monthly_production = []
        
        # phase 1
        for month_1 in range(0, self.transition_month+1):
            # the hyperbolic decline function
            monthly_production.append(q_1/(1+b*D_i*month_1)**(1/b))

        # exponential decline function constants
        q_2 = monthly_production[-1]
        D_s = (q_2 - q_1/(1+b*D_i*(self.transition_month+1))**(1/b))/q_2
        
        # phase 2
        for month_2 in range(1, self.end_month-self.transition_month+1):
            # exponential decline function
            monthly_production.append(q_2 * math.exp(-D_s*month_2))
            
        for i in range(0, well_start_month):
            monthly_production.insert(0, 0)
            
        return monthly_production[0:self.end_month+1]

    def monthly_volume_production(self, well_start_month):
        '''
        phase 1: hyperbolic decline function
        phase 2: exponential decline function
        '''
        # hyperbolic decline function constants
        q_1 = 1783961
        b = 2
        D_i = 0.1

        monthly_production = []
        
        # phase 1
        for month_1 in range(0, self.transition_month+1):
            # the hyperbolic decline function
            monthly_production.append(q_1/(1+b*D_i*month_1)**(1/b))

        # exponential decline function constants
        q_2 = monthly_production[-1]
        D_s = (q_2 - q_1/(1+b*D_i*(self.transition_month+1))**(1/b))/q_2
        
        # phase 2
        for month_2 in range(1, self.end_month-self.transition_month+1):
            # exponential decline function
            monthly_production.append(q_2 * math.exp(-D_s*month_2))
            
        for i in range(0, well_start_month):
            monthly_production.insert(0, 0)
            
        return monthly_production[0:self.end_month+1]