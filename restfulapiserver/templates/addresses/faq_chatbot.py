import openai

openai.api_key = "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"

messages = []

while True:
        user_content = input("질문: ")
        messages.append({"role": "user", "content": user_content})

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        content_save = completion['choices'][0]['message']['content'].strip()

        messages.append({"role": "user", "content": content_save})

        print("GPT: {0}\n".format(content_save))