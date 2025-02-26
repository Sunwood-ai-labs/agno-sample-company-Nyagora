import streamlit as st
from agents import TeamAgent
from dotenv import load_dotenv
import os

# 環境変数を読み込む
load_dotenv()

def main():
    st.title("エージェントシステム")

    user_input = st.text_area("リクエストを入力してください:", height=150)

    if st.button("送信"):
        if user_input:
            with st.spinner("処理中..."):
                # チームエージェントを実行
                team_agent = TeamAgent()
                response = team_agent.run(user_input, stream=True)

            full_response_text = ""
            response_placeholder = st.empty()

            for chunk in response:
                if (chunk.content is not None):
                    full_response_text += chunk.content
                    response_placeholder.markdown(full_response_text)

            st.success("タスクが完了しました！")
            st.write("---")
            st.write("使用したエージェント:")
            for member in team_agent.team:
                st.write(f"- {member.name}")
        else:
            st.warning("リクエストを入力してください。")

if __name__ == "__main__":
    main()
