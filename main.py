import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lastgang = pd.read_excel ('R_strom_34277.xlsx', sheet_name=0)

for _ in lastgang.index:
    lastgang.loc[_, 'Wochentag'] = lastgang.loc[_, 'TimeStamp'].weekday()

# Showing mean, max, min

x = np.mean(lastgang['Mittelwert'])
y = np.max(lastgang['Mittelwert'])
z = np.min(lastgang['Mittelwert'])
print(x, y, z)

# Showing Mittelwert-plot by time

plt.plot(lastgang['TimeStamp'], lastgang['Mittelwert'])
