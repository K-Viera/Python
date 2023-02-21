from decouple import config
import openai

API_KEY = config('OPENIA_KEY')
openai.api_key = API_KEY

prompt = "Say this is a test"
engine="text-davinci-003"

response = openai.Completion.create(engine=engine, prompt=prompt, max_tokens=5)

print(response)
print(response["choices"][0]["text"])