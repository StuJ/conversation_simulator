# Run the conversation between agents
# and write the output to a file.
import argparse
import datetime
import os
import pathlib

import agent, conversation, prompts, utils


def handle(run_name: str, mode: str, model: str, conv_len: int):
    """Handle the conversation between agents.
    Runs conversation according to prompts, agents
    and subagents defined in prompts.py. Outputs
    conversation to StdOut and writes conversation
    to 'conversations/<mode>/<run_name>.md', formatted
    according to format_prompt in prompts.py.

    Args:
        run_name (str): To name output file.
        mode (str): E.g. 'prediction', 'prediction_subagents'
            or 'debate'.
        model (str): Model to use for conversation, e.g. 'gpt-4'.
        conv_len (int): Max num of statements in conversation.
    """

    agent_data = prompts.get_agent_data(mode)
    if 'subagents' in mode:
        subagent_conv = True

    conv = conversation.run_conversation(
        agents=agent.Agent.instantiate_agents(agent_data), 
        initial_prompt='Begin the conversation',
        conversation_length=conv_len,
        model=model,
        subagent_conv=subagent_conv
    )
    output = utils.format_output(conv)

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

    parser = argparse.ArgumentParser()
    parser.add_argument('--run_name', type=str, default=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S"), help='To name output file, defaults to current date and time.')
    parser.add_argument('--mode', type=str, default='prediction', help="E.g. 'prediction', 'prediction_subagents' or 'debate'")
    parser.add_argument('--model', type=str, default='gpt-4-turbo-preview', help='Model to use for conversation, defaults to "gpt-4-turbo-preview".')
    parser.add_argument('--conv_len', type=int, default=30, help='Max num of statements in conversation')
    args = parser.parse_args()

    handle(
        run_name=args.run_name,
        mode=args.mode,
        model=args.model,
        conv_len=args.conv_len
    )
