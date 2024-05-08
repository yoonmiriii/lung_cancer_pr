import streamlit as st
import webbrowser


def run_home() :
    st.title('담배 때문에 답답한 폐?')
    st.header('국내 암 사망률 1위 "폐암"')
    st.image('./image/lung.gif', use_column_width=True)
    st.subheader('폐암의 원인 및 전조증상에 따른 암 발생 데이터를 통해' )
    st.subheader('폐암을 예측해 보자.')
    
    
    st.write('기사 출처')
    link1 = 'https://view.asiae.co.kr/article/2024041923390490966'
    st.write(f'[https://view.asiae.co.kr/article/2024041923390490966]({link1})')
       
    
    st.write('캐글에 있는 survey lung cancer.csv 파일을 사용했습니다.')
    link2 = 'https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer'
    st.write(f'[https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer]({link2})')

    
    
    # html_code = """
    # <a href="https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer" target="_blank">https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer</a>
    # """
    # st.components.v1.html(html_code, height=30)
    
    
    # if st.button('데이터 출처 바로가기') :
    #     webbrowser.open_new_tab(url)
   
    # else : 
    #     st.text('')  