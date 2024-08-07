![waving](https://capsule-render.vercel.app/api?type=waving&height=200&text=Predict_Lung_cancer&fontAlign=50&fontAlignY=40&color=gradient)

# 파일이름 : lung_cancer_pr
> ## 국내 암 사망율 1위인 폐암 가능성을 예측해 보자.

 > ### :warning: 폐암의 원인과 전조증상에 따른 암 발생 데이터를 기반으로 나의 현재상태로는 암 발생 가능성이 있는지 예측해보자.

 > #### 현재 국내 암사망율 1위는 폐암이라고 한다. 이전에 폐암은 흡연자만 걸린다고 알고 있었지만, 요즘 들어 비흡연자들도 폐암으로 사망하는 경우가 많은 것을 볼 수 있다. 폐암은 초기 증상이 없어서 발견하기가 더욱 힘든데, 내 몸에 나타나는 여러 증상들을 통해 폐암 가능성이 있는지 예측해 보자.


---

|인터프리터 언어|데이터분석|웹 대시보드 Tool|플랫폼|배포|
|:------:|:------:|:---------:|:-----:|:--------:|
|<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>|<img src="https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white /">|<img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/>|<img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white"/>|<img src="https://img.shields.io/badge/Amazon%20EC2-FF9900?style=for-the-badge&logo=Amazon%20EC2&logoColor=white">|

---
**작업순서**<br>
    데이터 주제 선정 ➡︎ 라이브러리 및 데이터 불러오기 ➡︎ 데이터 확인하기 ➡︎ 전처리, 변수 변환하기 ➡︎ Matplotlib로 차트 그리기 ➡︎모델링 및 예측하기 ➡︎ 예측 모델 평가하기 ➡︎ Python 프레임워크 Streamlit으로 웹 대시보드 개발 ➡︎ AWS EC2 배포

---
<br>
<br>

:pencil: 데이터 주제 선정 
-
폐암은 국내 암 사망율 1위이지만, 초기 증상이 없어 발견하기 어렵다고 한다. 그래서 증상이 나타나면 이미 손쓸 수가 없는 상태인 경우가 많아 사망율이 높지만, 초기에 발견해서 수술을 하면 완치율이 90% 정도로 양호한 질병이기도 하다.<br> 이런 폐암을 초기에 발견하면 좋을 것 같다는 생각에 프로젝트를 진행해 보았다.
  
<br>

:pencil: 라이브러리 및 데이터 블러오기
-
  데이터 파일(.csv)을 판다스 라이브러리를 이용하여 불러와서 데이터분석을 했습니다.<br> 

<br>

:pencil: 데이터 확인하기
-
 head()함수를 사용하여 상위 5개 행만 출력해 데이터를 확인했습니다.

<br>

:pencil: 전처리, 변수 변환하기
-
 머신러닝을 위해 데이터셋에 object로 되어 있는 변수들을 사이킷런 라이브러리의 LabelEncoder를 이용하여 숫자화 했습니다.

<br>

:pencil: Matplotlib로 차트 그리기
-
 - histogram으로 연령별 폐암 환자수를 나타냈습니다. <br>
 - 성별 및 모든 증상에 따른 폐암 환자 분포도를 pie차트로 나타냈습니다. 

<br>

:pencil: 모델링 및 예측하기
-
 - 모델링 하기 전 변수들을 X와 y값으로 나누었습니다.
 - X 값은 df.drop('y값', axis=1) 함수를 사용하여 y값을 제외한 모든 컬럼이 포함될 수 있도록 했습니다.
 - 사이킷런의 데이터 분리 모듈(.model_selection)을 이용하여 train 셋과 test 셋으로 나누었습니다.
 - test 셋 사이즈는 20%로 할당했습니다.
 - 사이킷런의 머신러닝 알고리즘 모듈(.linear_model)을 이용하여 로지스틱 회귀 모델을 생성하고, 모델을 학습시켰습니다.
 - os 라이브러리로 새 디렉토리를 생성하고, joblib 라이브러리로 예측데이터(.pkl) 생성했습니다.<br>

<br>

:pencil: 예측 모델 평가하기
-
 - 사이킷런의 평가 모듈(.metrics)을 이용하여 실제값과 예측값의 정확도를 평가하였습니다.
 - accuracy_score ≒ 0.87 의 인공지능이 생성되었습니다.

 <br>

:pencil: Streamlit으로 웹 대시보드 개발
-

- APP<br>
  * 사이드바를 통해서 웹 대시보드의 카테고리를 표시했습니다.<br>
  * 사이드바를 나타내기 위한 streamlit_option_menu는 파이썬에 기본 라이브러리가 아니여서, cmd에서 pip install streamlit_option_menu로 설치했습니다.<br>
- HOME <br>
  * 프로젝트 계기가 된 기사 출처 표시했습니다.<br>
  * 캐글에서 가져온 데이터 출처를 표시했습니다.<br>
  * 프로젝트의 주제 및 내용을 설명했습니다.<br>
- REASON<br>
  * 데이터를 데이터프레임형식으로 노출되게 했습니다.<br>
  * 연령별 폐암 환자수 그래프는 버튼 함수를 사용해서, 버튼을 눌러야 노출될 수 있도록 했습니다.<br>
  * 성별 및 증상별 폐암 환자수를 나타낸 파이차트는, 셀렉트박스 함수를 사용하여 컬럼을 선택할 수 있도록 했습니다.<br>
- ML<br>
  * 예측자의 성별과 여러 증상이 있는지 여부는 라디오 함수로 선택할 수 있도록 했습니다.<br>
  * 나이는 넘버인풋 함수로 기재할 수 있도록 했습니다.<br>
  * 선택한 데이터를 바탕으로 폐암 가능성이 있는 경우는 warning 메시지로 표시했습니다.<br>
  * 폐암 가능성이 없는 경우는 info 메시지로 표시했습니다.<br>
<br>

:pencil:  AWS EC2 배포
-
  - Github에 해당 프로젝트를 위한 새 리포지토리를 public으로 생성했습니다.
  - VScode와 깃허브를 연동하여, 수정작업 후 VScode의 소스컨트롤을 사용하여 다이렉트로 커밋과 git에 푸쉬를 했습니다.
  - AWS 프리티어 계정으로 EC2 인스턴스 생성하여, 웹 서비스를 사용했습니다.

<br>
<br>

> **데이터 출처**<br><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" /><br>
 survey lung cancer.csv 파일
 <https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer><br>
    
    

> **기사 출처**
 <https://view.asiae.co.kr/article/2024041923390490966>
> 
 
