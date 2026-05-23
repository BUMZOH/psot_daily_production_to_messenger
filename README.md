## 動作環境
Windows11
Python 3.12.10

## 環境構築
1.プログラムダウンロード
git clone https://github.com/BUMZOH/psot_daily_production_to_messenger.git

2.仮想環境構築
python -m venv .venv

3.仮想環境有効化
.venv\\Scripts\\activate

4.必要モジュールインストール
pip install -r requiments.txt

5.playwright用ブラウザインストール
playwright install

## 実行方法
run.batを実行
※仮想環境を自動で切り替えるため、main.pyではなく、run.batを使うこと

## アプリのアップデート
git pull