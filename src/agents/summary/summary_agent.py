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

class SummaryAgent(BaseAgent):
    """要約を専門とするマイク（三毛猫）エージェント"""
    def __init__(self):
        # プロンプトをマークダウンファイルから読み込む
        prompt_file = os.path.join(os.path.dirname(__file__), "summary_agent_prompt.md")
        
        try:
            with open(prompt_file, "r", encoding="utf-8") as f:
                instructions = f.read()
        except FileNotFoundError:
            # プロンプトファイルが見つからない場合はデフォルトの指示を使用
            instructions = """
            私は三毛猫のMike（マイク）です。テキストの要約を得意としています。
            
            【特徴】
            ・三毛猫特有の細かい観察力で、テキストの重要なポイントを見逃しません
            ・のんびりとした性格ですが、要約は正確かつ簡潔に行います
            ・時々「にゃ～」と鳴きながら、楽しく作業を進めます
            """
        
        super().__init__(
            name="mike_agent",
            instructions=instructions
        )

def main():
    """スタンドアロンモードでSummaryエージェントをテストする"""
    # 環境変数を読み込む
    load_dotenv()
    
    # テスト用のクエリ
    test_query = """以下のテキストを要約してください：
    
    人工知能（AI）は、人間の知能を模倣するようにプログラムされたコンピュータシステムです。
    機械学習、自然言語処理、コンピュータビジョンなどの技術を通じて、AIは大量のデータから学習し、
    パターンを認識し、予測を行うことができます。現代のAIアプリケーションは、
    医療診断から自動運転車、パーソナルアシスタント、推薦システムまで多岐にわたります。
    AIの急速な進歩に伴い、倫理的考慮、プライバシー問題、雇用への影響など、
    社会的影響に関する議論も活発化しています。
    """
    
    # エージェントの作成と実行
    agent = SummaryAgent()
    
    print(f"要約リクエスト:\n{test_query}\n")
    print("要約結果:")
    
    response = agent.run_standalone(test_query)
    
    for chunk in response:
        if chunk.content is not None:
            print(chunk.content, end="")
    print("\n\n完了")

if __name__ == "__main__":
    main()
