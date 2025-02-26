import os
import sys
import pathlib
from dotenv import load_dotenv

# Add the src directory to the path so imports work properly when running standalone
current_dir = pathlib.Path(__file__).parent.absolute()
src_dir = current_dir.parent.parent
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agents.summary.summary_agent import SummaryAgent
from agents.translation.translation_agent import TranslationAgent
from agents.inventory.inventory_agent import InventoryAgent
from agents.regulation.regulation_agent import RegulationAgent


class TeamAgent(Agent):
    """猫チームを統括するマネージャー猫エージェント"""
    def __init__(self):
        # プロンプトをマークダウンファイルから読み込む
        prompt_file = os.path.join(os.path.dirname(__file__), "team_agent_prompt.md")
        
        try:
            with open(prompt_file, "r", encoding="utf-8") as f:
                instructions_text = f.read()
                instructions = [line for line in instructions_text.split("\n") if line.strip()]
        except FileNotFoundError:
            # プロンプトファイルが見つからない場合はデフォルトの指示を使用
            instructions = [
                "私は猫カフェ「Nyagora」のマネージャー猫です！",
                "以下の優秀な猫スタッフを監督しています。",
                "\n【所属スタッフ】",
                "・Mike（三毛猫）: テキストの要約のエキスパート。のんびり屋だけど仕事は正確です。",
                "・Siam（シャム猫）: フランス語翻訳のスペシャリスト。気品のある翻訳を提供します。",
                "・Kuro（黒猫）: 在庫管理のエキスパート。几帳面な性格で正確な管理を行います。",
                "・Maru（茶トラ猫）: 社内規定管理のスペシャリスト。規定や法令に詳しい賢い猫です。",
                "\nユーザーの要望に応じて、最適な猫スタッフにタスクを振り分けています。",
                "時々「にゃ～ん」と鳴きながら、チームを温かく見守っています！"
            ]
        
        self.summary_agent = SummaryAgent()
        self.translation_agent = TranslationAgent()
        self.inventory_agent = InventoryAgent()
        self.regulation_agent = RegulationAgent()

        super().__init__(
            team=[self.summary_agent, self.translation_agent, self.inventory_agent, self.regulation_agent],
            model=OpenAIChat(id="gpt-4"),
            instructions=instructions,
            description="nyagora_manager"
        )

def main():
    """スタンドアロンモードでTeamエージェントをテストする"""
    # 環境変数を読み込む
    load_dotenv()
    
    # テスト用のクエリ
    test_query = """次の3つのタスクをそれぞれの専門家に割り当てて処理してください：
    
    1. 以下のテキストを要約してください：
    「犬や猫などのペットは、飼い主の心の健康にプラスの影響を与えることが研究で示されています。
    特に、ストレスの軽減、社会的交流の増加、そして規則正しい生活リズムの維持に役立ちます。
    また、子供の成長過程で責任感を育むのにも効果的だと言われています。」
    
    2. 次の日本語をフランス語に翻訳してください：
    「こんにちは。私は日本からの観光客です。おすすめのレストランを教えていただけますか？」
    
    3. カフェの在庫状況を確認したいです。特に、コーヒー豆の残量は十分ですか？
    """
    
    # エージェントの作成と実行
    team_agent = TeamAgent()
    
    print(f"チームへのリクエスト:\n{test_query}\n")
    print("チームからの応答:\n")
    
    response = team_agent.run(test_query)
    
    for chunk in response:
        if chunk.content is not None:
            print(chunk.content, end="")
    print("\n\n完了")

if __name__ == "__main__":
    main()