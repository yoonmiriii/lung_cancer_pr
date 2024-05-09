import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager
 
# 폰트 전체 리스트 확인
[i.fname for i in matplotlib.font_manager.fontManager.ttflist]
 
# 나눔 폰트 설치 확인
[f.name for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name]


import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')


def run_reason() :
    st.header('폐암 데이터 보기')
    st.markdown("""<style> h2 { color: #FF6347; } </style>""", unsafe_allow_html=True)

    st.text('')
    st.text('')
    st.text('')

    st.subheader('다양한 현상들에 따른 폐암 발병 데이터')

    df = pd.read_csv('./data/survey_lung_cancer.csv')
    
    # if st.button('데이터 보기', help='클릭해주세요.', use_container_width=True) :
    st.dataframe(df)

    st.text('')
    st.text('')
    st.text('')

    
    st.subheader('연령별 폐암 환자 수를 보여드립니다.')
    if st.button('그래프 보기', help='클릭해주세요.', use_container_width=True):
        df_cancer = df.loc[df['폐암'] == 'YES', ]
        my_bins = np.arange(20, 90+10, 10)
        fig1 = plt.figure()
        plt.hist(data= df_cancer, x= '나이', rwidth=0.9, bins = my_bins) 
        plt.title('나이대별 폐암 환자 수')
        plt.xlabel('나이')
        plt.ylabel('폐암 환자수(명)')
        plt.legend()
        st.pyplot(fig1) 

        st.text('')
        st.text('')
        st.text('')


    
    st.subheader('증상을 선택하면, 폐암 환자의 각 증상별 분포를 보여드립니다.')
    column_list = ['선택해주세요','성별', '흡연여부', '노란색손가락', '심리가불안정함', '또래압박', '만성질환', '피로감', '알레르기', '천명음', '음주', '기침', '숨가쁨', '삼키기어려움', '가슴통증']

    my_choice = st.selectbox('', column_list)
    df_cancer = df.loc[df['폐암'] == 'YES', ]
        
    if my_choice == column_list[0] : 
        st.text('')
    
    elif my_choice == column_list[1] : 
        df2 = df_cancer['성별'].value_counts()
        fig2 = plt.figure() 
        plt.pie(df2, labels= df2.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig2)

    elif my_choice == column_list[2] :
        df3 = df_cancer['흡연여부'].value_counts()
        fig3 = plt.figure() 
        plt.pie(df3, labels= df3.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig3)

    elif my_choice == column_list[3] :
        df4 = df_cancer['노란색손가락'].value_counts()
        fig4 = plt.figure() 
        plt.pie(df4, labels= df4.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig4)

    elif my_choice == column_list[4] :
        df5 = df_cancer['심리가불안정함'].value_counts()
        fig5 = plt.figure() 
        plt.pie(df5, labels= df5.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig5)

    elif my_choice == column_list[5] :
        df6 = df_cancer['또래압박'].value_counts()
        fig6 = plt.figure() 
        plt.pie(df6, labels= df6.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig6)

    elif my_choice == column_list[6] :
        df7 = df_cancer['만성질환'].value_counts()
        fig7 = plt.figure() 
        plt.pie(df7, labels= df7.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig7)

    elif my_choice == column_list[7] :
        df8 = df_cancer['피로감'].value_counts()
        fig8 = plt.figure() 
        plt.pie(df8, labels= df8.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig8)

    elif my_choice == column_list[8] :
        df9 = df_cancer['알레르기'].value_counts()
        fig9 = plt.figure() 
        plt.pie(df9, labels= df9.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig9)

    elif my_choice == column_list[9] :
        df10 = df_cancer['천명음'].value_counts()
        fig10 = plt.figure() 
        plt.pie(df10, labels= df10.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig10)

    elif my_choice == column_list[10] :
        df11 = df_cancer['음주'].value_counts()
        fig11 = plt.figure() 
        plt.pie(df11, labels= df11.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig11)

    elif my_choice == column_list[11] :
        df12 = df_cancer['기침'].value_counts()
        fig12 = plt.figure() 
        plt.pie(df12, labels= df12.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig12)

    elif my_choice == column_list[12] :
        df13 = df_cancer['숨가쁨'].value_counts()
        fig13 = plt.figure() 
        plt.pie(df13, labels= df13.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig13)

    elif my_choice == column_list[13] :
        df14 = df_cancer['삼키기어려움'].value_counts()
        fig14 = plt.figure() 
        plt.pie(df14, labels= df14.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig14)

    elif my_choice == column_list[14] :
        df15 = df_cancer['가슴통증'].value_counts()
        fig15 = plt.figure() 
        plt.pie(df15, labels= df15.index, autopct='%.1f', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('')
        plt.legend()
        st.pyplot(fig15)

    else : 
        st.text('')

    

  

    # st.info(f'선택하신 {choice_column}의 최대 데이터는 다음과 같습니다.')
    # st.dataframe(df.loc[df[choice_column] == df[choice_column].max(), ])

    # st.info(f'선택하신 {choice_column}의 최소 데이터는 다음과 같습니다.')
    # st.dataframe(df.loc[df[choice_column] == df[choice_column].min(), ])

    # st.subheader('상관관계 분석')
    # st.text('컬럼들을 2개 이상 선택하면, 컬럼들의 상관계수를 보여드립니다.')

    # corr_column_list = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    # selected_columns = st.multiselect('컬럼을 선택하세요.', corr_column_list)
    
    # # 2개 이상 선택했을때와 그렇지 않을때로 개발
    # if len(selected_columns) >= 2 : 
    #     # 1. 페어플롯을 그린다.
    #     # todo : 
    #     # 1.pairplot 을 다른 라이브러리 이용해서 하는 방법
    #     fig1 = sb.pairplot(data=df, vars = selected_columns)
    #     st.pyplot(fig1)

    #     # 2.pairplot 말고, 반복문으로 두 컬럼씩의 관계를 차트로 그리는 방법
             

    #     # 2. 상관계수 보여준다.
    #     st.dataframe(df[selected_columns].corr())
        
    # else :
    #     st.text('컬럼은 2개 이상 선택해야 합니다.')
