from agno.agent import Agent
from agno.models.openai import OpenAIChat
from .summary_agent import SummaryAgent
from .translation_agent import TranslationAgent
from .inventory_agent import InventoryAgent
from .regulation_agent import RegulationAgent

class TeamAgent(Agent):
    def __init__(self):
        self.summary_agent = SummaryAgent()
        self.translation_agent = TranslationAgent()
        self.inventory_agent = InventoryAgent()
        self.regulation_agent = RegulationAgent()

        super().__init__(
            team=[self.summary_agent, self.translation_agent, self.inventory_agent, self.regulation_agent],
            model=OpenAIChat(id="gpt-4"),
            instructions=[
                "私は猫カフェ「Nyagora」のマネージャー猫です！",
                "以下の2匹の優秀な猫スタッフを監督しています。",
                "\n【所属スタッフ】",
                "・Mike（三毛猫）: テキストの要約のエキスパート。のんびり屋だけど仕事は正確です。",
                "・Siam（シャム猫）: フランス語翻訳のスペシャリスト。気品のある翻訳を提供します。",
                "・Kuro（黒猫）: 在庫管理のエキスパート。几帳面な性格で正確な管理を行います。",
                "・Maru（茶トラ猫）: 社内規定管理のスペシャリスト。規定や法令に詳しい賢い猫です。",
                "\nユーザーの要望に応じて、最適な猫スタッフにタスクを振り分けています。",
                "時々「にゃ～ん」と鳴きながら、チームを温かく見守っています！"
            ],
            description="nyagora_manager"
        )
