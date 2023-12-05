# Run the conversation between agents
# and write the output to a file.
import os
import pathlib

import agent, converse, prompts, utils


def handle(run_name: str, mode: str, conversation_length: int, subagent_conv: bool):
    """Handle the conversation between agents.
    Runs conversation according to prompts, agents
    and subagents defined in prompts.py. Outputs
    conversation to StdOut and writes conversation
    to 'conversations/<mode>/<run_name>.md', formatted
    according to format_prompt in prompts.py.

    Args:
        run_name (str): To name output file.
        mode (str): E.g. 'prediction', 'prediction-subagents'
            or 'debate'.
        conversation_length (int): Max num of statements in conversation.
        subagent_conv (bool): Whether to enable subagent conversation.
    """

    agent_data = prompts.get_agent_data(mode)

    conversation = converse.run_conversation(
        agents=agent.Agent.instantiate_agents(agent_data), 
        initial_prompt='Begin the conversation',
        conversation_length=conversation_length,
        model='gpt-4-1106-preview',
        subagent_conv=subagent_conv
    )
    output = utils.format_output(conversation)

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
    conversation_length = 30
    run_name = f'15-china-len-{conversation_length}'
    mode = 'prediction'
    subagent_conv = False

    handle()
