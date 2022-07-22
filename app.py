import streamlit as st
import sqlite3
import pandas as pd
import os.path
import datetime

st.sidebar.image('./img/날씨.jpg')
st.sidebar.title('매천 날씨 ')
con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id,pw):
    cur.execute(f"SELECT * FROM users WHERE id = '{id}' and pwd = '{pw}'")
    return cur.fetchone()
menu = st.sidebar.selectbox('MENU', options=['로그인', '회원가입','프로필 촬영','업로드','날씨','불편 사항','불편 사항 내용'])

def weather_1(day):
    cur.execute(f"SELECT * "
                f"FROM weather "
                f"WHERE day='{d}'")
    return cur.fetchone()
def save_uploaded_file(directory, file):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('Saved file : {} in {}'.format(file.name, directory))


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



if menu == '프로필 촬영':


    file_path = os.path.dirname(__file__)
    save_dir=os.path.join(file_path,'img')
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    def save_uploaded_file(uploadedfile, new_name):
        with open(os.path.join(save_dir, uploadedfile.name),'wb')as f:
            f.write(uploadedfile.getbuffer())
        fname, ext = os.path.splitext(uploadedfile.name)

        if os.path.isfile(os.path.join(save_dir, new_name+ext)):
            os.remove(os.path.join(save_dir,new_name+ext))

        os.rename(os.path.join(save_dir, uploadedfile.name),
                os.path.join(save_dir, new_name+ext))
        return st.success('Saved file in img as [{}]'.format(new_name+ext))

    st.subheader('프로필 사진 설정')

    col1, col2 = st.columns(2)
    아이디 = ''

    with col1:
        아이디 = st.text_input('아이디', max_chars=10)

    picture = st.camera_input("사진 촬영")

    if picture:
        if 아이디 is None:
            st.warning('아이디를 확인하세요')
            st.stop()

        st.image(picture)
        save_uploaded_file(picture, 아이디)

if menu == '불편 사항':
    in_id = st.text_input('아이디', max_chars=12)
    in_bul = st.text_input('불편 사항', max_chars=200)
    bul_btn = st.button('제출')

    if bul_btn:
        cur.execute(f"INSERT INTO bul(id,bul) VALUES ("
                    f"'{in_id}', '{in_bul}')")
        con.commit()
        st.success('좋은 의견 감사합니다.')

if menu == '불편 사항 내용':
    st.subheader('불편 사항 내용')
    df = pd.read_sql("SELECT id as 아이디,bul as 불편사항내용 FROM bul", con)
    st.dataframe(df)

if menu == '날씨':
    st.subheader('날씨')
    st.info('날씨를 알고싶은 날을 클릭한 후 확인을 눌러주세요.')
    d = st.date_input(
        ("When?"),
        datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))


    info = weather_1(d)
    if info:
        col1, col2, col3 = st.columns(3)

        col1.metric("기온",info[1]+"°C",info[4]+"°C")
        col2.metric("바람",info[2]+"mph")
        col3.metric("습도", info[3]+"%")
    else:
        st.error('죄송합니다. 그날은 정보가 없습니다. 다른 유저들을 위해 정보를 입력 후 버튼을 눌러주시면 감사하겠습니다.')
        ud = d
        utp = st.text_input('기온을 입력해 주세요.(°C)')
        uch = st.text_input('전일대비 기온변화량을 입력해 주세요.(감소는 "-"를 붙여주시고 증가는 그대로 작성해주세요.)')
        uwd = st.text_input('풍속을 입력해 주세요.(mph)')
        uhd = st.text_input('습도를 입력해 주세요.(%)')
        uwh_btn = st.button('입력')

        if uwh_btn:
            cur.execute(f"INSERT INTO   weather(day, tp, wind, humid, cht) "
                        f"VALUES('{ud}','{utp}','{uwd}','{uhd}','{uch}')")
            con.commit()
            st.success('정보를 입력해 주셔서 감사합니다. 새로고침 해주시면 정보가 적용되었을 것입니다.')

if menu == '업로드':

    st.header("사진을 아이디로 바꾸고 업로드해주세요")
    image_file = st.file_uploader('Upload Image',type=['png','jpg'])

    save_uploaded_file('img', image_file)
    st.sidebar.image(image_file)





