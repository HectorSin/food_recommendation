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
a=np.array([])
if reason=="스트레스":
    a=np.append(a,1)
    a=a.astype(int)
elif reason=="지루함":
    a=np.append(a,2)
    a=a.astype(int)
elif reason=="우울함":
    a=np.append(a,3)
    a=a.astype(int)
elif reason=="배고픔":
    a=np.append(a,4)
    a=a.astype(int)
elif reason=="게으름":
    a=np.append(a,5)
    a=a.astype(int)
elif reason=="날씨":
    a=np.append(a,6)
    a=a.astype(int)
elif reason=="행복":
    a=np.append(a,7)
    a=a.astype(int)
elif reason=="여가생활":
    a=np.append(a,8)
    a=a.astype(int)
elif reason=="해당없음":
    a=np.append(a,9)
    a=a.astype(int) 

if fav=="이탈리안/양식":
    a=np.append(a,1)
    a=a.astype(int)
elif fav=="아시안":
    a=np.append(a,2)
    a=a.astype(int)
elif fav=="중국음식":
    a=np.append(a,3)
    a=a.astype(int)
elif fav=="패스트푸드":
    a=np.append(a,4)
    a=a.astype(int)
elif fav=="한식":
    a=np.append(a,5)
    a=a.astype(int)
elif fav=="베이커리/스낵류":
    a=np.append(a,6)
    a=a.astype(int)
elif fav=="건강식":
    a=np.append(a,7)
    a=a.astype(int)
elif fav=="일식":
    a=np.append(a,8)
    a=a.astype(int)

if fruit=="전혀섭취하지않는다":
    a=np.append(a,1)
    a=a.astype(int)
elif fruit=="섭취하지않는다":
    a=np.append(a,2)
    a=a.astype(int)
elif fruit=="보통이다":
    a=np.append(a,3)
    a=a.astype(int)
elif fruit=="섭취한다":
    a=np.append(a,4)
    a=a.astype(int)
elif fruit=="많이섭취한다":
    a=np.append(a,5)
    a=a.astype(int)

if pay=="5천원미만":
    a=np.append(a,1)
    a=a.astype(int)
elif pay=="5천원~1만원":
    a=np.append(a,2)
    a=a.astype(int)
elif pay=="1만원~2만원":
    a=np.append(a,3)
    a=a.astype(int)
elif pay=="2만원~3만원":
    a=np.append(a,4)
    a=a.astype(int)
elif pay=="3만원~4만원":
    a=np.append(a,5)
    a=a.astype(int)
elif pay=="4만원이상":
    a=np.append(a,6)
    a=a.astype(int)

if veggies=="전혀섭취하지않는다":
    a=np.append(a,1)
    a=a.astype(int)
elif veggies=="섭취하지않는다":
    a=np.append(a,2)
    a=a.astype(int)
elif veggies=="보통이다":
    a=np.append(a,3)
    a=a.astype(int)
elif veggies=="섭취한다":
    a=np.append(a,4)
    a=a.astype(int)
elif veggies=="많이섭취한다":
    a=np.append(a,5)
    a=a.astype(int)

user_similarity_scores=df.dot(a) / (np.linalg.norm(df,axis=1)*np.linalg.norm(a))
best_similarity=user_similarity_scores.idxmax()
result=data2.iloc[best_similarity]['result']

