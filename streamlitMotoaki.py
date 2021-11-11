# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:12:29 2021

@author: kutsu
"""

import streamlit as st


st.title("初めてのstreamlit")
st.write("私の名前は元章です")
text = st.text_input("あなたの名前を教えてください")
"あなたの名前は、",text,"です！"

condition = st.slider("あなたの今の調子は？",0,100,50)
"コンディション:",condition

option = st.selectbox("好きな数字を教えてください", list(["１番","２番","３番","４番"]))
"あなたが選択したのは、",option,"です"

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")
    
