import pandas as pd
import matplotlib.pyplot as plt

mydata = pd.read_csv('C:/Users/user/Desktop/python_total/mydata.csv')

mydata.boxplot(column='HM_AVG')
plt.show()