# RAG-lecture-lesson2


## 🚀 環境セットアップ

### 1. **Docker のインストール**
Dockerがインストールされていない場合は、以下のリンクからDocker Desktopをダウンロード・インストールしてください。

🔗 [Docker Desktop ダウンロード](https://www.docker.com/products/docker-desktop/)

インストール後、Dockerが正常に動作しているか確認します。
```sh
 docker --version
```

Dockerがインストールされていれば、バージョン情報が表示されます。

### 2. **リポジトリをクローン**
以下のコマンドでリポジトリをクローンします。
```sh
git clone -b todo_branch https://github.com/labdemy-lectureteam/RAG-lecture-lesson2.git
cd RAG-lecture-lesson2
```

### 3. **.envファイルを作成**
ルートディレクトリ下（RAG-lecture-lesson2）で以下のコマンドを実行し .env ファイルを作成してください。
```sh
touch .env
```

エディタで .env ファイルを開き、以下の内容を追加してください（必要に応じて値を変更）。

```txt
OPENAI_API_KEY=your_api_key_here
```

### 4. **Docker イメージをビルド**
アプリケーションのDockerイメージをビルドします。
```sh
docker build -t streamlit-langchain-app .
```

### 5. **コンテナを実行**
以下のコマンドでコンテナを起動します。

mac/linux
```sh
docker run -p 8501:8501 -v $(pwd):/app --rm streamlit-langchain-app
```

windows(power shell)
```sh
docker run -p 8501:8501 -v ${pwd}:/app --rm streamlit-langchain-app
```

この状態で、ブラウザを開いて `http://localhost:8501` にアクセスすると、Streamlitアプリが表示されます。

## 🔄 変更の適用
アプリを更新した場合、新しいパッケージを適用するために、以下の手順を実行してください。

1. **コンテナを停止・削除**
   ```sh
   docker stop $(docker ps -q --filter "ancestor=streamlit-langchain-app")
   docker rm $(docker ps -aq --filter "ancestor=streamlit-langchain-app")
   ```

2. **イメージを再ビルド**
   ```sh
   docker build -t streamlit-langchain-app .
   ```

3. **新しいコンテナを実行**
   ```sh
   docker run -p 8501:8501 streamlit-langchain-app
   ```

## 🛠 トラブルシューティング
### **Dockerが見つからないエラーが発生する場合**
```sh
ERROR: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```
→ **Docker Desktopを起動** し、再度 `docker ps` を実行してください。

### **ポートがすでに使用されている場合**
```sh
ERROR: Bind for 0.0.0.0:8501 failed: port is already allocated.
```
→ 既存のコンテナを停止:
```sh
docker stop $(docker ps -q --filter "ancestor=streamlit-langchain-app")
```
→ 再度 `docker run` を実行。

---

以上で、Streamlit LangChain アプリのセットアップは完了です！🎉
