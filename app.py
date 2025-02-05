import streamlit as st
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  # .envファイルからAPIキーを呼び出す。

st.title('RAG チャットボット')

def reset_st_session():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    st.session_state.model = ChatOpenAI(model='gpt-4o-mini') 

if "session_reset_done" not in st.session_state.keys():
    reset_st_session()
    st.session_state.session_reset_done = True
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
if user_prompt := st.chat_input():
    with st.chat_message('user'):
        st.markdown(user_prompt)
    st.session_state.messages.append({'role':'user', 'content':user_prompt})
    
    with st.chat_message('assistant'):
        response = st.write_stream(st.session_state.model.stream(user_prompt))
    st.session_state.messages.append({'role':'assistant', 'content':response})