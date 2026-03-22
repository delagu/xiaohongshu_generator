from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from xiaohongshu_model import Xiaohongshu
import os

def generate_xiaohongshu(theme, api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_template_text),
        ("user", user_template_text)
    ])
    model = ChatOpenAI(
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model="qwen-turbo",
        api_key=api_key
    )
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    chain = prompt | model | output_parser
    result = chain.invoke({
        "parser_instructions": output_parser.get_format_instructions(),
        "theme": theme
    })
    return result

if __name__ == '__main__':
    print(generate_xiaohongshu("大模型", os.getenv("DASHSCOPE_API_KEY")))
