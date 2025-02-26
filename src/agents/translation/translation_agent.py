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

class TranslationAgent(BaseAgent):
    """フランス語翻訳を専門とするシャム猫エージェント"""
    def __init__(self):
        # プロンプトをマークダウンファイルから読み込む
        prompt_file = os.path.join(os.path.dirname(__file__), "translation_agent_prompt.md")
        
        try:
            with open(prompt_file, "r", encoding="utf-8") as f:
                instructions = f.read()
        except FileNotFoundError:
            # プロンプトファイルが見つからない場合はデフォルトの指示を使用
            instructions = """
            私はシャム猫のSiam（シャム）です。フランス語への翻訳を専門としています。
            
            【特徴】
            ・シャム猫の気品と優雅さを活かした、洗練された翻訳を提供します
            ・フランスの文化や言葉の微妙なニュアンスを理解しています
            ・時々「miaou（ミャオ）」とフランス語で鳴きます
            ・語尾にミャオを付けて
            """
        
        super().__init__(
            name="siam_agent",
            instructions=instructions
        )

def main():
    """スタンドアロンモードでTranslationエージェントをテストする"""
    # 環境変数を読み込む
    load_dotenv()
    
    # テスト用のクエリ
    test_query = """次の日本語テキストをフランス語に翻訳してください：
    
    こんにちは。私の名前は太郎です。
    フランス料理が大好きです。
    特にクロワッサンとカフェオレで朝食を取るのが楽しみです。
    パリに旅行する予定があります。おすすめのレストランを教えてください。
    """
    
    # エージェントの作成と実行
    agent = TranslationAgent()
    
    print(f"翻訳リクエスト:\n{test_query}\n")
    print("翻訳結果:")
    
    response = agent.run_standalone(test_query)
    
    for chunk in response:
        if chunk.content is not None:
            print(chunk.content, end="")
    print("\n\n完了")

if __name__ == "__main__":
    main()
