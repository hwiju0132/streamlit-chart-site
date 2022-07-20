import streamlit as st
#타이틀
st.title('안녕하세요')
st.write("박주휘")
#버튼
import streamlit as st

if st.button('버튼'):
     st.write('버튼 클릭 성공')
else:
     st.write('안녕하세요!!!')
#다운로드 버튼
import streamlit as st

text_contents = '''ㅗㅗㅗㅗㅗ.'''
st.download_button('다운로드', text_contents)
#선택지
import streamlit as st

st.subheader('1. Checkbox test')
a = st.checkbox('1번')
b = st.checkbox('2번')
c = st.checkbox('3번')

if a:
    st.write('1번을 선택하셨습니다.')
if b:
    st.write('2번을 선택하셨습니다.')
if c:
    st.write('3번을 선택하셨습니다.')
#라디오 버튼
st.subheader('2. radio button test')
food = st.radio(
     "좋아하는 음식은 무엇인가요?",
     ('초밥', '짜장면', '김치볶음밥'))

if food == '초밥':
    st.write('You selected 초밥.')
elif food == '짜장면':
    st.write('You selected 짜장면.')
elif food == '김치볶음밥':
    st.write('You selected 김치볶음밥')
#로그인 폼
menu = st.sidebar.selectbox('MENU', options=['로그인', '회원가입', '회원목록'])

if menu == '로그인':
    st.subheader('로그인')
    st.sidebar.subheader('로그인')

    login_id = st.sidebar.text_input('아이디', placeholder='아이디를 입력하세요')
    elogin_pw = st.sidbar.text_input('패스워드',
                                     placeholder='패스워드를 입력하세요',
                                     type='password')

    login_btn = st.sidebar.button('로그인')

    if login_btn:
        st.sidebar.write(login_id)
        st.sidebar.write(login_pw)

if menu == '회원가입':
    st.subheader('회원가입')
    st.sidebar.write('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    st.sidebar.write('회원목록')
