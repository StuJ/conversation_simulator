import os

import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff

import prompts


openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_completion(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(50))
def completion_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)


def format_output(conversation: list[str]) -> str:
    """Formats the output of a conversation,
    according to instructions given in the 'format prompt'
    variable in prompts.py.

    Args:
        conversation (list[str]): Conversation as list of strings.
    
    Returns:
        str: formatted output as a single string.
    """
  
    conv_string = '\n\n'.join(conversation)
    messages = [{
        'role': 'user', 
        'content': f'{prompts.format_prompt}\n{conv_string}'
    }]
    response = chat_completion(
        model='gpt-4-1106-preview',
        messages=messages
    )
    return response.choices[0].message.content
