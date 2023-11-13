# Run the conversation between agents
# and write the output to a file.
import os
import pathlib

import agent, converse, prompts, utils


def format_output(conversation: list[str]) -> str:
    """Formats the output of a conversation,
    according to instructions given in the 'format prompt'
    variable in prompts.py.

    Args:
        conversation (list[str]): Conversation as list of strings.
    
    Returns:
        str: formatted output as a single string.
    """

    conv_string = '\n\n'.join(conversation)
    messages = [{
        'role': 'user', 
        'content': f'{prompts.format_prompt}\n{conv_string}'
    }]
    response = utils.chat_completion(
        model='gpt-4-1106-preview',
        messages=messages
    )

    return response.choices[0].message.content


def handle():
    """Handle the conversation between agents."""

    conversation_length = 20
    run_name = f'11-subagent-len-{conversation_length}'
    mode = 'prediction_subagents'
    agent_data = prompts.get_agent_data(mode)

    conversation = converse.run_conversation(
        agents=agent.Agent.instantiate_agents(agent_data), 
        initial_prompt='Begin the conversation',
        conversation_length=20,
        model='gpt-4-1106-preview',
        subagent_conv=True
    )

    output = format_output(conversation)

    output_dir = os.path.join(
        pathlib.Path(__file__).parent.resolve(),
        f'conversations/{mode}'
    )
    pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
    output_fname = os.path.join(output_dir, f'{run_name}.md')

    with open(output_fname, 'w+') as f:
        f.write(output)

    print(f'Written output to {output_fname}.')


if __name__ == '__main__':
    handle()
