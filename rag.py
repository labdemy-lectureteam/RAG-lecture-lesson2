from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
import shutil
import os
from langchain_openai import ChatOpenAI
import chromadb

from typing import List, Dict, Any
from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document
import streamlit as st

# PDFファイルの読み込み

# chunk分け

# ベクトルDBの初期化

# Retrieval処理

# promptの整形