from openai import OpenAI

client = OpenAI(api_key="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")

def chat_with_gpt(prom):
    response = client.chat.Completions.create(
        model="gpt-3.5-Turbo",
        messages=[("role": "user", "content": prompt)]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["quit", "exit", "Bye", "Sair", "Tchau"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)