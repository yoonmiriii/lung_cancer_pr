import streamlit as st
from home import run_home
from reason import run_reason
from ml import run_ml

from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io



def main() :
    
    menu = ['홈화면', '폐암 환자 통계 보러 가기', '폐암 가능성 예측해보기']

      
    with st.sidebar:
        choice = option_menu('Category', ['홈화면', '폐암 환자 통계 보러 가기', '폐암 가능성 예측해보기'],
                icons=['홈화면', '폐암 환자 통계 보러 가기', '폐암 가능성 예측해보기'],
                menu_icon="메뉴 타이틀 아이콘", default_index=0,
                styles={
                # default_index = 처음에 보여줄 페이지 인덱스 번호
                        "container": {"padding": "5!important", "background-color": "#fafafa"},
                        "icon": {"color": "orange", "font-size": "25px"}, 
                        "nav-link": {"font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                        "nav-link-selected": {"background-color": "#02ab21"},
    } # css 설정
    )


    # choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        run_home()

    elif choice == menu[1] :
        run_reason()

    elif choice == menu[2] :
        run_ml()

if __name__ == '__main__' :
    main()