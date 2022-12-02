import streamlit as st
import pandas as pd


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

reason=st.multiselect(
    '음식을 선택하는 이유를 선택해주세요',
    ('스트레스','지루함','우울함','배고픔','게으름','날씨','행복','여가생활','해당없음')
    )
    
fav=st.multiselect(
    '좋아하는 음식 종류를 선택해주세요',
    ('이탈리안/양식','아시안','중국음식','패스트푸드','한식','베이커리/스낵류','건강식','일식')
    )

fruit=st.multiselect(
    '과일 섭취량을 선택해주세요',
    ('전혀섭취하지않는다','섭취하지않는다','보통이다','섭취한다','많이섭취한다')
    )
pay=st.multiselect(
    '음식에 지불하는/지불할 비용을 선택해주세요',
    ('5천원미만','5천원~1만원','1만원~2만원','2만원~3만원','3만원~4만원','4만원이상')
    )   
veggies=st.multiselect(
    '야채 섭취량을 선택해주세요',
    ('전혀섭취하지않는다','섭취하지않는다','보통이다','섭취한다','많이섭취한다')
)

l_reason = len(reason)
l_fav = len(fav)
l_fruit = len(fruit)
l_pay = len(pay)
l_veggies = len(veggies)

import pandas as pd
import numpy as np

data=pd.read_csv('food1119.csv')
data.columns=['number',
              'reasons',
              'cuisine',
              'fruit',
              'pay',
              'veggies',
             'result']
data2=data[['reasons','cuisine','fruit','pay','veggies','result']]
df=data[['reasons','cuisine','fruit','pay','veggies']]

# 각 입력값 숫자로 전처리
for va in range(l_reason):
    if reason[va]=="스트레스":
        reason[va] = 1
    elif reason[va]=="지루함":
        reason[va] = 2
    elif reason[va]=="우울함":
        reason[va] = 3
    elif reason[va]=="배고픔":
        reason[va] = 4
    elif reason[va]=="게으름":
        reason[va] = 5
    elif reason[va]=="날씨":
        reason[va] = 6
    elif reason[va]=="행복":
        reason[va] = 7
    elif reason[va]=="여가생활":
        reason[va] = 8
    elif reason[va]=="해당없음":
        reason[va] = 9

for va in range(l_fav):
    if fav[va]=="이탈리안/양식":
        fav[va] = 1
    elif fav[va] =="아시안":
        fav[va] = 2
    elif fav[va]=="중국음식":
        fav[va] = 3
    elif fav[va]=="패스트푸드":
        fav[va] = 4
    elif fav[va]=="한식":
        fav[va] = 5
    elif fav[va]=="베이커리/스낵류":
        fav[va] = 6
    elif fav[va]=="건강식":
        fav[va] = 7
    elif fav[va]=="일식":
        fav[va] = 8

for va in range(l_fruit):
    if fruit[va] =="전혀섭취하지않는다":
        fruit[va] = 1
    elif fruit[va]=="섭취하지않는다":
        fruit[va] = 2
    elif fruit[va]=="보통이다":
        fruit[va] = 3
    elif fruit[va]=="섭취한다":
        fruit[va] = 4
    elif fruit[va]=="많이섭취한다":
        fruit[va] = 5

for va in range(l_pay):
    if pay[va]=="5천원미만":
        pay[va] = 1
    elif pay[va]=="5천원~1만원":
        pay[va] = 2
    elif pay[va]=="1만원~2만원":
        pay[va] = 3
    elif pay[va]=="2만원~3만원":
        pay[va] = 4
    elif pay[va]=="3만원~4만원":
        pay[va] = 5
    elif pay[va]=="4만원이상":
        pay[va] = 6

for va in range(l_veggies):
    if veggies[va]=="전혀섭취하지않는다":
        veggies[va] = 1
    elif veggies[va]=="섭취하지않는다":
        veggies[va] = 2
    elif veggies[va]=="보통이다":
        veggies[va] = 3
    elif veggies[va]=="섭취한다":
        veggies[va] = 4
    elif veggies[va]=="많이섭취한다":
        veggies[va] = 5

result = np.array([])
score = np.array([])
if reason != '선택해주세요' or fav != '선택해주세요' or fruit != '선택해주세요' or pay != '선택해주세요' or veggies != '선택해주세요':
    for a in range(l_reason):
        for b in range(l_fav):
            for c in range(l_fruit):
                for d in range(l_pay):
                    for e in range(l_veggies):
                        al = []
                        al.append(reason[a])
                        al.append(fav[b])
                        al.append(fruit[c])
                        al.append(pay[d])
                        al.append(veggies[e])
                        
                        user_similarity_scores = df.dot(al) / (np.linalg.norm(df,axis=1)*np.linalg.norm(al))
                        best_similarity=user_similarity_scores.idxmax()
                        similarity_score = user_similarity_scores[best_similarity]
                        result = np.append(result, data2.iloc[best_similarity]['result'])
                        score = np.append(score,round((similarity_score*100),2))

st.markdown("<h1 style='text-align: center; color: #808000;'>-----------------</h1>", unsafe_allow_html=True)

if st.button('결과 전송'):
    for a in range(len(result)):
        st.write(f'##### 오늘의 {a+1}번째 추천메뉴는 \'{result[a]}\'입니다. 관련성은 {score[a]}%입니다.')
    if len(result) == 0:
        st.write("입력하지 않은 요소가 있습니다.")
else:
    st.write('##### 오늘의 추천메뉴를 계산하는 중입니다.')