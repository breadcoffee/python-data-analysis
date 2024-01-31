# data : 20240131
# desc : 상관관계

# numpy를 이용한 상관분석
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([3,2,3,1,2])

print(np.corrcoef(a,b))

# pandas를 이용한 상관분석
import pandas as pd
mydata = pd.read_csv('mydata.csv')

X = mydata.iloc[:,1:4]
print(X.corr(method='pearson'))