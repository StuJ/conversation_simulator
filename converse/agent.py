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

    def __init__(self, agent_data: dict, context: str) -> None:
        self.name = agent_data['name']
        self.desc = agent_data['description']
        system_prompt = context['prompt_template'].format(name=self.name, desc=self.desc)
        self.messages = [{'role': 'system', 'content': system_prompt}]
        self.conversation = ''
        self.subagents = None

        if subagents := (agent_data.get('subagents')):
            self.deliberate_len = subagents['conversation_len']
            self.deliberate_prompt = subagents['initial_prompt']
            self.subagents = self.instantiate_agents(subagents)
    
    @staticmethod
    def instantiate_agents(data: dict):
        return [Agent(agent, data) for agent in data['agents']]
    
    def chat_completion(self, messages: str, model: str = 'gpt-4') -> str:
        """Get chat completon response from OpenAI, given input messages.

        Args:
            messages (str): The input messages.
            model (str, optional): The model to use. Defaults to 'gpt-4'.
        
            Returns:
                str: The text response.
        """
    
    def deliberate(self, agents: list, model: str = 'gpt-4'):
        """Deliberate between agents, generating a response.
        Runs a conversation between agents, then summarises the
        conversation to generate a response.

        Args:
            agents (list): The agents to deliberate between.
            model (str, optional): The model to use. Defaults to 'gpt-4'.
        
        Returns:
            str: The agent's response.
        """

        # Run the conversation between subagents.
        print(f'{self.name} deliberation:\n')
        deliberation = converse.run_conversation(
            agents=agents,
            initial_prompt=self.deliberate_prompt,
            conversation_length=self.deliberate_len,
            model=model
        )

        # Summarise the conversation to generate a response.
        prompt = self.conversation + '\n'.join(deliberation)
        response = openai.ChatCompletion.create(
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

        input_messages = self.messages

        # If agent has subagents, run a conversation
        # between them for the agent to generate its 
        # response from.
        if self.subagents:
            print(f'{self.name} deliberation:\n')
            deliberation = converse.run_conversation(
                agents=self.subagents,
                initial_prompt=self.deliberate_prompt,
                conversation_length=self.deliberate_len,
                model=model
            )
            deliberation_prompt = (
                f'Statements: {self.conversation}\n' +
                f'{self.name} deliberation:\n' + 
                '\n'.join(deliberation)
            )
            # Input the deliberation to the agent to summarise, 
            # but don't save the deliberation to the agent's messages.
            input_messages = self.messages + [{'role': 'user', 'content': deliberation_prompt}]

        # TODO: fix - this is appending the input to the agent's messages
        # when we only want to do that when there are no subagents.
        self.messages.append({'role': 'user', 'content': input})
        self.conversation += input + '\n'

        response = openai.ChatCompletion.create(
            model=model,
            messages=input_messages,
            temperature=1.0
        )
        newest = response.choices[0].message
        self.messages.append(newest)
        self.conversation += newest.content + '\n'

        return newest['content']
