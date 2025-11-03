from openai import OpenAI

client = OpenAI(
    api_key="EMPTY",  # vLLM 无需密钥，任意字符串即可
    base_url="http://localhost:8000/v1"  # 端口需与启动命令一致
)

modelpath = 'the path to your model'
def use_llm(modelpath,query,max_tokens=1000,temperature=0.7):
    response = client.chat.completions.create(
        model=modelpath,
        messages=[
            {"role": "system", "content": "你是一个智能AI助手，你需要对用户的问题进行回答"},
            {"role": "user", "content": query}
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        stream=True
    )
    full_text = ""
    for chunk in response:
        full_text += chunk.choices[0].text
        print(chunk.choices[0].text, end="", flush=True)

    return full_text

if __name__ == '__main__':
    query = input('输入你的问题，输入q、quit或exit退出：')
    while True:
        if query.lower() == 'q' or query.lower() == 'quit' or query.lower() == 'exit':
            print('再见')
            break
        else:
            response = use_llm(modelpath,query)