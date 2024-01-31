# data : 20240131
# desc : 박스 플롯

import pandas as pd
import matplotlib.pyplot as plt

mydata = pd.read_csv('mydata.csv')

mydata.boxplot(column='HM_AVG')
plt.show()