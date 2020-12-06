# d-challenge-api/yamagoya


# 環境構築
## Python インストール
### 開発時のバージョン
3.9
### 仮想環境構築
本サービスの環境用に構築します
```
python -m venv [newenvname]
```
### 仮想環境に切り替え
```
¥[newenvname]¥Scripts¥activate
```
### ライブラリインスストール
仮想環境に切り替わっている状態で、実行
仮想環境内にインストールされる
```
pip install -r requirements.txt
```

# 起動
仮想環境に切り替わった状態で、
```
uvicorn main:app --reload
```
## 接続確認
http://localhost:8000/tripcost
