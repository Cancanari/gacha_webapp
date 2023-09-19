import streamlit as st
from PIL import Image
import datetime

st.title("⚔谷山の冒険⚔")
st.caption("目指せ！　フリーランスへの道🌟")
st.subheader("自己紹介")
st.text("好きなVTuberは白上フブキです🦊　僕はホロライブのゲームを創る為に頑張ります！")
st.text("ここからはイマジナリーフブちゃんが担当します🌟")
code = '''
include<stdio.h>
int main(){
	int x = 0;
	printf("%d",x);
	return 0;
}
'''
st.code(code, language='c')

#画像
image = Image.open("unnamed.png")
st.image(image,width=200)

with st.form(key='profile_form'):
	#テキストボックス
	name = st.text_input('🦊あなたの名前を教えて🦊')

	#セレクトボックス
	age_category = st.selectbox("白上フブキ好き度",("大好き","普通","えーっと"))

	#ラジオボタン
	age_category1 = st.radio("白上フブキ知ってる度",("めっちゃ知ってる","知ってる","知らない"))

	#複数選択
	hobby = st.multiselect("好きなVTuber",("白上フブキ","儒烏風亭らでん","その他"))

	#チェックボックス
	st.checkbox("メールマガジンを購読する")

	#スライダー
	height = st.slider("白上フブキ知名度",min_value =0,max_value=100 )

	#日付
	start_date = st.date_input("開始日",datetime.date(2023,9,19))

	#カラーピッカー
	color = st.color_picker("テーマカラー","#E0FFFF")

	#ボタン
	submit_btn = st.form_submit_button('フブちゃんとお話しましょう🍖')
	if submit_btn == True:
		st.text("はじめまして～♪　"+ name +"さん")