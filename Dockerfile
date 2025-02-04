# Python公式のimageを使う
FROM python:3.10

# working directoryの指定
WORKDIR /app

# requirementsファイルをコピー
COPY requirements.txt requirements.txt

# 依存パッケージのインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリのコードをコンテナ内へコピー
COPY . .

# Streamlitのデフォルトポートを解放
EXPOSE 8501

# streamlitアプリの実行
# CMD ["streamlit", "run", "hello_world.py", "--server.port=8501", "--server.address=0.0.0.0"]
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
