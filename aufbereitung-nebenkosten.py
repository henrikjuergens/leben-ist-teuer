import numpy as np
import pandas as pd 

max_add_costs = np.genfromtxt('maximale-nebenkosten.csv', delimiter=';')

# Expand with 2004
max_add_costs[0] = [2004, 2.44]

# Apply correction to get average for 2022-2023 based on 2023
max_add_costs[-2:, 1] = max_add_costs[-2:, 1] * (2.51/max_add_costs[-1, 1])
# Correct 2021 due to russian invasion in ukraine
max_add_costs[-3, 1] = 2.3

# Apply correction to get average for 2004-2018 based on 2018
max_add_costs[:-3, 1] = max_add_costs[:-3, 1] * (2.17/max_add_costs[-4, 1])

x_orig = max_add_costs[:, 0]
y_orig = max_add_costs[:, 1]

x_new = np.linspace(x_orig.min(), x_orig.max(), 20)

# Perform linear interpolation
y_new = np.interp(x_new, x_orig, y_orig)

# Combine the new x and y values into a single array
interpolated_data = np.column_stack((x_new, y_new))

column_values = ['Jahr', 'Nebenkosten pro m2']
df = pd.DataFrame(interpolated_data, columns=column_values)
df.to_csv("nebenkosten-m2.csv", sep=';', header=False, index=False)
