import streamlit as st
import webbrowser


def run_home() :
    st.title('담배 때문에 답답한 폐?')
    st.header('국내 암 사망률 1위 "폐암"')
    st.text('')
    st.text('')
    st.markdown("""<style> h2 { color: red; } </style>""", unsafe_allow_html=True)
    st.image('./image/lung.gif', use_column_width=True)
    st.subheader('폐암의 원인 및 전조증상에 따른 암 발생 데이터를 통해' )
    st.subheader('폐암을 예측해 보자.')

    
    st.write('현재 국내 암사망율 1위는 폐암이라고 한다. 이전에 폐암은 흡연자만 걸린다고 알고 있었지만, 요즘 들어 비흡연자들도 폐암으로 사망하는 경우가 많은 것을 볼 수 있다. 폐암은 초기 증상이 없어서 발견하기가 더욱 힘든데, 내 몸에 나타나는 여러 증상들을 통해 폐암 가능성이 있는지 예측해 보자.')
  
    st.write('Streamlit으로 웹 대시보드를 만들었고, Matplotllib의 Pie 차트로 증상별 폐암 환자의 분포도를 나타냈으며, LogisticRegression를 통해 폐암 가능성을 예측하였다.')
    
    st.text('기사 출처')
    link1 = 'https://view.asiae.co.kr/article/2024041923390490966'
    st.write(f'[https://view.asiae.co.kr/article/2024041923390490966]({link1})')
       
    
    st.text('캐글에 있는 survey lung cancer.csv 파일을 사용했습니다.')
    link2 = 'https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer'
    st.write(f'[https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer]({link2})')

    
    
    