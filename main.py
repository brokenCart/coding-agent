import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

parser = argparse.ArgumentParser(description="ChatBot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


def main():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENROUTER_API_KEY is not set in the environment variables."
        )

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

    generate_content(client, messages)


def generate_content(client: OpenAI, messages):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    if not response.usage:
        raise RuntimeError(
            "Failed API call. Please check your API key and model availability."
        )

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
