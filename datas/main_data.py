from turtle import width
import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
#----------------------------Positive words------------------------------------------
url = requests.get("https://positivewordsresearch.com/olumlu-sozler-liste/", auth=('user', 'pass'))
# print(url.status_code) ==> 200
content = url.content
soup = BeautifulSoup(content,"html.parser")
data = []
ids = ("a-ile-baslayan-olumlu-kelimeler","b-ile-baslayan-olumlu-kelimeler","c-ile-baslayan-olumlu-kelimeler","d-ile-baslayan-olumlu-kelimeler",
"e-ile-baslayan-olumlu-kelimeler","f-ile-baslayan-olumlu-kelimeler","g-ile-baslayan-olumlu-kelimeler","h-ile-baslayan-olumlu-kelimeler","i-ile-baslayan-olumlu-kelimeler",
"k-ile-baslayan-olumlu-kelimeler","l-ile-baslayan-olumlu-kelimeler","m-ile-baslayan-olumlu-kelimeler","n-ile-baslayan-olumlu-kelimeler","o-ile-baslayan-olumlu-kelimeler",
"p-ile-baslayan-olumlu-kelimeler","r-ile-baslayan-olumlu-kelimeler","s-ile-baslayan-olumlu-kelimeler","t-ile-baslayan-olumlu-kelimeler","u-ile-baslayan-olumlu-kelimeler",
"v-ile-baslayan-olumlu-kelimeler","y-ile-baslayan-olumlu-kelimeler","z-ile-baslayan-olumlu-kelimeler",)
data_a = soup.find("h2",id="a-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_a)
data_b = soup.find("h2",id="b-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_b)
data_c = soup.find("h2",id="a-ile-baslayan-olumlu-kelimeler").next.next.next.next.next.next.next.next.next.next.next.next.next.next.next.text.split(",")
data.extend(data_c)
data_d = soup.find("h2",id="d-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_d)
data_e = soup.find("h2",id="e-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_e)
data_f = soup.find("h2",id="f-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_f)
data_g = soup.find("h2",id="g-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_g)
data_h = soup.find("h2",id="h-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_h)
data_ı = soup.find("h2",id="i-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_ı)
data_k = soup.find("h2",id="k-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_k)
data_l = soup.find("h2",id="l-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_l)
data_m = soup.find("h2",id="m-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_m)
data_n = soup.find("h2",id="n-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_n)
data_o = soup.find("h2",id="o-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_o)
data_p = soup.find("h2",id="p-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_p)
data_r = soup.find("h2",id="r-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_r)
data_s = soup.find("h2",id="s-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_s)
data_t = soup.find("h2",id="t-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_t)
data_u = soup.find("h2",id="u-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_u)
data_v = soup.find("h2",id="v-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_v)
data_y = soup.find("h2",id="y-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_y)
data_z = soup.find("h2",id="z-ile-baslayan-olumlu-kelimeler").next.next.next.text.split(",")
data.extend(data_z)

#data = (data_a,data_b,data_c,data_d,data_e,data_f,data_g,data_h,data_ı,data_k,data_l,data_m,data_n,data_o,data_p,data_r,data_s,data_t,data_u,data_v,data_y,data_z)


#if you want to try this folder, please change csv name

df = pd.DataFrame(data)
df.to_csv("datas/PositiveWords1.csv")

#--------------------------NEGATİVE WORDS-----------------------------------------
url = requests.get("https://www.learnentry.com/english-turkish/negative-words-in-turkish/", auth=('user', 'pass'))
#print(url.status_code) ==> 200
content = url.content
soup = BeautifulSoup(content,"html.parser")
data = []
data_negative = soup.find_all("tbody")
df_negative = pd.DataFrame(data_negative)
df_negative.to_csv("datas/NegativeWords1.csv")

"""

df1 = pd.read_csv("datas/NegativeWordsEng.txt",sep=" ", header=None, names=["NegativeWords"])
read_file_negative = pd.DataFrame(df1)
read_file_negative.to_csv("datas/NegativeWordsEng.csv")


df = pd.read_csv("datas/PositiveWordsEng.txt",sep=" ", header=None, names=["PositiveWords"])
read_file_positive = pd.DataFrame(df)
read_file_positive.to_csv("datas/PositiveWordsEng.csv")
