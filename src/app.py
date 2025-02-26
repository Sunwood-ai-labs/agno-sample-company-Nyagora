import streamlit as st
from agents import TeamAgent
from dotenv import load_dotenv
import os
import time

# 環境変数を読み込む
load_dotenv()

def check_api_key():
    """APIキーの状態をチェックする"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return False, "❌ OpenAI APIキーが設定されていません"
    elif api_key.startswith("sk-"):
        return True, "✅ OpenAI APIキーが正しく設定されています"
    else:
        return False, "⚠️ OpenAI APIキーの形式が正しくありません"

def main():
    # サイドバーにAPIキーの状態を表示
    st.sidebar.title("システム状態")
    api_status, api_message = check_api_key()
    st.sidebar.markdown(api_message)
    
    if not api_status:
        st.sidebar.error("APIキーを.envファイルで設定してください")
        return

    st.title("🐱 Nyagora - 猫のエージェントシステム")
    st.markdown("""
    ### システム概要
    Nyagoraは、賢い猫たちがあなたのタスクをサポートする特別なシステムです。
    各猫エージェントは独自の専門分野を持ち、協力してタスクを処理します：
    
    - 📝 ミケ: テキストの要約を得意とする三毛猫
    - 🌏 シャム: フランス語翻訳のエキスパートであるシャム猫
    """)

    user_input = st.text_area("リクエストを入力してください:", height=150)
    col1, col2 = st.columns(2)

    if st.button("送信"):
        if user_input:
            spinner_text = "にゃ～ん...処理中..."
            my_bar = st.progress(0)
            
            start_time = time.time()
            with st.spinner(spinner_text):
                # チームエージェントを実行
                team_agent = TeamAgent()
                st.session_state['processing_start_time'] = start_time
                response = team_agent.run(user_input, stream=True)

                # プログレスバーを更新
                for i in range(100):
                    my_bar.progress(i + 1)

            full_response_text = ""
            response_placeholder = st.empty()

            for chunk in response:
                if (chunk.content is not None):
                    full_response_text += chunk.content
                    response_placeholder.markdown(full_response_text)
            
            # 処理時間を計算して保存
            end_time = time.time()
            processing_time = end_time - st.session_state['processing_start_time']

            st.success("にゃ！タスクが完了しました！ 🐾")
            
            with col1:
                st.markdown("### 担当した猫エージェント")
                for member in team_agent.team:
                    if "mike" in member.name.lower():
                        emoji = "🐱"
                        display_name = "Mike（三毛猫）"
                    else:
                        emoji = "😺"
                        display_name = "Siam（シャム猫）"
                    st.info(f"{emoji} {display_name}")
            with col2:
                st.markdown("### 処理詳細")
                # 処理時間を適切なフォーマットで表示
                if processing_time < 60:
                    time_display = f"{processing_time:.1f}秒"
                else:
                    time_display = f"{processing_time / 60:.1f}分"
                st.info(f"処理時間: {time_display}")
        else:
            st.warning("リクエストを入力してください。")

if __name__ == "__main__":
    main()
