# data : 20240131
# desc : 데이터 로드

import pandas as pd
"""
- pandas 를 이용해 데이터 로드 시 옵션 키워드
    - sep / delimiter : 구분자를 지정합니다.
    - header : header를 컬럼이름으로 지정합니다.
    - index_col : index로 사용할 컬럼을 지정합니다.
    - encoding : 파일의 인코딩을 지정합니다(한글일 경우 매우 중요)
"""

# .CSV 파일 불러오기
mydata = pd.read_csv('C:/Users/user/Desktop/python_total/mydata.csv')

# 파일 불러올 때 index 지정하기
mydata = pd.read_csv('C:/Users/user/Desktop/python_total/mydata.csv', index_col=0)

# .txt 파일 불러오기 (구분자가 |로 되어있을 경우)
mydata = pd.read_csv('C:/Users/user/Desktop/python_total/mydata.csv', sep='|')