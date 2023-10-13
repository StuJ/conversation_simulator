# Unit tests for agent.py
import pytest

from converse import agent


@pytest.fixture
def agent_data():
    return {
        'agent_level': 'Highest',
        'prompt_template': 'name: {name}, desc: {desc}',
        'agents':
        [
            {
                'name': 'agent1',
                'description': 'description1',
                'subagents': {
                    'conversation_len': 5,
                    'initial_prompt': 'initial_prompt1',
                    'prompt_template': 'name: {name}, desc: {desc}',
                    'agents': []
                }
            },
            {
                'name': 'agent2',
                'description': 'description2',
                'subagents': {
                    'conversation_len': 6,
                    'initial_prompt': 'initial_prompt2',
                    'prompt_template': 'name: {name}, desc: {desc}',
                    'agents': []
                }
            }
        ]
    }


@pytest.fixture
def agent_with_subagents(agent_data):
    for i in [0, 1]:
        agent_data['agents'][i]['subagents']['agents'] = [
            {
                'name': 'subagent1',
                'description': 'description',
                'agents': []
            },
            {
                'name': 'subagent2',
                'description': 'description'
            }
        ]
    return agent.Agent(agent_data)


def test_agent_instantiation(agent_data):
    agent.Agent(agent_data)


def test_agent_instantiation_with_subagents(agent_with_subagents):
    assert len(agent_with_subagents.subagents) == 2


def test_instantiate_agents(agent_data):
    agents = agent.Agent.instantiate_agents({'agents': [agent_data]})
    assert len(agents) == 1
    assert agents[0].name == 'agent'
    assert agents[0].desc == 'description'


def test_instantiate_agents_with_subagents(agent_data):
    agent_data['agents'] = [
        {
            'name': 'subagent1',
            'description': 'description',
            'agents': []
        },
        {
            'name': 'subagent2',
            'description': 'description',
            'agents': []
        }
    ]
    agents = agent.Agent.instantiate_agents({'agents': [agent_data]})
    assert len(agents) == 1
    assert len(agents[0].subagents) == 2

