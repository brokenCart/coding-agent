import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

parser = argparse.ArgumentParser(description="ChatBot")
parser.add_argument("user_prompt", type=str, help="User Prompt")
args = parser.parse_args()

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
        "content": args.user_prompt,
    },
]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
)

if not response.usage:
    raise RuntimeError("Failed API call. Please check your API key and model availability.")

print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Response tokens: {response.usage.completion_tokens}")
print(response.choices[0].message.content)
