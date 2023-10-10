import os

import openai

import converse

openai.api_key = os.getenv("OPENAI_API_KEY")

# v1: run deliberation as completion, passing root conversation 
# as input and telling it to debate between preset personalities,
# passing the presets as system prompt, to generate their response.

# v2: run deliberation as chat, creating set of sub-agents with their
# own descriptions as system prompt, passing the root conversation as
# context and told to generate their response. This actually seems easier
# and allows for arbitrary hierarchy of agents. Though in this approach
# the high level conversation isn't an agent, it's just coordinating
# conversations between the orgs. High level needs to just call agents,
# which is what run_conversation already does. So we just need to
# instantiate the high level agent, which doesn't have a system prompt,
# then run conversations between sub agents. Does the high level agent
# summarise the conversation between sub agents? Or do sub agents generate
# their own statement? I think the high level agent should summarise the
# conversation between sub agents, and then the sub agents should generate
# their own statement. So the high level agent is just a coordinator, and
# the sub agents are the ones that are actually deliberating. The high level
# agent should have a system prompt, which is the description of the
#  organisation. The sub agents should have a system prompt, which is the
# description of the agent. The high level agent should have a user prompt,
# which is the conversation between the sub agents.


class Agent(object):
    """An agent in a conversation."""

    def __init__(self, data: dict, prompt_template: str) -> None:
        self.name = data['name']
        self.desc = data['description']
        system_prompt = prompt_template.format(name=self.name, desc=self.desc)
        self.messages = [{'role': 'system', 'content': system_prompt}]
        self.subagents = self.instantiate_agents(data['subagents'])
    
    @staticmethod
    def instantiate_agents(data: dict):
        agents = data['agents']
        return [Agent(agent, data['prompt_template']) for agent in agents]
    
    def deliberate(self, model: str = 'gpt-4'):
        """Deliberate between subagents, generating a response.

        Args:
            model (str, optional): The model to use. Defaults to 'gpt-4'.
        
        Returns:
            str: The agent's response.
        """

        # Run the conversation between subagents.
        deliberation = converse.run_conversation(self.subagents)

        # Summarise the conversation to generate a response.
        prompt = self.messages + '\n'.join(deliberation)
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            temperature=1.0
        )
        newest = response.choices[0].text
        self.messages.append(newest)

        return newest
   
    def get_response(self, input: str, model: str = 'gpt-4'):
        """Get agent's response via OpenAI, given input.
        Appends the response to the agent's messages then returns it.

        Args:
            input (str): The input to the agent.
            model (str, optional): The model to use. Defaults to 'gpt-4'.
        
        Returns:
            str: The agent's response.
        """

        self.messages.append({'role': 'user', 'content': input})

        # If agent has subagents, run a conversation between them
        # to decide on the higher agent's response.
        if self.subagents:
            return self.deliberate(self.subagents, model)

        response = openai.ChatCompletion.create(
            model=model,
            messages=self.messages,
            temperature=1.0
        )
        newest = response.choices[0].message
        self.messages.append(newest)

        return newest['content']
