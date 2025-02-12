import streamlit as st

# テキスト(h1)
st.write("# 簡易的なウェブアプリ")

# ユーザーの発言としてテキストを出力する
with st.chat_message('user'):
    st.write('こんにちは！')

# アシスタントの発言としてテキストを出力する
with st.chat_message('assistant'):
    st.write('こんにちは！私はAIアシスタントです！')
    
# chatの入力欄
st.chat_input(placeholder="メッセージを入力")


# # chatの受け取りも可能
# user_prompt = st.chat_input(placeholder="メッセージを入力")
# if user_prompt:
#     with st.chat_message('user'):
#         st.markdown(user_prompt)
#         # session stateの更新
#         st.session_state.user_message = user_prompt

# st.write("## session stateの中身")
# st.session_state

