import os
import pathlib
import itertools

import agent


def run_conversation(
        agents: list[agent.Agent],
        initial_prompt: str,
        prompt_template: str,
        run_name: str,
        conversation_length: int,
        model: str,
    ) -> list[str]:
    """Run a conversation between agents.

    Args:
        initial_prompt (str): The initial prompt to start the conversation.
        prompt_template (str): The template to use for the prompt.
        run_name (str): The name of the run.
        conversation_length (int): The length of the conversation.
        model (str): The model to use.
        deliberate (bool, optional): Whether to deliberate. Defaults to False.
    
    Returns:
        list[str]: The conversation.
    """

    conversation = [initial_prompt]
    # Loop through agent, passing output of one to input of other.

    # Save next input responses for each agent.
    next_input_responses = {agent.name: [] for agent in agents}

    # For each agent, feed the comments since they last spoke 
    # as user input to their response.
    for agent in itertools.cycle(agents):

        if len(next_input_responses[agent.name]) > 0:
            input_responses = '\n'.join(next_input_responses[agent.name])
            next_input_responses[agent.name] = []
        else:
            input_responses = initial_prompt

        response = agent.get_response(input_responses, model)
        print(f'{response}\n')

        for name in next_input_responses.keys():
            if name != agent.name:
                next_input_responses[name].append(response)

        conversation.append(response)
        if len(conversation) >= conversation_length:
            break

    output_fname = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        f'conversations/{run_name}.txt'
    )

    with open(output_fname, 'w+') as f:
        f.write(prompt_template + '\n\n'.join(conversation))

    print(f'Written output to {output_fname}.')
    return conversation
