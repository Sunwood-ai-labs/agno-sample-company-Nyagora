import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv

class BaseAgent(Agent):
    """基本エージェントクラス"""
    def __init__(self, name: str, instructions: str, knowledge=None, search_knowledge=None):
        super().__init__(
            name=name,
            knowledge=knowledge,
            search_knowledge=search_knowledge,
            model=OpenAIChat(
                id="gpt-4",
                api_key=os.environ.get("OPENAI_API_KEY")
            ),
            instructions=instructions,
            debug_mode=True
        )

    def run_standalone(self, query: str):
        """スタンドアロンモードでエージェントを実行する"""
        return self.run(query)

def main():
    """スタンドアロンモードでエージェントをテストする"""
    # 環境変数を読み込む
    load_dotenv()
    
    # テスト用のクエリ
    test_query = "これはテストクエリです。基本エージェントの機能をテストします。"
    
    # エージェントの作成と実行
    agent = BaseAgent(
        name="test_agent",
        instructions="これはテスト用の基本エージェントです。クエリに対して応答します。"
    )
    
    print(f"クエリ: {test_query}")
    print("応答:")
    response = agent.run_standalone(test_query)
    
    for chunk in response:
        if chunk.content is not None:
            print(chunk.content, end="")
    print("\n完了")

if __name__ == "__main__":
    main()
