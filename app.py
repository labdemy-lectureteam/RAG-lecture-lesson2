import streamlit as st
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from typing import List, Dict
from rag import *

load_dotenv()  # .envファイルからAPIキーを呼び出す。

st.title('RAG チャットボット')

def reset_st_session():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    st.session_state.model = ChatOpenAI(model='gpt-4o-mini') 
    try:
        documents = load_PDF(path='documents')
    except:
        st.warning('RAGを使うためにはPDFファイルをアップロードしてください', icon="⚠️")
    else:
        chunks = create_chunks(documents=documents, chunk_size=500, chunk_overlap=50)
        embedding_model= OpenAIEmbeddings(model='text-embedding-3-small')
        vector_db = init_vector_db(embedding_model=embedding_model,db_path="database")
        vector_db.add_documents(documents=chunks)
        st.session_state.vector_db = vector_db
        msg = 'PDFデータの準備が完了しました。'
        st.success(msg)
    return

if "session_reset_done" not in st.session_state.keys():
    reset_st_session()
    st.session_state.session_reset_done = True

    
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
user_prompt = st.chat_input()
if user_prompt:
    with st.chat_message('user'):
        st.markdown(user_prompt)
    st.session_state.messages.append({'role':'user', 'content':user_prompt})
    
    # Retreivalとprompt整形
    context = get_context_from_db(st.session_state.vector_db, user_prompt) 
    final_prompt,sources = format_prompt(context, user_prompt,st.session_state.messages)
    
    # 回答と出典の表示
    with st.chat_message('assistant'):
        response = st.write_stream(st.session_state.model.stream(final_prompt))
        formatted_sources = '\n 参考文献：\n' 
        formatted_sources += '\n '.join(f"{idx+1}. {source['source']}, {source['page']}ページ" for idx,source in enumerate(sources))
        st.markdown(formatted_sources)
    st.session_state.messages.append({'role':'assistant', 'content':response+formatted_sources})