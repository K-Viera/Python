import openai
from decouple import config
from modules import Cost

API_KEY = config('OPENIA_KEY')
openai.api_key = API_KEY

response=openai.Completion.create(
    model='curie:ft-personal-2023-03-07-23-56-50',
    prompt='i am having trouble with my account')
    
print("\n" + response['choices'][0]['text'])
Cost.printCost(response['model'],response['usage']['total_tokens'])