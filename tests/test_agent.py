# Unit tests for agent.py
import pytest

from converse import agent


@pytest.fixture
def agent_data():
    return {
        'name': 'agent',
        'description': 'description',
        'agents': []
    }


@pytest.fixture
def agent_with_subagents(agent_data):
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
    return agent.Agent(agent_data)


def test_agent_instantiation(agent_data):
    agent.Agent(agent_data)


def test_agent_instantiation_with_subagents(agent_with_subagents):
    assert len(agent_with_subagents.subagents) == 2
    assert agent_with_subagents.subagents[0].parent == agent_with_subagents
    assert agent_with_subagents.subagents[1].parent == agent_with_subagents
    assert agent_with_subagents.subagents[0].parent.name == 'agent'
    assert agent_with_subagents.subagents[1].parent.name == 'agent'


def test_instantiate_agents(agent_data):
    agents = agent.instantiate_agents({'agents': [agent_data]})
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
    agents = agent.instantiate_agents({'agents': [agent_data]})
    assert len(agents) == 1
    assert len(agents[0].subagents) == 2
    assert agents[0].subagents[0].parent == agents[0]
    assert agents[0].subagents[1].parent == agents[0]
    assert agents[0].subagents[0].parent.name == 'agent'
    assert agents[0].subagents[1].parent.name == 'agent'


def test_agent_deliberate(agent_with_subagents):
    response = agent_with_subagents.deliberate()
    assert len(agent_with_subagents.messages) == 2
    assert response == agent_with_subagents.messages[1]
