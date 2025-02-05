import streamlit as st
import os
from streamlit_js_eval import streamlit_js_eval
from app import reset_st_session

st.write('## ファイル管理画面')

if uploaded_files := st.file_uploader("ファイルをアップロード：",accept_multiple_files=True):
    if not os.path.exists("documents"):
        os.makedirs("documents")
    for uploaded_file in uploaded_files:
        with open(os.path.join("documents",uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getbuffer())
    reset_st_session()    
    msg = 'PDFデータの更新が完了しました。'
    st.session_state.messages.append({'role':'assistant', 'content':msg})
