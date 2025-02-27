# 社内規定RAGエージェント

茶トラ猫のMaruが社内規定に関する質問に答えるRAGエージェントです。PostgreSQLのpgvectorを使用して、ベクターデータベースによる効率的な検索を実現しています。

## セットアップ手順

1. 必要なパッケージをインストール：
```bash
pip install openai sqlalchemy 'psycopg[binary]' pgvector agno python-dotenv
```

2. 環境変数の設定：
`.env`ファイルを作成し、OpenAI APIキーを設定：
```
OPENAI_API_KEY=your_api_key_here
```

3. ベクターデータベースの起動：
```bash
docker-compose up -d
```

4. エージェントの実行：
```bash
python regulation_agent.py
```

## 使用方法

エージェントに社内規定に関する質問をすることができます。例：
- 「試用期間は何ヶ月ですか？」
- 「ハラスメントに関する規定について教えてください」
- 「懲戒処分の種類を教えてください」

## システム構成

- RAGエージェント: `agno`フレームワークを使用
- ベクターデータベース: PostgreSQL + pgvector
- 知識ベース: Markdownファイルで管理された社内規定

## トラブルシューティング

### データベース接続エラー
- Docker Composeが実行されているか確認
- `docker-compose ps`でコンテナの状態を確認
- ポート5532が利用可能か確認

### OpenAI APIエラー
- .envファイルが正しく設定されているか確認
- APIキーの有効性を確認

## 注意事項

- 本システムは社内規定の参照・解釈を支援するものですが、最終的な判断は人間が行ってください
- 重要な決定を行う際は、必ず原文の規定を確認してください
