# data : 20240131
# desc : 데이터 접근

import pandas as pd

'''
- 데이터/변수 접근
    - mydata.columns : 데이터가 보유한 변수명을 확인합니다.
    - mydata.x1 또는 mydata[‘x1’] : 변수열(column)을 선택합니다.
    - mydata.ix[1] 또는 mydata.ix[‘row2’] : 특정 행(row)을 선택합니다.
    - del mydata[‘x1’] : 변수를 삭제합니다.
    - mydata.rename(columns={‘x1':'new_name'}, inplace=True) : 변수명을 변경합니다.
'''

# dictionary 생성
data = {'ID': ['A1', 'A2', 'A3', 'A4', 'A5'],
        'X1': [1, 2, 3, 4, 5],
        'X2': [3.0, 4.5, 3.2, 4.0, 3.5]}

# dictionary을 DataFrame으로 변환
mydata = pd.DataFrame(data, index = ['a', 'b', 'c', 'd', 'e'])

# x1변수를 선택해 상위 행 보기
print(mydata['X1'].head())

# x1변수의 두번째 행부터 4번째 행까지 보기
print(mydata[1:5]['X1'])

# x1변수명을 item1변수명으로 변경
mydata.rename(columns={'X1':'item1'}, inplace=True)