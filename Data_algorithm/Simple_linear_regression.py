# data : 20240131
# desc : 단순선형회귀

# 패키지 불러오기
import pandas as pd
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt

# 예제 데이터 로드
mydata = pd.read_csv('data_regression.csv') # 데이터 위치 지정
print(mydata.head()) # 로드 데이터 확인

# 데이터 정제
mydata.loc[mydata['SS_DAY'] == -9] # 20150520 일조합 결측치(-9) 확인
mydata.loc[(mydata['SS_DAY'] != -9) & (mydata['CA_TOT'] == 0.5)] # 20150520을 제외한

#일평균전운량이 0.5였던 날들 확인
mydata.loc[mydata['SS_DAY'] == -9, 'SS_DAY'] = 10.7 # 일조합 결측치에 평균값 10.7 입력

# 단순선형회귀 모델링
result = sm.ols(formula='SS_DAY ~ CA_TOT', data=mydata).fit()

# 회귀분석 결과 요약
print(result.summary())

# 세부 분석 결과 확인
print('< Parameters > \n', result.params) # 회귀계수 출력
print('< Prob (Parameters) > \n', result.pvalues) # 회귀계수에 대한 P-value 출력
print('< Adj. R-squaured > \n', result.rsquared_adj) # 조정된 R-squared 출력
print('< Prob (F-statistic) > \n', result.f_pvalue) # 모형의 적합도 출력

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8, 5))
plt.ylabel('SS_DAY', size=12)
plt.xlabel('CA_TOT', size=12)
ax.plot(mydata.CA_TOT.values, mydata.SS_DAY.values, 'o', label='Data')
ax.plot(mydata.CA_TOT.values, result.fittedvalues, 'b-', label='Regression')
ax.legend(loc='best')

plt.show()