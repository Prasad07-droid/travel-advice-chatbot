import openai
# Set your OpenAI API key
openai.api_key = "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"
while True:
    user_input = input("you: ")
    if user_input.lower() == "quit":
        print("bot: Goodbye!")
        break
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a travel advice bot, provide information related to travel."},
            {"role": "user", "content": user_input}
        ]
    )
    
    print("bot:", response.choices[0].message['content'])