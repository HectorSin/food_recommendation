import streamlit as st
import pandas as pd

# 로그인
# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data



def main():
	"""Simple Login App"""

	st.title("O_오늘_M_뭐_M_먹지")

	menu = ["Home","SignUp","Login"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")

	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("회원 가입에 필요한 Username과 Password를 ")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()


st.markdown("<h1 style='text-align: center; color: #008080;'>사용자 정보 기반 메뉴 추천</h1>", unsafe_allow_html=True)

st.markdown("#### 안녕하세요, 팀25의 '오늘 뭐먹지'입니다.\
            <br>사용자 정보를 기반으로 메뉴를 추천해드립니다!", unsafe_allow_html=True)

reason=st.selectbox(
    '음식을 선택하는 이유를 선택해주세요',
    ('스트레스','지루함','우울함','배고픔','게으름','날씨','행복','여가생활','해당없음')
    )
    
fav=st.selectbox(
    '좋아하는 음식 종류를 선택해주세요',
    ('이탈리안/양식','아시안','중국음식','패스트푸드','한식','베이커리/스낵류','건강식','일식')
    )

fruit=st.selectbox(
    '과일 섭취량을 선택해주세요',
    ('전혀섭취하지않는다','섭취하지않는다','보통이다','섭취한다','많이섭취한다')
    )
pay=st.selectbox(
    '음식에 지불하는/지불할 비용을 선택해주세요',
    ('5천원미만','5천원~1만원','1만원~2만원','2만원~3만원','3만원~4만원','4만원이상')
    )   
veggies=st.selectbox(
    '야채 섭취량을 선택해주세요',
    ('전혀섭취하지않는다','섭취하지않는다','보통이다','섭취한다','많이섭취한다')
)

st.write('선택하신 결과 :',reason,'/',fav,'/',fruit,'/',pay,'/',veggies)



st.markdown("<h1 style='text-align: center; color: #808000;'>-----------------</h1>", unsafe_allow_html=True)
st.markdown("##### 오늘의 추천메뉴는 \'{}\'입니다.".format(result))
     



