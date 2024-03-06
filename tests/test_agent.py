from unittest.mock import patch

from converse.agent import Agent


def test_initialization(agent_obj):
    assert agent_obj.name == 'Test Agent'
    assert agent_obj.desc == 'A test agent'
    assert 'system' in agent_obj.messages[0]['role']
    assert 'Hello, I am Test Agent. A test agent' in agent_obj.messages[0]['content']


def test_instantiate_agents_with_valid_data(agent_data):
    agents = Agent.instantiate_agents(agent_data)
    assert len(agents) == 2
    for a in agents:
        assert isinstance(a, Agent)


def test_get_response_without_subagents(agent_obj):
    with patch('converse.utils.completion_with_backoff') as mocked_completion:
        mocked_completion.return_value.choices[0].message = {
            'role': 'assistant', 'content': 'Test response'
        }
        response, subagent_output = agent_obj.get_response('Hello')
        assert response == 'Test response'
        assert subagent_output is None
        assert len(agent_obj.messages) == 3

        # Test that the system message has been rendered and stored correctly.
        system_msg = agent_obj.messages[0]
        assert system_msg['role'] == 'system'
        assert 'Hello, I am Test Agent. A test agent' in system_msg['content']

        # Test the input message.
        input_msg = agent_obj.messages[1]
        assert input_msg['role'] == 'user'
        assert agent_obj.messages[1]['content'] == 'Hello'

        # Test the agent's response.
        response_msg = agent_obj.messages[2]
        assert response_msg['role'] == 'assistant'
        assert response_msg['content'] == 'Test response'


def test_get_response_with_subagents(subagent_conv_context):
    agent = Agent(subagent_conv_context['agents'][0], subagent_conv_context)

    with (patch('converse.utils.completion_with_backoff') as mocked_completion,
            patch('converse.converse.run_conversation') as mocked_converse):
        mocked_completion.return_value.choices[0].message = {
            'role': 'assistant', 'content': 'Test response'
        }
        mocked_converse.return_value = ['Subagent message']
        response, subagent_output = agent.get_response('Hello')

        # Assert correct calls made to run_conversation and completion_with_backoff.
        mocked_converse.assert_called_once()
        assert mocked_converse.call_args_list[0][1]['agents'] == agent.subagents
        assert mocked_converse.call_args_list[0][1]['initial_prompt'] == 'Subagent conversation:'
        assert mocked_converse.call_args_list[0][1]['conversation_length'] == 5
        assert mocked_converse.call_args_list[0][1]['model'] == 'gpt-4'

        mocked_completion.assert_called_once()
        assert mocked_completion.call_args_list[0][1]['model'] == 'gpt-4'
        completion_call_msg = mocked_completion.call_args_list[0][1]['messages']
        assert completion_call_msg[0]['role'] == 'user'
        assert 'Subagent conversation:' in completion_call_msg[0]['content']

        # Messages should be stored in the agent's messages attribute
        # and not contain the subagent conversation.
        assert response == 'Test response'
        assert subagent_output == 'Subagent message'
        assert len(agent.messages) == 3

        # Test that the system message has been rendered and stored correctly.
        system_msg = agent.messages[0]
        assert system_msg['role'] == 'system'
        assert 'Hello, I am agent with subagents' in system_msg['content']

        # Test the input message.
        input_msg = agent.messages[1]
        assert input_msg['role'] == 'user'
        assert agent.messages[1]['content'] == 'Hello'

        # Test the agent's response.
        response_msg = agent.messages[2]
        assert response_msg['role'] == 'assistant'
        assert response_msg['content'] == 'Test response'
