import itertools


def run_conversation(
        agents: list,
        initial_prompt: str,
        conversation_length: int,
        model: str,
        deliberate: bool = True
    ) -> list[str]:
    """Run a conversation between agents.

    Args:
        agents (list): The agents to converse.
        initial_prompt (str): The initial prompt to start the conversation.
        conversation_length (int): The length of the conversation.
        model (str): The model to use.
        deliberate (bool, optional): Whether to deliberate. Defaults to True.
    
    Returns:
        list[str]: The conversation.
    """

    conversation = [initial_prompt]
    # Loop through agent, passing output of one to input of other.

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

        response = agent.get_response(input_responses, model, deliberate)
        print(f'{response}\n')

        for name in next_input_responses.keys():
            if name != agent.name:
                next_input_responses[name].append(response)

        conversation.append(response)

        # Length must be one more than the conversation length
        # because of the initial prompt.
        if len(conversation) > conversation_length:
            break
    print('---------------------------')

    return conversation
