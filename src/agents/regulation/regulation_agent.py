import os
from typing import Iterator
from dotenv import load_dotenv
from agno.document.base import Document
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType
from agno.embedder.openai import OpenAIEmbedder

from agno.document.chunking.fixed import FixedSizeChunking
from pydantic import BaseModel, ConfigDict, Field, model_validator

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from agents.base.base_agent import BaseAgent


class RegulationAgent(BaseAgent):
    """社内規定管理を専門とする茶トラ猫エージェント"""
    def __init__(self):
        # データベース接続URL
        db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

        # 社内規定ファイルを読み込む
        regulation_file = "Nyagora社の人事規定.md"

        with open(regulation_file, "r", encoding="utf-8") as f:
            regulation_content = f.read()
        
        # PgVectorを使用してナレッジベースを作成
        self.knowledge_base = DocumentKnowledgeBase(
            documents=[Document(content=regulation_content)],
            vector_db=PgVector(
                table_name="regulations3",
                db_url=db_url,
                search_type=SearchType.hybrid,
                embedder=OpenAIEmbedder(id="text-embedding-3-small"),
            ),
        )
        self.knowledge_base.load(recreate=True)  # テーブルを再作成


        # プロンプトをマークダウンファイルから読み込む
        prompt_file = os.path.join(os.path.dirname(__file__), "regulation_agent_prompt.md")

        with open(prompt_file, "r", encoding="utf-8") as f:
            instructions = f.read()

        # BaseAgentの初期化
        super().__init__(
            name="maru_agent",
            instructions=instructions,
            knowledge=self.knowledge_base,
            search_knowledge=True
        )

def main():
    """スタンドアロンモードでRegulationエージェントをテストする"""
    # 環境変数を読み込む
    load_dotenv()

    print("Dockerコンテナが起動していることを確認してください。")
    print("docker-compose up -d を実行してデータベースを起動してください。")
    
    # エージェントの作成
    agent = RegulationAgent()
    
    if agent.knowledge_base is None:
        print("Error: ナレッジベースの初期化に失敗しました。")
        return

    # 社内規定に関する質問
    regulation_query = "試用期間は何ヶ月ですか？"

    # エージェントの実行
    print(f"\n規定確認リクエスト:\n{regulation_query}\n")
    print("規定確認結果:")
    
    response = agent.run_standalone(regulation_query)
    
    for chunk in response:
        if chunk.content is not None:
            print(chunk.content, end="")
    print("\n\n完了")

if __name__ == "__main__":
    main()
