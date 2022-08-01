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

print(f'mean is {x}, max is {y}, and min is {z}')

# Showing Mittelwert-plot by time


plt.plot(lastgang['TimeStamp'], lastgang['Mittelwert'])
plt.xlabel('Zeit')
plt.ylabel('Mittelwert')
plt.show()

plt.scatter(lastgang['TimeStamp'], lastgang['Mittelwert'])
plt.xlabel('Zeit')
plt.ylabel('Mittelwert')
plt.show()

# The cumulative amount of electricity consumption in the months

jan = lastgang['Mittelwert'][0:2976]
feb = lastgang['Mittelwert'][2977:5664]
mar = lastgang['Mittelwert'][5664:8636]
apr = lastgang['Mittelwert'][8636:11516]
may = lastgang['Mittelwert'][11516:14492]
jun = lastgang['Mittelwert'][14492:17372]
jul = lastgang['Mittelwert'][17372:20348]
aug = lastgang['Mittelwert'][20348:23324]
sep = lastgang['Mittelwert'][23324:26204]
oct = lastgang['Mittelwert'][26204:29184]
nov = lastgang['Mittelwert'][29184:32064]
dec = lastgang['Mittelwert'][32064:35040]

SumMittelwertJan = np.sum(jan)
SumMittelwertFeb = np.sum(feb)
SumMittelwertMar = np.sum(mar)
SumMittelwertApr = np.sum(apr)
SumMittelwertMay = np.sum(may)
SumMittelwertJun = np.sum(jun)
SumMittelwertJul = np.sum(jul)
SumMittelwertAug = np.sum(aug)
SumMittelwertSep = np.sum(sep)
SumMittelwertOct = np.sum(oct)
SumMittelwertNov = np.sum(nov)
SumMittelwertDec = np.sum(dec)


x2 = [SumMittelwertJan,SumMittelwertFeb,SumMittelwertMar,SumMittelwertApr,SumMittelwertMay,
      SumMittelwertJun,SumMittelwertJul,SumMittelwertAug,SumMittelwertSep,SumMittelwertOct,
      SumMittelwertNov,SumMittelwertDec]
x3 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

print(f'The cumulative amount of electricity consumption in the months of the year is: {x2}')

# showing pie-chart for the cumulative amount of electricity consumption in the months

plt.pie(x2, labels = x3 )
plt.show()

