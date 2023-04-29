import streamlit as st
import sqlite3
import pandas as pd
import os.path
import datetime
import matplotlib.pyplot as plt
import numpy as np
import math
menu = st.sidebar.selectbox('MENU', options=['그래프 그리기','로그인','회원가입'])
con = sqlite3.connect('database.db')
cur = con.cursor()

st.title('박주휘 웹사이트')




if menu=='그래프 그리기':

    draw_1=st.sidebar.text_input('2차항 계수', placeholder='입력하세요')
    draw_2 = st.sidebar.text_input('1차항 계수', placeholder='입력하세요')
    draw_3 = st.sidebar.text_input('상수항', placeholder='입력하세요')
    draw_btn = st.sidebar.button('N차그리기')
    draw_4 = st.sidebar.text_input('사인 함수',placeholder='입력하세요 ex 3sinx+2: 3,2')
    draw4_btn = st.sidebar.button('사인 그래프 그리기')
    draw_5 = st.sidebar.text_input('코사인 함수', placeholder='입력하세요 ex 3cosx+2: 3,2')
    draw5_btn = st.sidebar.button('코사인 그래프 그리기')
    y = []
    y1 = []
    y2 = []
    if draw_btn:
        for i in range(9):
            c=int(draw_1)*i*i + int(draw_2) * i + int(draw_3)
            print(c)
            y.append(c)
        print(y)
    score = y
    st.line_chart(score)
    if draw4_btn:
        s = draw_4
        a1, b1 = s.split(',')
        print(a1)
        print(b1)
        for i in range(1000):
            sin_ = math.sin(math.radians(int(i)))
            c2=sin_*int(a1)+int(b1)
            print(c2)
            y1.append(c2)
        print(y1)
    score = y1
    st.line_chart(score)
    if draw5_btn:
        s1 = draw_5
        a2, b2 = s1.split(',')
        print(a2)
        print(b2)
        for i in range(1000):
            cos_ = math.cos(math.radians(int(i)))
            c3=cos_*int(a2)+int(b2)
            print(c3)
            y2.append(c3)
        print(y2)
    score = y2
    st.line_chart(score)



if menu == '로그인':


    login_id = st.text_input('아이디', placeholder='아이디를 입력하세요')
    login_pw = st.text_input('패스워드',
                                     placeholder='패스워드를 입력하세요',
                                     type='password')

    login_btn = st.button('로그인')


    if login_btn:
        users_info = login_user(login_id,login_pw)
        file_name = './img/'+users_info[0]+'.jpg'
        if os.path.exists(file_name):
            st.sidebar.image(file_name)
            st.sidebar.write(users_info[4], '님 환영합니다.')
        else :
            st.sidebar.image('./img/commonimage.jpg')
            st.sidebar.write(users_info[4],'님 환영합니다.')

if menu == '회원가입':
    st.subheader('회원가입')
    with st.form('my_form', clear_on_submit=True):
        st.info('다음 양식을 모두 입력 후 제출합니다.')
        in_id = st.text_input('아이디', max_chars=12)
        in_name = st.text_input('성명', max_chars=10)
        in_age = st.text_input('나이', max_chars=3)
        in_pwd = st.text_input('비밀번호', type='password')
        in_pwd_chk = st.text_input('비밀번호 확인', type='password')
        in_gender = st.radio('성별', options=['남', '여'], horizontal=True)

        if st.form_submit_button:
            if in_pwd!=in_pwd_chk:
                st.error('비밀번호가 일치하지 않습니다')
                st.stop()


        submitted = st.form_submit_button('제출')
        if submitted:

            if st.form_submit_button:
                if in_pwd != in_pwd_chk:
                    st.error('비밀번호가 일치하지 않습니다')
                    st.stop()
                cur.execute(f"INSERT INTO users(id, pwd,age , name,gender) VALUES ("
                        f"'{in_id}', '{in_pwd}',{in_age}, '{in_name}', '{in_gender}')")
                st.success('회원가입에 성공했습니다.')

                con.commit()
























