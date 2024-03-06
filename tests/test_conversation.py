from unittest.mock import patch

from converse.conversation import run_conversation


def test_run_conversation(agent_obj):
    initial_prompt = 'Hello'
    conversation_length = 10    
    model = 'gpt-4'
    agents = [agent_obj, agent_obj]
    subagent_conv = True

    with patch('converse.agent.Agent.get_response') as mocked_get_response:
        responses = [(f'Test response {i}', None) for i in range(conversation_length)]
        mocked_get_response.side_effect = responses
        result = run_conversation(agents, initial_prompt, conversation_length, model, subagent_conv)

        assert isinstance(result, list)
        assert len(result) == conversation_length + 1  # Including initial prompt
        expected_conversation = [initial_prompt] + [r[0] for r in responses]
        assert result == expected_conversation
