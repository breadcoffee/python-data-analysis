# data : 20240131
# desc : 산점도

import matplotlib.pyplot as plt
import pandas as pd

mydata=pd.read_csv('mydata.csv')

plt.scatter(mydata['RN_DAY'],
mydata['CA_TOT'],color='b', marker='o')
plt.xlabel('RN_DAY')
plt.ylabel('CA_TOT')
plt.show()