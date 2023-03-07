import openai
from decouple import config

API_KEY = config('OPENIA_KEY')
openai.api_key = API_KEY

conversation=[{"role": "system", "content": "You are a helpful assistant."}]

def getCost(tokens):
    return tokens / 1000 *0.002

while(True):
    user_input = input("")     
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=2,
        max_tokens=250,
        top_p=0.9
    )

    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    print("\n" + response['choices'][0]['message']['content'])
    print("Cost: {:.5f} $ with {} used tokens \n".format(getCost(response['usage']['total_tokens']), response['usage']['total_tokens']))
