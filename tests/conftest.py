import pytest

from converse.agent import Agent


@pytest.fixture
def agent():
    return {'name': 'Test Agent', 'description': 'A test agent'}


@pytest.fixture
def agent_data(agent):
    return {
        'prompt_template': 'Hello, I am {name}. {desc}',
        'agents': [agent, agent]
    }


@pytest.fixture
def subagent_conv_context(agent):
    agent_data_with_subagents = {
        'name': 'Test Agent with subagents',
        'description': 'A test agent with subagents',
        'subagents': {
            'prompt_template': 'Hello, I am subagent {name}. {desc}',
            'conversation_len': 5,
            'initial_prompt': 'Subagent conversation:',
            'agents': [agent, agent]
        }
    }
    return {
        'prompt_template': 'Hello, I am agent with subagents {name}. {desc}',
        'agents': [agent_data_with_subagents, agent_data_with_subagents]
    }


@pytest.fixture
def agent_obj(agent_data, agent):
    return Agent(agent, agent_data)
