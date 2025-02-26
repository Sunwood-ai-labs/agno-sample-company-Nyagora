<div align="center">

![Nyagora](https://github.com/user-attachments/assets/518ff441-3d1e-409f-b116-df79852208fe)

# 🐱 Nyagora - 猫のエージェントシステム

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

</div>

## 🌟 システム概要

Nyagoraは、賢い猫たちがあなたのタスクをサポートする特別なAIエージェントシステムです。
Streamlitを利用した直感的なインターフェースと、個性豊かな猫エージェントたちが、
あなたの要望に優しく寄り添いながら、効率的な解決策を提供します。

### 🐱 猫エージェントの紹介

1. **Mike（三毛猫）- 要約スペシャリスト**
   - 細かい観察力を活かした正確な要約
   - のんびりと丁寧な仕事が得意

2. **Siam（シャム猫）- フランス語翻訳エキスパート**
   - 気品のある洗練された翻訳
   - フランス文化への深い造詣

## 📁 プロジェクト構成
- `src/agents/agent_definitions.py`: エージェントの定義を行うファイルです。ここでは、エージェントの特性や役割を定義します。

- `src/agents/team_agent.py`: チームエージェントのロジックを実装するファイルです。エージェント間のタスクの委任や、ユーザーからのリクエストに対する応答を管理します。

- `src/utils/__init__.py`: ユーティリティモジュールの初期化ファイルです。共通のヘルパー関数をインポートするための準備をします。

- `src/utils/stream_helpers.py`: ストリーミング出力を管理するためのヘルパー関数を含むファイルです。リアルタイムでの応答更新をサポートします。

- `.env.example`: 環境変数の例を示すファイルです。APIキーなどの設定を行うためのテンプレートです。

- `.gitignore`: Gitで無視するファイルやディレクトリを指定するファイルです。

- `requirements.txt`: プロジェクトに必要なPythonパッケージのリストを含むファイルです。依存関係を管理します。

## セットアップ手順

1. リポジトリをクローンします。
   ```bash
   git clone <リポジトリのURL>
   cd agent-system
   ```

2. 必要なパッケージをインストールします。
   ```
   pip install -r requirements.txt
   ```

3. 環境変数を設定します。`.env.example`を参考にして、必要な環境変数を設定してください。

4. アプリケーションを実行します。
   ```
   streamlit run src/app.py
   ```

5. ブラウザで表示されたURLにアクセスして、エージェントシステムを利用します。

## 使用方法

1. アプリケーションを起動すると、Nyagoraの猫エージェントたちが待機しています
2. テキストエリアにリクエストを入力します
3. 「送信」ボタンをクリックすると、猫たちが楽しく「にゃ～ん」と鳴きながら作業を開始します
4. 進捗状況がリアルタイムで表示され、担当した猫エージェントも確認できます
5. 処理が完了すると、「にゃ！」という元気な声とともに結果と処理時間が表示されます


## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細はLICENSEファイルを参照してください。
