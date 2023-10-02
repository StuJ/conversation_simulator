import os

import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

# v1: run deliberation as completion, passing root conversation 
# as input and telling it to debate between preset personalities,
# passing the presets as system prompt, to generate their response.

# v2: run deliberation as chat, creating set of sub-agents with their
# own descriptions as system prompt, passing the root conversation as
# context and told to generate their response. This actually seems easier
# and allows for arbitrary hierarchy of agents.


class Agent(object):
    """An agent in a conversation."""

    def __init__(self, name, description, prompt_template) -> None:
        self.name = name
        system_prompt = prompt_template.format(name=name, desc=description)
        self.messages = [{'role': 'system', 'content': system_prompt}]
    
    def deliberate(self, input, model='gpt-4'):
        """Simulate an internal conversation to decide which response to give.
        Returns the response.

        Args:
            input (str): The input to the agent.
            model (str, optional): The model to use. Defaults to 'gpt-4'.
        
        Returns:
            str: The agent's response.
        """
        pass


    
    def get_response(self, input, model='gpt-4', deliberate=False):
        """Get agent's response via OpenAI, given input.
        Appends the response to the agent's messages then returns it.
        Optionally run a deliberation process, where
        the agent simulates an internal conversation to decide which response to give.

        Args:
            input (str): The input to the agent.
            model (str, optional): The model to use. Defaults to 'gpt-4'.
            deliberate (bool, optional): Whether to deliberate. Defaults to False.
        
        Returns:
            str: The agent's response.
        """

        self.messages.append({'role': 'user', 'content': input})
        if deliberate:
            deliberated_input = self.deliberate(input, model=model)

        response = openai.ChatCompletion.create(
            model=model,
            messages=self.messages,
            temperature=1.0
        )
        newest = response.choices[0].message
        self.messages.append(newest)

        return newest['content']
    
