import itertools


def run_conversation(
        agents: list,
        initial_prompt: str,
        conversation_length: int,
        model: str,
        subagent_conv: bool = True
    ) -> list[str]:
    """Run a conversation between agents.

    Args:
        agents (list): The agents to converse.
        initial_prompt (str): The initial prompt to start the conversation.
        conversation_length (int): The length of the conversation.
        model (str): The model to use.
        subagent_conv (bool, optional): Whether to run conversation between subagents.
            Defaults to True.
    
    Returns:
        list[str]: The conversation.
    """

    conversation = [initial_prompt]
    conv_len = 0

    # Save next input responses for each agent.
    next_input_responses = {agent.name: [] for agent in agents}

    # For each agent, feed the comments since they last spoke 
    # as user input to their response.
    print('---------------------------')
    for agent in itertools.cycle(agents):

        if len(next_input_responses[agent.name]) > 0:
            input_responses = '\n'.join(next_input_responses[agent.name])
            next_input_responses[agent.name] = []
        else:
            input_responses = initial_prompt

        response, subagent_output = agent.get_response(
            input_responses, model, subagent_conv
        )
        print(f'{response}\n')

        for name in next_input_responses.keys():
            if name != agent.name:
                next_input_responses[name].append(response)

        conversation.append(response)
        conv_len += 1
        if subagent_output:
            conversation.append(subagent_output)

        if conv_len >= conversation_length:
            break

    print('---------------------------')

    return conversation
