from .base_agent import BaseAgent

class TranslationAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="translation_agent",
            instructions="私はテキストをフランス語に翻訳することを専門とするアシスタントです。"
        )
