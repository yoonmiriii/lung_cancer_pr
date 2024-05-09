import joblib
import streamlit as st
import numpy as np
import os

def run_ml():
    global regressor  # regressor를 전역 변수로 선언
    regressor = None  # regressor 변수 초기화

    
   
    
    st.subheader('나의 증상에 따른 폐암 여부 예측하기')

    st.text('(총 13문항에 예/아니오를 선택해 주시기 바랍니다)')

    st.write('성별을 선택하세요')
    Gender = st.radio('', ['남자', '여자'], key='Gender')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Gender == '남자':
        Gender = 1
    elif Gender == '여자':
        Gender = 0

    st.write('나이를 입력하세요')
    Age = st.number_input('', min_value=20, max_value=100, value=24)

    st.write('1. 당신은 흡연을 하십니까?')
    Smoking = st.radio('', ['예', '아니오'], key='Smoking')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Smoking == '예':
        Smoking = 1
    elif Smoking == '아니오':
        Smoking = 0

    st.write('2. 당신의 손가락은 황변현상이 있습니까?')
    Yellow = st.radio('', ['예', '아니오'], key='Yellow')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Yellow == '예':
        Yellow = 1
    elif Yellow == '아니오':
        Yellow = 0

    st.write('3. 당신은 불안감을 자주 느끼고 있습니까?')
    Anxiety = st.radio('', ['예', '아니오'], key='Anxiety')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Anxiety == '예':
        Anxiety = 1
    elif Anxiety == '아니오':
        Anxiety = 0

    st.write('4. 친구들과 있으면 불편합니까?')
    Peer_pressure = st.radio('', ['예', '아니오'], key='Peer_pressure')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Peer_pressure == '예':
        Peer_pressure = 1
    elif Peer_pressure == '아니오':
        Peer_pressure = 0

    st.write('5. 갖고 있는 만성질환이 있습니까?')
    Chronic = st.radio('', ['예', '아니오'], key='Chronic')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Chronic == '예':
        Chronic = 1
    elif Chronic == '아니오':
        Chronic = 0

    st.write('6. 당신은 최근에 부쩍 피곤하다고 느끼고 있습니까?')
    Fatigue = st.radio('', ['예', '아니오'], key='Fatigue')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Fatigue == '예':
        Fatigue = 1
    elif Fatigue == '아니오':
        Fatigue = 0

    st.write('7. 알레르기 증상이 있습니까?')
    Allergy = st.radio('', ['예', '아니오'], key='Allergy')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Allergy == '예':
        Allergy = 1
    elif Allergy == '아니오':
        Allergy = 0

    st.write('8. 숨을 쉴 때 "쌕쌕"거리는 소리가 납니까?')
    Wheezing = st.radio('', ['예', '아니오'], key='Wheezing')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Wheezing == '예':
        Wheezing = 1
    elif Wheezing == '아니오':
        Wheezing = 0

    st.write('9. 술을 즐기십니까?')
    Alcohol = st.radio('', ['예', '아니오'], key='Alcohol')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Alcohol == '예':
        Alcohol = 1
    elif Alcohol == '아니오':
        Alcohol = 0

    st.write('10. 기침을 자주 하십니까?')
    Coughing = st.radio('', ['예', '아니오'], key='Coughing')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Coughing == '예':
        Coughing = 1
    elif Coughing == '아니오':
        Coughing = 0

    st.write('11. 숨쉬는 것이 힘들다고 느껴지십니까?')
    Breath = st.radio('', ['예', '아니오'], key='Breath')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Breath == '예':
        Breath = 1
    elif Breath == '아니오':
        Breath = 0

    st.write('12. 음식물을 삼키는 것이 힘드십니까?')
    Swallowing = st.radio('', ['예', '아니오'], key='Swallowing')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Swallowing == '예':
        Swallowing = 1
    elif Swallowing == '아니오':
        Swallowing = 0

    st.write('13. 가슴에 통증이 느껴지십니까?')
    Chest = st.radio('', ['예', '아니오'], key='Chest')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    if Chest == '예':
        Chest = 1
    elif Chest == '아니오':
        Chest = 0
       

    st.subheader('폐암 여부를 예측합니다.')
    
    if st.button('예측하기'):
        new_data = np.array([Gender, Age, Smoking, Yellow, Anxiety, Peer_pressure, Chronic, Fatigue, Allergy, Wheezing, Alcohol, Coughing, Breath, Swallowing, Chest])
        new_data = new_data.reshape(1, -1)

        # 모델 파일 경로 확인
        model_path = './model/regressor.pkl'
        if os.path.exists(model_path):
            # 모델 파일이 존재하는 경우 로드하기
            regressor = joblib.load(model_path)
            pred = regressor.predict(new_data)
            pred = round(pred[0], 1)
            
            if pred == 1:
                st.warning('폐암 가능성이 있습니다.')
            else :
                st.info('건강합니다.')
        
    
    

 
