import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mydata = pd.read_csv('C:/Users/user/Desktop/python_total/mydata.csv')
mydata['HM_AVG'].hist()

plt.figure(figsize=(10,5))
sns.distplot(mydata.HM_AVG, kde =False) # kde : 가우시안 확률밀도 여부
plt.show()