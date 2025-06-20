import openai
from config import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def generate_response(prompt_text):
    response = openai.ChatCompletion.create(
        model='gpt-4o',
        messages=[
            {"role": "system", "content": "You are a helpful email assistant. Respond professionally."},
            {"role": "user", "content": prompt_text}
        ]
    )
    return response.choices[0].message['content']
