import streamlit as st
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()  # .envファイルからAPIキーを呼び出す。

st.title('RAG チャットボット')

def reset_st_session():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    st.session_state.model = ChatOpenAI(model='gpt-4o-mini') 

if "session_reset_done" not in st.session_state.keys():
    reset_st_session()
    st.session_state.session_reset_done = True
    
def format_prompt(query:str, chat_history:List[Dict[str, str]])->str:
    PROMPT = """
    You are a helpful assistant. Answer the user given the chat history:
    
    chat history: {CHAT_HISTORY}
    user query: {QUERY}
    """
    prompt = ChatPromptTemplate.from_template(PROMPT)
    chat_history = '\n\n'.join([f"{message['role']}: {message['content']}" for message in chat_history])
    prompt = prompt.format(CHAT_HISTORY=chat_history,QUERY=query)
    return prompt
    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
user_prompt = st.chat_input()
if user_prompt:
    with st.chat_message('user'):
        st.markdown(user_prompt)
    st.session_state.messages.append({'role':'user', 'content':user_prompt})
    
    final_prompt = format_prompt(user_prompt,st.session_state.messages)
    
    with st.chat_message('assistant'):
        response = st.write_stream(st.session_state.model.stream(final_prompt))
    st.session_state.messages.append({'role':'assistant', 'content':response})