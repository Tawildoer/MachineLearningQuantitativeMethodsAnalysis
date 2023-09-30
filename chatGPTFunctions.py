import openai

API_KEY = "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"

def chatGPTQuery(inputString, logging=False):
    openai.api_key = API_KEY
    conversation = [
    {"role": "user", "content": inputString},
    ]

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",  # ChatGPT model
    messages=conversation,
    max_tokens=1  # Adjust max_tokens as needed for response length
    )

# Extract and print the assistant's reply
    reply = response['choices'][0]['message']['content']
    if logging:
        print(reply)
    return reply