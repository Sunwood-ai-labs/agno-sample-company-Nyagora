from agno.agent import Agent
from agno.models.openai import OpenAIChat
from .summary_agent import SummaryAgent
from .translation_agent import TranslationAgent

class TeamAgent(Agent):
    def __init__(self):
        self.summary_agent = SummaryAgent()
        self.translation_agent = TranslationAgent()
        
        super().__init__(
            team=[self.summary_agent, self.translation_agent],
            model=OpenAIChat(id="gpt-4o"),
            instructions=[
                "私はチームリーダーとして、2つの専門エージェントを管理します。",
                "テキストの要約が必要な場合は要約エージェントに、フランス語翻訳が必要な場合は翻訳エージェントに、",
                "適切にタスクを振り分けて、ユーザーの要望に応えます。"
            ],
            description="チームリーダーエージェント"
        )
