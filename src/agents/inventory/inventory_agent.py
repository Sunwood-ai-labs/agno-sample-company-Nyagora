import os
import sys
import pathlib
from dotenv import load_dotenv

# Add the src directory to the path so imports work properly when running standalone
current_dir = pathlib.Path(__file__).parent.absolute()
src_dir = current_dir.parent.parent
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

from agents.base.base_agent import BaseAgent

class InventoryAgent(BaseAgent):
    """在庫管理を専門とする黒猫エージェント"""
    def __init__(self):
        # プロンプトをマークダウンファイルから読み込む
        prompt_file = os.path.join(os.path.dirname(__file__), "inventory_agent_prompt.md")
        
        try:
            with open(prompt_file, "r", encoding="utf-8") as f:
                instructions = f.read()
        except FileNotFoundError:
            # プロンプトファイルが見つからない場合はデフォルトの指示を使用
            instructions = """
            私は黒猫のKuro（クロ）です。在庫管理を担当しています。

            【特徴】
            ・真面目で几帳面な性格を活かし、正確な在庫管理を行います
            ・商品の入出荷、在庫レベルの監視、発注のタイミング管理が得意です
            ・時々「にゃ～」と鳴きながら、在庫の確認をします
            ・語尾に「にゃん」を付けることがあります
            """
        
        super().__init__(
            name="kuro_agent",
            instructions=instructions
        )

def main():
    """スタンドアロンモードでInventoryエージェントをテストする"""
    # 環境変数を読み込む
    load_dotenv()
    
    # テスト用のクエリ
    test_query = """現在の在庫状況を確認してください。特に人気商品のカフェオレカップと
    猫型クッキーの在庫が十分かどうか知りたいです。
    また、先週の売上データと比較して、発注が必要な商品があれば教えてください。"""
    
    # エージェントの作成と実行
    agent = InventoryAgent()
    
    print(f"在庫確認リクエスト:\n{test_query}\n")
    print("在庫確認結果:")
    
    response = agent.run_standalone(test_query)
    
    for chunk in response:
        if chunk.content is not None:
            print(chunk.content, end="")
    print("\n\n完了")

if __name__ == "__main__":
    main()
