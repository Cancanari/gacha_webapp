import streamlit as st
from random import randint

st.title("ガチャシュミレーションアプリ")
st.caption("10連ガチャを引くアプリです")

prob = [85, 10, 5]
sum_prob = sum(prob)

with st.form(key='gacha'):
	#ボタン
	submit_btn = st.form_submit_button('ガチャを引く')
	if submit_btn == True:
		st.text("ガチャを引きます")
		for i in range(10):
			value = randint(1, sum_prob)
			rare = 1
			sum_p = 0
			for p in prob:
				sum_p += p
				if value <= sum_p:
					st.text("レア度"+("💓"*rare)+"を引いた！")
					break
				rare += 1