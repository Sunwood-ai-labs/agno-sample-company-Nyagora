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

class RegulationAgent(BaseAgent):
    """社内規定管理を専門とする茶トラ猫エージェント"""
    def __init__(self):
        # プロンプトをマークダウンファイルから読み込む
        prompt_file = os.path.join(os.path.dirname(__file__), "regulation_agent_prompt.md")
        
        try:
            with open(prompt_file, "r", encoding="utf-8") as f:
                instructions = f.read()
        except FileNotFoundError:
            # プロンプトファイルが見つからない場合はデフォルトの指示を使用
            instructions = """
            私は茶トラ猫のMaru（マル）です。社内規定の管理を担当しています。

            【特徴】
            ・社内規定や法令の解釈・適用に関する質問に答えます
            ・規定の更新や変更の提案を行います
            ・コンプライアンスの観点から助言を提供します
            ・時々「にゃ～ん」と鳴きながら、規定書をめくっています
            ・語尾に「にょ」を付けることがあります
            """
        
        super().__init__(
            name="maru_agent",
            instructions=instructions
        )

def main():
    """スタンドアロンモードでRegulationエージェントをテストする"""
    # 環境変数を読み込む
    load_dotenv()
    
    # テスト用のクエリ
    test_query = """新しい衛生管理規定について教えてください。
    また、従業員がマスクを着用し忘れた場合の対応手順も確認したいです。
    最近の法改正で変更された点があれば教えてください。"""
    
    # エージェントの作成と実行
    agent = RegulationAgent()
    
    print(f"規定確認リクエスト:\n{test_query}\n")
    print("規定確認結果:")
    
    response = agent.run_standalone(test_query)
    
    for chunk in response:
        if chunk.content is not None:
            print(chunk.content, end="")
    print("\n\n完了")

if __name__ == "__main__":
    main()
