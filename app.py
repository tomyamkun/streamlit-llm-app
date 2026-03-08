from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os

def get_expert_response(input_text, expert_type):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    
    if expert_type == "プログラミングの専門家":
        system_content = "あなたは優秀なプログラミングの専門家です。コードの書き方やエラーの解決方法について、初心者にもわかりやすく教えてください。"
    elif expert_type == "料理の専門家":
        system_content = "あなたは一流の料理の専門家です。レシピや調理のコツ、食材の保存方法について、美味しく作るためのアドバイスを提供してください。"
    elif expert_type == "フィットネスの専門家":
        system_content = "あなたはプロのフィットネス専門家です。効果的なトレーニング方法や健康的な食事について、論理的かつモチベーションが上がるようにアドバイスしてください。"
    else:
        system_content = "あなたは親切なAIアシスタントです。"
        
    messages = [
        SystemMessage(content=system_content),
        HumanMessage(content=input_text)
    ]
    
    response = llm.invoke(messages)
    
    return response.content

st.title("専門家AI相談アプリ")

st.write("### アプリの概要")
st.write("このアプリは、ユーザーが選んだ分野の「専門家AI」に対して、質問や相談ができるチャットアプリです。")
st.write("### 操作方法")
st.write("1. 相談したい専門家の種類をラジオボタンから選択してください。")
st.write("2. 質問や相談したい内容をテキストボックスに入力してください。")
st.write("3. 「相談する」ボタンを押すと、専門家AIからの回答が表示されます。")

st.divider()

expert_type = st.radio(
    "相談する専門家を選択してください:",
    ["プログラミングの専門家", "料理の専門家", "フィットネスの専門家"]
)

input_text = st.text_input("質問・相談内容を入力してください:")

if st.button("相談する"):
    if input_text:
        with st.spinner(f"{expert_type}が回答を考えています..."):
            try:
                answer = get_expert_response(input_text, expert_type)
                
                st.write(f"### {expert_type}からの回答")
                st.write(answer)
            except Exception as e:
                st.error("エラーが発生しました。APIキーの設定などを確認してください。")
                st.error(f"詳細: {e}")
    else:
        st.warning("質問・相談内容を入力してから「相談する」ボタンを押してください。")