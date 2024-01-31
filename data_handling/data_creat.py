# data : 20240131
# desc : 데이터 생성

import pandas as pd

# dictionary 생성
data = {'ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
        'X1': [1, 2, 3, 4, 5],
        'X2': [3.0, 4.5, 3.2, 4.0, 3.5]}

# dictionary을 DataFrame으로 변환
mydata = pd.DataFrame(data, index = ['a', 'b', 'c', 'd', 'e'])

print(mydata)