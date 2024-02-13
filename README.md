# python-data-analysis
python을 활용한 데이터 분석 실습

## 데이터 다루기
- 데이터 로드
```python
import pandas as pd
데이터명 =
pd.read_csv('파일경로/파일명.csv')
```

- 데이터 생성
```python
import pandas as pd

dictionary 파일명 =
{'컬럼명1': ['chr1','chr2','chr3'], '컬럼명2':[num1, num2, num3]}

데이터 프레임 파일명 =
pd.DataFrame(dictionary 파일명,index=['a','b','c','d','e'])
```

- 데이터 접근
```python
import pandas as pd

mydata['x1'].head()

mydata[1:5]['x1']

mydata.rename(columns={'x1':'item1'}, inplace=True)
```

- 데이터 저장
```python
import pandas as pd
데이터명.to_csv('파일을 저장할 경로/파일명.csv', 옵션)
```

## 데이터 탐색과 시각화
- 히스토그램
    - matplotlib(평균 상대습도)
    ![Alt text](/Image_file/image_histogram.png)
    - seaborn(평균 상대습도)
    ![Alt text](/Image_file/image_seaborn.png)

- 박스 플롯
    - 평균 상대습도
    ![Alt text](/Image_file/image_boxplot.png)

- 산점도
    - 강수량에 따른 전운량
        - CA_TOT(일평균 전운량), RN_DAY(강수량)
    ![Alt text](/Image_file/image_scatterplot.png)

## 분석 알고리즘
- 단순선형회귀
    - 일평균 전운량에 따른 일조합(시간) 예측
        - CA_TOT(일평균 전운량), SS_DAY(일조합)
    ![Alt text](/Image_file/image_sunlight.png)

- K-최근접 이웃
    - 일평균 전운량과 평균 상대습도에 따른 비(또는 눈)이 온 날 예측
        - CA_TOT(일평균 전운량), HM_AVG(평균 상대습도)

[K-NN Algorithm 클릭](Data_algorithm/K_NN_Algorithm.ipynb)
    ![Alt text](/Image_file/image_K-NN.png)