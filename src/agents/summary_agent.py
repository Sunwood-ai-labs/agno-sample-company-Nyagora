from .base_agent import BaseAgent

class SummaryAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="summary_agent",
            instructions="私はテキストの要約を専門とするアシスタントです。"
        )
