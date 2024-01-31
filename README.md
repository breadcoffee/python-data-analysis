# python-data-analysis
python을 활용한 데이터 분석 실습

## 데이터 다루기
- 데이터 로드
'''
import pandas as pd
데이터명 =
pd.read_csv(‘파일경로/파일명.csv’)
'''

- 데이터 생성
'''
import pandas as pd
# dictionary 생성
dictionary 파일명
= {‘컬럼명1’: [‘chr1’,’chr2’,’chr3’], ‘컬럼명2’:
[num1, num2, num3]}
# 변수타입이 character인 경우 값을 작은 따옴표
사이에 입력, 숫자인 경우 숫자만 입력
# dictionary을 DataFame으로 변환
데이터 프레임 파일명 =
pd.DataFrame(dictionary 파일명,
index=[‘a’,’b’,’c’,’d’,’e’])
# index 키워드 뒤에 row 수만큼 index 명칭을 작은
따옴표 사이마다 입력
'''
