# Nyagora エージェントシステム - デバッグガイド

このガイドでは、Nyagoraエージェントシステムの各エージェントをスタンドアロンモードでデバッグする方法について説明します。

## 準備

1. 環境変数の設定
   - `.env` ファイルにAPIキーが正しく設定されていることを確認してください
   - 例: `OPENAI_API_KEY=sk-your-api-key`

2. 必要なライブラリのインストール
   ```bash
   pip install -r requirements.txt
   ```

## 各エージェントの単体実行

各エージェントは個別に実行してテストできます。以下のコマンドを使用してください。

### 基本エージェント (BaseAgent)

```bash
python src/agents/base/base_agent.py
```

### 要約エージェント (Summary Agent - Mike)

```bash
python src/agents/summary/summary_agent.py
```

### 翻訳エージェント (Translation Agent - Siam)

```bash
python src/agents/translation/translation_agent.py
```

### 在庫管理エージェント (Inventory Agent - Kuro)

```bash
python src/agents/inventory/inventory_agent.py
```

### 規定管理エージェント (Regulation Agent - Maru)

```bash
python src/agents/regulation/regulation_agent.py
```

### チーム管理エージェント (Team Agent - Manager)

```bash
python src/agents/team/team_agent.py
```

## プロンプトの編集

各エージェントのプロンプトはマークダウンファイルとして、対応するエージェントのディレクトリに保存されています：

- `src/agents/summary/summary_agent_prompt.md`
- `src/agents/translation/translation_agent_prompt.md`
- `src/agents/inventory/inventory_agent_prompt.md`
- `src/agents/regulation/regulation_agent_prompt.md`
- `src/agents/team/team_agent_prompt.md`

これらのファイルを編集することで、エージェントの動作をカスタマイズできます。

## アプリケーションの実行

完全なアプリケーションを実行するには：

```bash
streamlit run src/app.py
```

## デバッグのヒント

1. 各エージェントを単体で実行して、期待どおりに機能するか確認する
2. 問題がある場合は、プロンプトを調整する
3. チームエージェントを実行して、エージェント間の連携が正常に機能するか確認する
4. デバッグモードは各エージェントで有効になっているため、詳細なログを確認できる
