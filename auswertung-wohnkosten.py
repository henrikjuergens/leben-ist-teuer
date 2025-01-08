import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

life_work_time = 40
flat_size_m2 = 70
housing_prices_m2 = np.genfromtxt('wohungspreise-m2.csv', delimiter=';')[:-1]
additional_costs_m2 = np.genfromtxt('nebenkosten-m2.csv', delimiter=';')
net_income = np.genfromtxt('median-nettoaequivalenzeinkommen.csv', delimiter=';')

lifetime_net_income = net_income
# Assuming 40 year lifetime work time
lifetime_net_income[:, 1] = lifetime_net_income[:, 1] * life_work_time

housing_prices = housing_prices_m2
# Taking a 70m2 flat as the average of the data (60m2-80m2)
lifetime_add_cost = additional_costs_m2[:, 1] * life_work_time * flat_size_m2 * 12
print(lifetime_add_cost)
housing_prices[:, 1] = housing_prices_m2[:, 1] * flat_size_m2 + lifetime_add_cost

housing_lifetime_income_ratio = housing_prices

housing_lifetime_income_ratio[:, 1] = 100 * (housing_lifetime_income_ratio[:, 1] / lifetime_net_income[13:, 1] )

column_values = ['Jahr', 'Anteil Wohnkosten (70m²) am nettoäq. median Lebenszeiteinkommen (40 Jahre Arbeit)']
df = pd.DataFrame(housing_lifetime_income_ratio, columns = column_values)
df['Empfohlenes Maximales Budget'] = 30

my_color = ['b','tab:red']
plt.rcParams['figure.figsize'] = [9, 6]
ax = df.plot(x=0, ylim=[0, 32], color=my_color)
ax.xaxis.set_major_locator(plt.MaxNLocator(8))
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
plt.title('Anteil der Wohnkosten für die Mitte der Gesellschaft', fontsize=16, fontweight='bold', fontname='Arial')
plt.show()