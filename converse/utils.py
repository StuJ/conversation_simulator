import os

import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff


openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_completion(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(50))
def completion_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)
