from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

def get_session_history(session_id:str,store):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

def get_chat_response(prompt,store,session_id,api_key):
    model = ChatOpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-turbo",
        api_key=api_key
    )
    prompt_template = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name="history"),
        ("human","{input}")
    ])
    basic_chain = prompt_template | model
    chain = RunnableWithMessageHistory(basic_chain,lambda sid:get_session_history(sid,store),
                                       input_messages_key="input",
                                       history_messages_key="history")
    response = chain.invoke({"input":prompt},{"configurable":{"session_id":session_id}})
    return response.content
    print(response2)
