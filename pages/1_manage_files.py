import streamlit as st
import os
from app import reset_st_session
from streamlit_js_eval import streamlit_js_eval

st.write('## ファイル管理画面')

uploaded_files = st.file_uploader("ファイルをアップロード：",accept_multiple_files=True)
if uploaded_files:
    if not os.path.exists("documents"):
        os.makedirs("documents")
    for uploaded_file in uploaded_files:
        with open(os.path.join("documents",uploaded_file.name),"wb") as f:
            f.write(uploaded_file.getbuffer())
    reset_st_session()    
    msg = 'PDFデータの更新が完了しました。'
    st.session_state.messages.append({'role':'assistant', 'content':msg})
    streamlit_js_eval(js_expressions="parent.window.location.reload()")

st.write('#### ファイル一覧')
files_to_remove = []
if os.path.isdir('documents') and len(os.listdir('documents')) != 0:
    for file_name in os.listdir('documents'):
        remove_file = st.checkbox(file_name)
        if remove_file:
            files_to_remove.append(file_name)

if st.button("選択したファイルを削除",key='delete_files'):
    for file in files_to_remove:
        os.remove(f'documents/{file}')
    st.rerun()
    # streamlit_js_eval(js_expressions="parent.window.location.reload()")
    
