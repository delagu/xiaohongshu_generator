import streamlit as st
from utils02 import get_chat_response

with st.sidebar:
    api_key = st.text_input("请输入OpenAI API Key：",type="password")
    st.markdown("[获取OpenAI API key](https://platform.openai.com/account/api-keys)")

st.title("💬 克隆ChatGPT")

if "store" not in st.session_state:
    st.session_state["store"] = {}
    st.session_state["messages"] = [{"role":"ai","content":"你好，我是你的AI助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role":"human","content":prompt})
    st.chat_message("human").write(prompt)
    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt,st.session_state["store"],"session_1",api_key)
        print(st.session_state["store"])
    st.session_state["messages"].append({"role":"ai","content":response})
    st.chat_message("ai").write(response)
