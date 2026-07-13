import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {
        "role": "user",
        "content": "Who won the FIFA World Cup in 2022? Answer in one word.",
    },
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)
print(response.choices[0].message.content)
