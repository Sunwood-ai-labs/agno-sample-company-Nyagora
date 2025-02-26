import os
from agno.agent import Agent
from agno.models.openai import OpenAIChat

class BaseAgent(Agent):
    """基本エージェントクラス"""
    def __init__(self, name: str, instructions: str):
        super().__init__(
            name=name,
            model=OpenAIChat(
                id="gpt-4",
                api_key=os.environ.get("OPENAI_API_KEY")
            ),
            instructions=instructions
        )

__all__ = ["BaseAgent"]
