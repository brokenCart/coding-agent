import argparse
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from config import MAX_AGENT_ITERATIONS
from prompts import system_prompt

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
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(MAX_AGENT_ITERATIONS):
        try:
            final_response = generate_content(client, messages, args.verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                return
        except Exception as e:
            print(f"Error in generate_content: {e}")

    print(f"Maximum iterations ({MAX_AGENT_ITERATIONS}) reached")
    sys.exit(1)


def generate_content(
    client: OpenAI, messages: list[dict[str, str]], verbose: bool = False
):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    if not response.usage:
        raise RuntimeError(
            "Failed API call. Please check your API key and model availability."
        )

    if verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    messages.append(message)

    if not message.tool_calls:
        return message.content

    for tool_call in message.tool_calls:
        if tool_call.type != "function":
            continue
        result_message = call_function(tool_call, verbose)
        if not result_message.get("content"):
            raise RuntimeError(f"Empty function response for {tool_call.function.name}")
        if verbose:
            print(f"-> {result_message['content']}")
        messages.append(result_message)


if __name__ == "__main__":
    main()
